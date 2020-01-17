# swagger_client.DefaultApi

All URIs are relative to *https://chompthis.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**food_branded_barcode_php_get**](DefaultApi.md#food_branded_barcode_php_get) | **GET** /food/branded/barcode.php | Get a branded food item using a barcode
[**food_branded_id_php_get**](DefaultApi.md#food_branded_id_php_get) | **GET** /food/branded/id.php | Get a branded food item using an ID number
[**food_branded_name_php_get**](DefaultApi.md#food_branded_name_php_get) | **GET** /food/branded/name.php | Get a branded food item by name
[**food_branded_search_php_get**](DefaultApi.md#food_branded_search_php_get) | **GET** /food/branded/search.php | Get data for branded food items using various search parameters
[**ingredient_search_php_get**](DefaultApi.md#ingredient_search_php_get) | **GET** /ingredient/search.php | Get raw/generic food ingredient item(s)

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
code = 'code_example' # str | UPC/EAN barcode  __Example:__ 0842234000988  __Resources:__ [Database search](https://chompthis.com/api/lookup.php)  _Read [this article](https://desk.zoho.com/portal/chompthis/kb/articles/im-having-trouble-getting-matches-for-barcodes-what-can-id-do) for tips and tricks._ 

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
 **code** | **str**| UPC/EAN barcode  __Example:__ 0842234000988  __Resources:__ [Database search](https://chompthis.com/api/lookup.php)  _Read [this article](https://desk.zoho.com/portal/chompthis/kb/articles/im-having-trouble-getting-matches-for-barcodes-what-can-id-do) for tips and tricks._  | 

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
id = 56 # int | Chomp branded food ID.  _Set \"source=USDA\" if you wish to pass in the food's FoodData Central ID (fdc_id)._  __Example #1:__ 15  __Resources:__ [Find branded food IDs](https://chompthis.com/api/lookup.php) 
source = 'source_example' # str | Specify the data source (optional).  You must pass in \"USDA\" if you want to look up a food item using a USDA FDC ID.  __Example:__ USDA _(defaults to \"Chomp\")_  (optional)

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
 **id** | **int**| Chomp branded food ID.  _Set \&quot;source&#x3D;USDA\&quot; if you wish to pass in the food&#x27;s FoodData Central ID (fdc_id)._  __Example #1:__ 15  __Resources:__ [Find branded food IDs](https://chompthis.com/api/lookup.php)  | 
 **source** | **str**| Specify the data source (optional).  You must pass in \&quot;USDA\&quot; if you want to look up a food item using a USDA FDC ID.  __Example:__ USDA _(defaults to \&quot;Chomp\&quot;)_  | [optional] 

### Return type

[**BrandedFoodObject**](BrandedFoodObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **food_branded_name_php_get**
> BrandedFoodObject food_branded_name_php_get(name, limit=limit)

Get a branded food item by name

# Search for branded food items by name.  __Example:__ ```https://chompthis.com/api/v2/food/branded/name.php?api_key=API_KEY&name=NAME``` 

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
name = 'name_example' # str | Branded food name  __Example:__ Starburst  __Resources:__ [Find branded food names](https://chompthis.com/api/lookup.php) 
limit = 56 # int | Set maximum number of records you want the API to return.  ___Note:__ The maximum value is 10._  __Example:__ 3 _(defaults to 10)_  (optional)

try:
    # Get a branded food item by name
    api_response = api_instance.food_branded_name_php_get(name, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->food_branded_name_php_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Branded food name  __Example:__ Starburst  __Resources:__ [Find branded food names](https://chompthis.com/api/lookup.php)  | 
 **limit** | **int**| Set maximum number of records you want the API to return.  ___Note:__ The maximum value is 10._  __Example:__ 3 _(defaults to 10)_  | [optional] 

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

# Search for branded food items using various parameters.  __Example:__ ```https://chompthis.com/api/v2/food/branded/search.php?api_key=API_KEY&brand=BRAND&country=COUNTRY&page=1```  ___Tip:__ Get started by using the [Query Builder](https://chompthis.com/api/build.php)._ 

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
allergen = 'allergen_example' # str | Specify a required allergen ingredient (optional)  __Example__: Peanuts  __Resources__: [List of allergens](https://chompthis.com/api/data/allergen.php)  (optional)
brand = 'brand_example' # str | Specify a required brand (optional)  __Example__: Starbucks  __Resources__: [List of brands](https://chompthis.com/api/data/brand.php)  (optional)
category = 'category_example' # str | Specify a required category (optional)  __Example__: Pasta Dishes  __Resources__: [List of categories](https://chompthis.com/api/data/category.php)  (optional)
country = 'country_example' # str | Specify a required country (optional)  __Example__: United States  __Resources__: [List of countries](https://chompthis.com/api/data/country.php)  (optional)
diet = 'diet_example' # str | Specify a required diet (optional)  _Filters the search to only include food items that are considered compatible with the following diets: Vegan, Vegetarian, Gluten Free_  __Example__: Gluten Free  __Resources__: [List of diets](https://chompthis.com/api/data/lifestyle.php)  (optional)
ingredient = 'ingredient_example' # str | Specify a required ingredient (optional)  __Example__: Salt  __Resources__: [List of ingredients](https://chompthis.com/api/data/ingredient.php)  (optional)
keyword = 'keyword_example' # str | Specify a required keyword (optional)  __Example__: Starbucks  __Resources__: [List of brands](https://chompthis.com/api/data/brand.php)  (optional)
mineral = 'mineral_example' # str | Specify a required mineral (optional)  __Example__: Potassium  __Resources__: [List of minerals](https://chompthis.com/api/data/mineral.php)  (optional)
nutrient = 'nutrient_example' # str | Specify a required nutrition label item (optional)  __Example__: Caffeine  __Resources__: [List of nutrition label items](https://chompthis.com/api/data/nutrition.php)  (optional)
palm_oil = 'palm_oil_example' # str | Specify a required palm oil ingredient (optional)  __Example__: E160a Beta Carotene  __Resources__: [List of palm oil ingredients](https://chompthis.com/api/data/palm-oil.php)  (optional)
trace = 'trace_example' # str | Specify a required trace ingredient (optional)  __Example__: Tree Nuts  __Resources__: [List of trace ingredients](https://chompthis.com/api/data/trace.php)  (optional)
vitamin = 'vitamin_example' # str | Specify a required vitamin (optional)  __Example__: Biotin  __Resources__: [List of vitamins](https://chompthis.com/api/data/vitamin.php)  (optional)
limit = 56 # int | Set maximum number of records you want the API to return.  ___Note:__ The maximum value is 10._  __Example:__ 3 _(defaults to 10)_  (optional)
page = 56 # int | Specify the search response page number.  _Each page will contain up to 10 items._  __Example__: 1 _(default)_  (optional)

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
 **allergen** | **str**| Specify a required allergen ingredient (optional)  __Example__: Peanuts  __Resources__: [List of allergens](https://chompthis.com/api/data/allergen.php)  | [optional] 
 **brand** | **str**| Specify a required brand (optional)  __Example__: Starbucks  __Resources__: [List of brands](https://chompthis.com/api/data/brand.php)  | [optional] 
 **category** | **str**| Specify a required category (optional)  __Example__: Pasta Dishes  __Resources__: [List of categories](https://chompthis.com/api/data/category.php)  | [optional] 
 **country** | **str**| Specify a required country (optional)  __Example__: United States  __Resources__: [List of countries](https://chompthis.com/api/data/country.php)  | [optional] 
 **diet** | **str**| Specify a required diet (optional)  _Filters the search to only include food items that are considered compatible with the following diets: Vegan, Vegetarian, Gluten Free_  __Example__: Gluten Free  __Resources__: [List of diets](https://chompthis.com/api/data/lifestyle.php)  | [optional] 
 **ingredient** | **str**| Specify a required ingredient (optional)  __Example__: Salt  __Resources__: [List of ingredients](https://chompthis.com/api/data/ingredient.php)  | [optional] 
 **keyword** | **str**| Specify a required keyword (optional)  __Example__: Starbucks  __Resources__: [List of brands](https://chompthis.com/api/data/brand.php)  | [optional] 
 **mineral** | **str**| Specify a required mineral (optional)  __Example__: Potassium  __Resources__: [List of minerals](https://chompthis.com/api/data/mineral.php)  | [optional] 
 **nutrient** | **str**| Specify a required nutrition label item (optional)  __Example__: Caffeine  __Resources__: [List of nutrition label items](https://chompthis.com/api/data/nutrition.php)  | [optional] 
 **palm_oil** | **str**| Specify a required palm oil ingredient (optional)  __Example__: E160a Beta Carotene  __Resources__: [List of palm oil ingredients](https://chompthis.com/api/data/palm-oil.php)  | [optional] 
 **trace** | **str**| Specify a required trace ingredient (optional)  __Example__: Tree Nuts  __Resources__: [List of trace ingredients](https://chompthis.com/api/data/trace.php)  | [optional] 
 **vitamin** | **str**| Specify a required vitamin (optional)  __Example__: Biotin  __Resources__: [List of vitamins](https://chompthis.com/api/data/vitamin.php)  | [optional] 
 **limit** | **int**| Set maximum number of records you want the API to return.  ___Note:__ The maximum value is 10._  __Example:__ 3 _(defaults to 10)_  | [optional] 
 **page** | **int**| Specify the search response page number.  _Each page will contain up to 10 items._  __Example__: 1 _(default)_  | [optional] 

### Return type

[**BrandedFoodObject**](BrandedFoodObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ingredient_search_php_get**
> IngredientObject ingredient_search_php_get(find, list, raw=raw, limit=limit)

Get raw/generic food ingredient item(s)

# Get data for a specific ingredient or a specific set of ingredients.  __Example:__ ```https://chompthis.com/api/v2/ingredient/search.php?api_key=API_KEY&find=STRING/LIST&list=BOOLEAN&raw=BOOLEAN``` 

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
find = 56 # int | Specify the ingredient name(s).  __Example #1:__ broccoli  __Example #2:__ broccoli,cauliflower,spinach  ___Important Note:__ Set the \"is_list\" parameter to true before passing in a comma-separated list of ingredients._ 
list = true # bool | Specify if you are searching for multiple ingredients.  _Setting this to true will configure this endpoint so that it accepts a comma-separated list of ingredients._  _By default, this endpoint expects a single ingredient._  __Example:__ true _(defaults to false)_ 
raw = true # bool | Specify if you only want data for raw ingredients.  __Example:__ true _(defaults to true)_  (optional)
limit = 56 # int | Set maximum number of records you want the API to return.  ___Important Note:__ Setting this to \"1\" will return 1 record per search term._  __Example:__ 1 _(defaults to 1, max is 3)_  (optional)

try:
    # Get raw/generic food ingredient item(s)
    api_response = api_instance.ingredient_search_php_get(find, list, raw=raw, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ingredient_search_php_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **find** | **int**| Specify the ingredient name(s).  __Example #1:__ broccoli  __Example #2:__ broccoli,cauliflower,spinach  ___Important Note:__ Set the \&quot;is_list\&quot; parameter to true before passing in a comma-separated list of ingredients._  | 
 **list** | **bool**| Specify if you are searching for multiple ingredients.  _Setting this to true will configure this endpoint so that it accepts a comma-separated list of ingredients._  _By default, this endpoint expects a single ingredient._  __Example:__ true _(defaults to false)_  | 
 **raw** | **bool**| Specify if you only want data for raw ingredients.  __Example:__ true _(defaults to true)_  | [optional] 
 **limit** | **int**| Set maximum number of records you want the API to return.  ___Important Note:__ Setting this to \&quot;1\&quot; will return 1 record per search term._  __Example:__ 1 _(defaults to 1, max is 3)_  | [optional] 

### Return type

[**IngredientObject**](IngredientObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

