# CrossBorderQuotesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_currency** | **str** | The currency to return the quote in. Use three uppercase letters, per the ISO currency code (ISO 4217). For example- USD, CAD, or EUR | 
**basket_currency** | **str** | The default currency of the basket. Use three uppercase letters, per the ISO currency code (ISO 4217). For example- USD, CAD, or EUR | 
**from_address** | [**Address**](Address.md) |  | [optional] 
**to_address** | [**Address**](Address.md) |  | 
**basket_items** | [**list[CrossBorderQuotesRequestBasketItems]**](CrossBorderQuotesRequestBasketItems.md) | The items in the buyer&#39;s shopping basket. | 
**rates** | [**list[CrossBorderQuotesRequestRates]**](CrossBorderQuotesRequestRates.md) | Specifies the carrier, service, parcel, and other information. In a response, this field also contains the service charges. Importatn- In a request, the rates array can contain only one rates object. | 
**shipment_options** | [**list[CarrierFacilityResponseCarrierFacilityOptions]**](CarrierFacilityResponseCarrierFacilityOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


