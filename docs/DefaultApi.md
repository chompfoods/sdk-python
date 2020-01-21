# swagger_client.DefaultApi

All URIs are relative to *https://chompthis.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**food_branded_barcode_php_get**](DefaultApi.md#food_branded_barcode_php_get) | **GET** /food/branded/barcode.php | Get a branded food item using a barcode
[**food_branded_id_php_get**](DefaultApi.md#food_branded_id_php_get) | **GET** /food/branded/id.php | Get a branded food item using an ID number
[**food_branded_name_php_get**](DefaultApi.md#food_branded_name_php_get) | **GET** /food/branded/name.php | Get a branded food item by name
[**food_branded_search_php_get**](DefaultApi.md#food_branded_search_php_get) | **GET** /food/branded/search.php | Get data for branded food items using various search parameters
[**food_ingredient_search_php_get**](DefaultApi.md#food_ingredient_search_php_get) | **GET** /food/ingredient/search.php | Get raw/generic food ingredient item(s)

# **food_branded_barcode_php_get**
> BrandedFoodObject food_branded_barcode_php_get(code)

Get a branded food item using a barcode

# Get data for a branded food using the food's UPC/EAN barcode.  __Example:__ ```https://chompthis.com/api/v2/food/branded/barcode.php?api_key=API_KEY&code=CODE``` 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | UPC/EAN barcode  __Example:__ &code=0842234000988  __Tips:__    - Use our [food lookup tool](https://chompthis.com/api/lookup.php).   - Read [this article](https://desk.zoho.com/portal/chompthis/kb/articles/im-having-trouble-getting-matches-for-barcodes-what-can-id-do) for general tips and tricks. 

try:
    # Get a branded food item using a barcode
    api_response = api_instance.food_branded_barcode_php_get(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->food_branded_barcode_php_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| UPC/EAN barcode  __Example:__ &amp;code&#x3D;0842234000988  __Tips:__    - Use our [food lookup tool](https://chompthis.com/api/lookup.php).   - Read [this article](https://desk.zoho.com/portal/chompthis/kb/articles/im-having-trouble-getting-matches-for-barcodes-what-can-id-do) for general tips and tricks.  | 

### Return type

[**BrandedFoodObject**](BrandedFoodObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **food_branded_id_php_get**
> BrandedFoodObject food_branded_id_php_get(id, source=source)

Get a branded food item using an ID number

# Get data for a branded food using Chomp's internal ID number.  _Alternatively, set the \"source\" parameter to \"USDA\" and use the food's FDC ID._  __Example:__ ```https://chompthis.com/api/v2/food/branded/id.php?api_key=API_KEY&id=ID``` 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | The ID number of a branded food item.  __Example #1:__ &id=15  __Example #2:__ &id=FDC_ID&source=USDA  ___Tip:__ Get started by using our  [ood lookup tool](https://chompthis.com/api/lookup.php)._ 
source = 'source_example' # str | Configure the endpoint to accept food IDs from various data sources. This endpoint defaults to Chomp but can accept FDC IDs.  __Example:__ &source=Chomp  ___Important Note:__ Pass in &source=USDA if you want to look up food items using a USDA FDC ID._  (optional)

try:
    # Get a branded food item using an ID number
    api_response = api_instance.food_branded_id_php_get(id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->food_branded_id_php_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID number of a branded food item.  __Example #1:__ &amp;id&#x3D;15  __Example #2:__ &amp;id&#x3D;FDC_ID&amp;source&#x3D;USDA  ___Tip:__ Get started by using our  [ood lookup tool](https://chompthis.com/api/lookup.php)._  | 
 **source** | **str**| Configure the endpoint to accept food IDs from various data sources. This endpoint defaults to Chomp but can accept FDC IDs.  __Example:__ &amp;source&#x3D;Chomp  ___Important Note:__ Pass in &amp;source&#x3D;USDA if you want to look up food items using a USDA FDC ID._  | [optional] 

### Return type

[**BrandedFoodObject**](BrandedFoodObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **food_branded_name_php_get**
> BrandedFoodObject food_branded_name_php_get(name, limit=limit, page=page)

Get a branded food item by name

# Search for branded food items by name.  This API endpoint is only available to Standard and Premium API subscribers. Please consider upgrading your subscription if you are subscribed to the Limited plan. _[Read this](https://desk.zoho.com/portal/chompthis/kb/articles/can-i-upgrade-downgrade-my-subscription) if you aren't sure how to upgrade your subscription._  __Example:__ ```https://chompthis.com/api/v2/food/branded/name.php?api_key=API_KEY&name=NAME``` 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Search for branded food items using a general food name keyword. This does not have to exactly match the \"official\" name for the food.  __Example:__ &name=Starburst  ___Tip:__ Get started by using our [food lookup tool](https://chompthis.com/api/lookup.php)._ 
limit = 56 # int | Set maximum number of records you want the API to return.  __Example:__ &limit=10  (optional)
page = 56 # int | This is how you paginate the search result. By default, you will see the first 10 records. You must increment the page number to access the next 10 records, and so on.  __Example__: &page=1  (optional)

try:
    # Get a branded food item by name
    api_response = api_instance.food_branded_name_php_get(name, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->food_branded_name_php_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Search for branded food items using a general food name keyword. This does not have to exactly match the \&quot;official\&quot; name for the food.  __Example:__ &amp;name&#x3D;Starburst  ___Tip:__ Get started by using our [food lookup tool](https://chompthis.com/api/lookup.php)._  | 
 **limit** | **int**| Set maximum number of records you want the API to return.  __Example:__ &amp;limit&#x3D;10  | [optional] 
 **page** | **int**| This is how you paginate the search result. By default, you will see the first 10 records. You must increment the page number to access the next 10 records, and so on.  __Example__: &amp;page&#x3D;1  | [optional] 

### Return type

[**BrandedFoodObject**](BrandedFoodObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **food_branded_search_php_get**
> BrandedFoodObject food_branded_search_php_get(allergen=allergen, brand=brand, category=category, country=country, diet=diet, ingredient=ingredient, keyword=keyword, mineral=mineral, nutrient=nutrient, palm_oil=palm_oil, trace=trace, vitamin=vitamin, limit=limit, page=page)

Get data for branded food items using various search parameters

# Search for branded food items using various parameters.  This API endpoint is only available to Standard and Premium API subscribers. Please consider upgrading your subscription if you are subscribed to the Limited plan. _[Read this](https://desk.zoho.com/portal/chompthis/kb/articles/can-i-upgrade-downgrade-my-subscription) if you aren't sure how to upgrade your subscription._  __Example:__ ```https://chompthis.com/api/v2/food/branded/search.php?api_key=API_KEY&brand=BRAND&country=COUNTRY&page=1```  ___Tip:__ Get started by using the [Query Builder](https://chompthis.com/api/build.php)._ 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
allergen = 'allergen_example' # str | Filter the search to only include branded foods that contain a specific allergen.  __Example__: &allergen=Peanuts  ___Important Note:__ This parameter cannot be used alone. It must be paired with at least 1 additional parameter._  (optional)
brand = 'brand_example' # str | Filter the search to only include branded foods that are owned by a specific brand.  __Example__: &brand=Starbucks  (optional)
category = 'category_example' # str | Filter the search to only include branded foods from a specific category.  __Example__: &category=Plant Based Foods  (optional)
country = 'country_example' # str | Filter the search to only include branded foods that are sold in a specific country.  __Example__: &country=United States  ___Important Note:__ This parameter cannot be used alone. It must be paired with at least 1 additional parameter._  (optional)
diet = 'diet_example' # str | Filter the search to only include branded foods that are considered compatible with a specific diet.  ___Important Note:__ This parameter cannot be used alone. It must be paired with at least 1 additional parameter._  (optional)
ingredient = 'ingredient_example' # str | Filter the search to only include branded foods that contain a specific ingredient.  __Example__: &ingredient=Salt  (optional)
keyword = 'keyword_example' # str | Filter the search to only include branded foods that are associated with a specific keyword.  __Example__: &keyword=Organic  ___Important Note:__ This parameter cannot be used alone. It must be paired with at least 1 additional parameter._  (optional)
mineral = 'mineral_example' # str | Filter the search to only include branded foods that contain a specific mineral.  __Example__: &mineral=Potassium  (optional)
nutrient = 'nutrient_example' # str | Filter the search to only include branded foods that contain a specific nutrient.  __Example__: &nutrient=Caffeine  ___Important Note:__ This parameter cannot be used alone. It must be paired with at least 1 additional parameter._  (optional)
palm_oil = 'palm_oil_example' # str | Filter the search to only include branded foods that contain a specific ingredient made using palm oil.  __Example__: &palm_oil=E160a Beta Carotene  (optional)
trace = 'trace_example' # str | Filter the search to only include branded foods that contain a specific trace ingredient.  __Example__: &trace=Tree Nuts  ___Important Note:__ This parameter cannot be used alone. It must be paired with at least 1 additional parameter._  (optional)
vitamin = 'vitamin_example' # str | Filter the search to only include branded foods that contain a specific vitamin.  __Example__: &vitamin=Biotin  (optional)
limit = 56 # int | Set maximum number of records you want the API to return.  __Example:__ &limit=10  (optional)
page = 56 # int | This is how you paginate the search result. By default, you will see the first 10 records. You must increment the page number to access the next 10 records, and so on.  __Example__: &page=1  (optional)

try:
    # Get data for branded food items using various search parameters
    api_response = api_instance.food_branded_search_php_get(allergen=allergen, brand=brand, category=category, country=country, diet=diet, ingredient=ingredient, keyword=keyword, mineral=mineral, nutrient=nutrient, palm_oil=palm_oil, trace=trace, vitamin=vitamin, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->food_branded_search_php_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allergen** | **str**| Filter the search to only include branded foods that contain a specific allergen.  __Example__: &amp;allergen&#x3D;Peanuts  ___Important Note:__ This parameter cannot be used alone. It must be paired with at least 1 additional parameter._  | [optional] 
 **brand** | **str**| Filter the search to only include branded foods that are owned by a specific brand.  __Example__: &amp;brand&#x3D;Starbucks  | [optional] 
 **category** | **str**| Filter the search to only include branded foods from a specific category.  __Example__: &amp;category&#x3D;Plant Based Foods  | [optional] 
 **country** | **str**| Filter the search to only include branded foods that are sold in a specific country.  __Example__: &amp;country&#x3D;United States  ___Important Note:__ This parameter cannot be used alone. It must be paired with at least 1 additional parameter._  | [optional] 
 **diet** | **str**| Filter the search to only include branded foods that are considered compatible with a specific diet.  ___Important Note:__ This parameter cannot be used alone. It must be paired with at least 1 additional parameter._  | [optional] 
 **ingredient** | **str**| Filter the search to only include branded foods that contain a specific ingredient.  __Example__: &amp;ingredient&#x3D;Salt  | [optional] 
 **keyword** | **str**| Filter the search to only include branded foods that are associated with a specific keyword.  __Example__: &amp;keyword&#x3D;Organic  ___Important Note:__ This parameter cannot be used alone. It must be paired with at least 1 additional parameter._  | [optional] 
 **mineral** | **str**| Filter the search to only include branded foods that contain a specific mineral.  __Example__: &amp;mineral&#x3D;Potassium  | [optional] 
 **nutrient** | **str**| Filter the search to only include branded foods that contain a specific nutrient.  __Example__: &amp;nutrient&#x3D;Caffeine  ___Important Note:__ This parameter cannot be used alone. It must be paired with at least 1 additional parameter._  | [optional] 
 **palm_oil** | **str**| Filter the search to only include branded foods that contain a specific ingredient made using palm oil.  __Example__: &amp;palm_oil&#x3D;E160a Beta Carotene  | [optional] 
 **trace** | **str**| Filter the search to only include branded foods that contain a specific trace ingredient.  __Example__: &amp;trace&#x3D;Tree Nuts  ___Important Note:__ This parameter cannot be used alone. It must be paired with at least 1 additional parameter._  | [optional] 
 **vitamin** | **str**| Filter the search to only include branded foods that contain a specific vitamin.  __Example__: &amp;vitamin&#x3D;Biotin  | [optional] 
 **limit** | **int**| Set maximum number of records you want the API to return.  __Example:__ &amp;limit&#x3D;10  | [optional] 
 **page** | **int**| This is how you paginate the search result. By default, you will see the first 10 records. You must increment the page number to access the next 10 records, and so on.  __Example__: &amp;page&#x3D;1  | [optional] 

### Return type

[**BrandedFoodObject**](BrandedFoodObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **food_ingredient_search_php_get**
> IngredientObject food_ingredient_search_php_get(find, list, raw=raw, limit=limit)

Get raw/generic food ingredient item(s)

# Get data for a specific ingredient or a specific set of ingredients.  This API endpoint is only available to Standard and Premium API subscribers. Please consider upgrading your subscription if you are subscribed to the Limited plan. _[Read this](https://desk.zoho.com/portal/chompthis/kb/articles/can-i-upgrade-downgrade-my-subscription) if you aren't sure how to upgrade your subscription._  __Example:__ ```https://chompthis.com/api/v2/ingredient/search.php?api_key=API_KEY&find=STRING/LIST&list=BOOLEAN&raw=BOOLEAN``` 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
find = 56 # int | Search our database for a single ingredient or a specific set of ingredients.  __Example #1:__ &find=broccoli  __Example #2:__ &find=broccoli,cauliflower,spinach&list=true  __Important List Notes:__    - Set the \"list\" parameter to \"true\" before passing in a comma-separated list of ingredients.   - Comma-separated lists cannot contain more than __15 ingredients__. You must perform additional API calls if you are looking up more than 15 ingredients. 
list = true # bool | Setting _&list=true_ will configure this endpoint to allow searching for ingredients using a comma-separated list. By default, this endpoint will __only__ return results for the first ingredient.  __Example:__ &list=true 
raw = true # bool | Optionally filter the search result to only include raw ingredients.  __Example:__ &raw=true  (optional)
limit = 56 # int | Set maximum number of records you want the API to return, per search term.  __Example:__ &limit=3  (optional)

try:
    # Get raw/generic food ingredient item(s)
    api_response = api_instance.food_ingredient_search_php_get(find, list, raw=raw, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->food_ingredient_search_php_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **find** | **int**| Search our database for a single ingredient or a specific set of ingredients.  __Example #1:__ &amp;find&#x3D;broccoli  __Example #2:__ &amp;find&#x3D;broccoli,cauliflower,spinach&amp;list&#x3D;true  __Important List Notes:__    - Set the \&quot;list\&quot; parameter to \&quot;true\&quot; before passing in a comma-separated list of ingredients.   - Comma-separated lists cannot contain more than __15 ingredients__. You must perform additional API calls if you are looking up more than 15 ingredients.  | 
 **list** | **bool**| Setting _&amp;list&#x3D;true_ will configure this endpoint to allow searching for ingredients using a comma-separated list. By default, this endpoint will __only__ return results for the first ingredient.  __Example:__ &amp;list&#x3D;true  | 
 **raw** | **bool**| Optionally filter the search result to only include raw ingredients.  __Example:__ &amp;raw&#x3D;true  | [optional] 
 **limit** | **int**| Set maximum number of records you want the API to return, per search term.  __Example:__ &amp;limit&#x3D;3  | [optional] 

### Return type

[**IngredientObject**](IngredientObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

