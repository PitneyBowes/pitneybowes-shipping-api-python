# &#x1F534; DEPRECATED . THIS PROJECT IS NO LONGER MAINTAINED
# Pitney Bowes Shipping Client Library for Python
[![PyPI version](https://badge.fury.io/py/pbshipping.svg)](https://badge.fury.io/py/pbshipping)

The Pitney Bowes Shipping Services APIs provide easy access to United States 
Postage Service shipping and tracking services that can be easily integrated 
into any web application such as online shopping carts, e-commerce sites or 
multi-carrier applications. 

This package provides a wrapper layer allowing easy access to the Pitney Bowes 
shipping REST APIs in the Python programming language.  

You would need a Pitney Bowes developer account for testing and using the API
and the client library.

For more informaton please visit the 
[Pitney Bowes developer portal](http://developer.pitneybowes.com).

## Installation

You can either install from the source available from Github repository (https://github.com/PitneyBowes/pitneybowes-shipping-api-python) or
the [Python Package Index (PyPI)](https://pypi.python.org/pypi).

### Installing from the source:

```
python setup.py install
```

### Installing from PyPI

```
pip install pbshipping
``` 

## Registration

Make sure you have signed up a developer account on the 
[Pitney Bowes developer portal](http://developer.pitneybowes.com).

Once you have successfully registered for a developer account, sign in and
you can access your API test key (`API key` and `API secret`) from the *Dashboard*
page. 

You can also access your `Developer ID` (e.g.: 12345678) from the *My Account* 
page.

By default, your developer account is configured to work with individual 
merchant account payment model. In this caes, each merchant signs up for 
a Pitney Bowes shipment account directly and their funds are directly 
managed by Pitney Bowes. 

For testing purpose, you can create a merchant account 
at https://developer.pbshippingmerchant.pitneybowes.com/home?developerID={DeveloperID}.
Make sure you replace the placeholder in the URL with your own developer ID.

You will use the `email address` for registering the merchant account for
identifying the corresponding mercchant in the shipping API call. 

## Understanding Configuration

The client library provides a Configuration class (*__init.py*) for 
managing configuraton for environment using the Shipping APIs. The values 
for each parameter can be readily accessed and modified programmatically:

```
class Configuration: 
    params = {
        "sandbox": "https://api-sandbox.pitneybowes.com",
        "production": "https://api.pitneybowes.com",
        "is_production": False,
        "default_api_version": "/v1",
        "override_api_version": {
            "post/developers/.../merchants/registration": "/v2",
            "get/ledger/developers/.../transactions/reports": "/v2"
        }
    }
    . . . . . 
```
* *sandbox* and *production* refer to the URL pointing at the testing (sandbox)
and production server supporting the endpoints;
* *is_production* controls if the application should run in sandbox or 
production mode;
* *default_api_version* defines the default API version to be used in general 
except for cases where explict overrides are specified;
* *override_api_version* is a set (Python dictionary) of API version 
overrides for specific API calls; each entry defines the particular version 
to be used for the corresponding API.

#### Choosing API version

You may need to use different version number for diferent Shipping APIs. 
This can be accomplished by customizing the *defaul_api_version* and 
*override_api_version* entries in the *Configuration.params* structure. 

To specify the version number of a particular call type:
* Identify the *signature* for the API call; the signature mimics the relative
path of the API and can be found in the comment headers in *shipping_resource.py*.
* Add an entry to *override_api_version* in the format 
*<api signature>: <verson string>* 


## Running the Tutorials

Two examples are provided as tutorials to demonstrate the shipping services 
and client library features:

* *tutorial_rest.py* demonstrates a simple shipping workflow using the 
Pitney Bowes Shipping REST APIs directly.
* *tutorial_client_library.py* demonstrates how to use the different class and
methods available through the client library to consume the shipping services.

```
python tutorial_rest.py
python tutorial_client_library.py
```

To run either example, you would need to set your authentication (key and secret), 
developer (ID), and merchant (email) credentials either through environment 
variables or command line arguments.

### Setting through Environment Variables

The following four varaibles should be set:
* PBSHIPPING_KEY: your assigned API key
* PBSHIPPING_SECRET: your assigned API secret
* PBSHIPPING_DEVID: your Developer ID
* PBSHIPPING_MERCHANT: email address for the regsitered merchant account

```
export PBSHIPPING_KEY=<api key>
export PBSHIPPING_SECRET=<api secret>
export PBSHIPPING_DEVID=<developer id>
export PBSHIPPING_MERCHANT=<merchant email address>
```

### Setting through Command Line Arguments

Use the command line long options *--key*, *--secret*, *--devid*, and *--merchant*:

```
python tutorial_client_library.py --key=<your key> --secret=<your secret> 
                                  --devid==<developer id> 
                                  --merchant=<merchant email>
```

## Running Test 

The test suite can be found under the *pbshipping/test* and can be run 
through the *setup.py* script as follows:

```
python setup.py test 
```

Unlike the tutorials, you have to set the authentication, developer, and 
merchant settings through environment variables to run the test.

## Documentation

The Pitney Bowes Shipping Services API (REST) documentation can be found at the 
[Pitney Bowes developer portal](http://developer.pitneybowes.com).

Developers are also encouraged to use the tutorial example and source code 
comment blocks (shipping_resource.py) for information on the wrapper layer 
interface and mapping to the underlying REST shipping APIs. 

## Support 

For support issues please contact support at ShippingAPISupport@pb.com


