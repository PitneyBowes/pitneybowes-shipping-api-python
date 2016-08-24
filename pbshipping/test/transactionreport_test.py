#
# Copyright 2016 Pitney Bowes Inc.
# Licensed under the MIT License (the "License"); you may not use this file 
# except in compliance with the License.  You may obtain a copy of the License 
# in the LICENSE file or at 
#
#    https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT 
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and 
# limitations under the License.
#
# File: transactonreport_test.py
# Description: transaction report management related tests
#

import json
import datetime
import unittest
import test_util
from pbshipping import *

class TestTransactionReport(unittest.TestCase):

    def setUp(self):
        test_util.setup_env()        
        self.auth_obj = AuthenticationToken(api_key=test_util._test_api_key, 
                                            api_secret=test_util._test_api_secret)
        self.developer = test_util.setup_developer(self.auth_obj)
        merchant, acct_num = test_util.setup_merchant(self.auth_obj, self.developer)
        self.shipperId = merchant.postalReportingNumber

    def tearDown(self):
        pass
    
    def verifyAndPrintReport(self, report, query):
        print "  Total matching records = " + str(report.totalElements)
        print "  Total number of pages = " + str(report.totalPages)
        print "  Current page number is " + str(report.number)
        print "  Page size is " + str(report.size)
        print "  Sort by " + report.sort[0].property
        
        if report.sort[0].ascending == True:
            sort_dir = "asc"
        else:
            sort_dir = "desc"
        self.assertEqual(report.sort[0].property + "," + sort_dir, query["sort"])

        rate_benchmark = test_util.check_shipment_rate(
            self.auth_obj, self.developer)

        for next_row in report.content:
            txn = TransactionDetails(next_row)
            self.assertEqual(txn.developerRateAmount, rate_benchmark)

            txn_detail = "      timestamp: " + txn.transactionDateTime
            txn_detail += " txid: " + txn.transactionId
            txn_detail += " type: " + txn.transactionType
            txn_detail += " rate: " + str(txn.developerRateAmount)
            txn_detail += " balance: " + str(txn.shipperPostagePaymentAccountBalance)
            print txn_detail  
        
    def testTransactionReport(self):
        print "Testing get transaction report  ..."  

        query = dict()
        
        # limit query to the past 7 days 
        utc_now = datetime.datetime.utcnow()
        qdays_delta = datetime.timedelta(days=7)
        query["fromDate"] = (utc_now - qdays_delta).isoformat() + "Z"
        query["toDate"] = utc_now.isoformat() + "Z"        
        # limit to transactions originating from this test suite
        query["transactionId"] = "%%" + test_util._TEST_SUITE_TXID_PREFIX  + "%%"
        # limit to test suite merchant
        query["merchantId"] = self.shipperId
        # sort according to transaction id in descending order
        query["sort"] = "transactionId,desc"

        # paging control can be configured through these parameters           
        # query["page"] = 0 # control the page to query for 
        # query["size"] = 20 # control the page size 
        
        report = self.developer.getTransactionReport(self.auth_obj, query)
        self.verifyAndPrintReport(report, query)
        
if __name__ == "__main__":
    unittest.main()