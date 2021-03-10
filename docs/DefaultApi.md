# swagger_client.DefaultApi

All URIs are relative to *https://chompthis.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**food_branded_barcode_php_get**](DefaultApi.md#food_branded_barcode_php_get) | **GET** /food/branded/barcode.php | Get a branded food item using a barcode
[**food_branded_name_php_get**](DefaultApi.md#food_branded_name_php_get) | **GET** /food/branded/name.php | Get a branded food item by name
[**food_branded_search_php_get**](DefaultApi.md#food_branded_search_php_get) | **GET** /food/branded/search.php | Get data for branded food items using various search parameters
[**food_ingredient_search_php_get**](DefaultApi.md#food_ingredient_search_php_get) | **GET** /food/ingredient/search.php | Get raw/generic food ingredient item(s)
[**recipe_id_php_get**](DefaultApi.md#recipe_id_php_get) | **GET** /recipe/id.php | Get a recipe by ID
[**recipe_ingredient_php_get**](DefaultApi.md#recipe_ingredient_php_get) | **GET** /recipe/ingredient.php | Get recipes using a list of ingredients
[**recipe_random_php_get**](DefaultApi.md#recipe_random_php_get) | **GET** /recipe/random.php | Get random popular recipes
[**recipe_search_php_get**](DefaultApi.md#recipe_search_php_get) | **GET** /recipe/search.php | Get recipes using a title and optional filters

# **food_branded_barcode_php_get**
> BrandedFoodObject food_branded_barcode_php_get(code, user_id=user_id)

Get a branded food item using a barcode

## Get data for a branded food using the food's UPC/EAN barcode.  **You must have a Food API key to use this endpoint.** Get a [Food API key](https://chompthis.com/api/).  **Example**  > ```https://chompthis.com/api/v2/food/branded/barcode.php?api_key=API_KEY&code=CODE```  **Tips**   * Read our **[Knowledge Base article](https://desk.zoho.com/portal/chompthis/kb/articles/im-having-trouble-getting-matches-for-barcodes-what-can-id-do)** for helpful tips and tricks.   * Perform a [check-digit](https://en.wikipedia.org/wiki/Check_digit#UPC) on the barcode you are using.   * Use a barcode from our website [ChompThis.com](https://chompthis.com/?r=api). Search for a food and use the barcode shown in the search results.   * It is possible that our database contains the food you're looking for, but does not have the same barcode you are using. This can happen if a manufacturer introduces a variation of the same food, or the barcode you got was from a 2 oz bag of chips when our database has the food packaged in a 4 oz bag.   * [Contact us](https://chompthis.com/contact.php?api=y) if you are having trouble. 

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
code = 'code_example' # str | #### UPC/EAN barcode  **Example** > ```&code=0842234000988``` 
user_id = 'user_id_example' # str | #### **Only required for Premium subscribers.** The unique identifier assigned to each user on your platform. This can be any string of letters or numbers and doesn't have to relate to your own database. [Learn more](https://desk.zoho.com/portal/chompthis/en/kb/articles/monthly-active-users)  **Example** > ```&user_id=fehef8w4ha```  (optional)

try:
    # Get a branded food item using a barcode
    api_response = api_instance.food_branded_barcode_php_get(code, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->food_branded_barcode_php_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| #### UPC/EAN barcode  **Example** &gt; &#x60;&#x60;&#x60;&amp;code&#x3D;0842234000988&#x60;&#x60;&#x60;  | 
 **user_id** | **str**| #### **Only required for Premium subscribers.** The unique identifier assigned to each user on your platform. This can be any string of letters or numbers and doesn&#x27;t have to relate to your own database. [Learn more](https://desk.zoho.com/portal/chompthis/en/kb/articles/monthly-active-users)  **Example** &gt; &#x60;&#x60;&#x60;&amp;user_id&#x3D;fehef8w4ha&#x60;&#x60;&#x60;  | [optional] 

### Return type

[**BrandedFoodObject**](BrandedFoodObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **food_branded_name_php_get**
> BrandedFoodObject food_branded_name_php_get(name, limit=limit, page=page, user_id=user_id)

Get a branded food item by name

## Search for branded food items by name.  **You must have a Food API key to use this endpoint.** Get a [Food API key](https://chompthis.com/api/).  **Example** > ```https://chompthis.com/api/v2/food/branded/name.php?api_key=API_KEY&name=NAME```  **Tips**   * Get started by using our **[food lookup tool](https://chompthis.com/api/lookup.php)**.  > This API endpoint is only available to Standard and Premium API subscribers. Please consider upgrading your subscription if you are subscribed to the Limited plan. **[Read this](https://desk.zoho.com/portal/chompthis/kb/articles/can-i-upgrade-downgrade-my-subscription)** if you aren't sure how to upgrade your subscription. 

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
name = 'name_example' # str | #### Search for branded food items using a general food name keyword. This does not have to exactly match the \"official\" name for the food.  **Example** > ```&name=Starburst``` 
limit = 56 # int | #### Set maximum number of records you want the API to return. The default value is \"**10**.\"  **Example** > ```&limit=10```  (optional)
page = 56 # int | #### This is how you paginate the search result. By default, you will see the first 10 records. You must increment the page number to access the next 10 records, and so on. The default value is \"**1**.\"  **Example** > ```&page=1```  (optional)
user_id = 'user_id_example' # str | #### **Only required for Premium subscribers.** The unique identifier assigned to each user on your platform. This can be any string of letters or numbers and doesn't have to relate to your own database. [Learn more](https://desk.zoho.com/portal/chompthis/en/kb/articles/monthly-active-users)  **Example** > ```&user_id=fehef8w4ha```  (optional)

try:
    # Get a branded food item by name
    api_response = api_instance.food_branded_name_php_get(name, limit=limit, page=page, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->food_branded_name_php_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| #### Search for branded food items using a general food name keyword. This does not have to exactly match the \&quot;official\&quot; name for the food.  **Example** &gt; &#x60;&#x60;&#x60;&amp;name&#x3D;Starburst&#x60;&#x60;&#x60;  | 
 **limit** | **int**| #### Set maximum number of records you want the API to return. The default value is \&quot;**10**.\&quot;  **Example** &gt; &#x60;&#x60;&#x60;&amp;limit&#x3D;10&#x60;&#x60;&#x60;  | [optional] 
 **page** | **int**| #### This is how you paginate the search result. By default, you will see the first 10 records. You must increment the page number to access the next 10 records, and so on. The default value is \&quot;**1**.\&quot;  **Example** &gt; &#x60;&#x60;&#x60;&amp;page&#x3D;1&#x60;&#x60;&#x60;  | [optional] 
 **user_id** | **str**| #### **Only required for Premium subscribers.** The unique identifier assigned to each user on your platform. This can be any string of letters or numbers and doesn&#x27;t have to relate to your own database. [Learn more](https://desk.zoho.com/portal/chompthis/en/kb/articles/monthly-active-users)  **Example** &gt; &#x60;&#x60;&#x60;&amp;user_id&#x3D;fehef8w4ha&#x60;&#x60;&#x60;  | [optional] 

### Return type

[**BrandedFoodObject**](BrandedFoodObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **food_branded_search_php_get**
> BrandedFoodObject food_branded_search_php_get(allergen=allergen, brand=brand, category=category, country=country, diet=diet, ingredient=ingredient, keyword=keyword, mineral=mineral, nutrient=nutrient, palm_oil=palm_oil, trace=trace, vitamin=vitamin, limit=limit, page=page, user_id=user_id)

Get data for branded food items using various search parameters

## Search for branded food items using various parameters.  **You must have a Food API key to use this endpoint.** Get a [Food API key](https://chompthis.com/api/).  **Example** > ```https://chompthis.com/api/v2/food/branded/search.php?api_key=API_KEY&brand=BRAND&country=COUNTRY&page=1```  **Tips**    * Get started by using the **[Query Builder](https://chompthis.com/api/build.php)**.  > This API endpoint is only available to Standard and Premium API subscribers. Please consider upgrading your subscription if you are subscribed to the Limited plan. **[Read this](https://desk.zoho.com/portal/chompthis/kb/articles/can-i-upgrade-downgrade-my-subscription)** if you aren't sure how to upgrade your subscription. 

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
allergen = 'allergen_example' # str | #### Filter the search to only include branded foods that contain a specific allergen.  **Example** > ```&allergen=Peanuts```  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter.  (optional)
brand = 'brand_example' # str | #### Filter the search to only include branded foods that are owned by a specific brand.  **Example** > ```&brand=Starbucks```  (optional)
category = 'category_example' # str | #### Filter the search to only include branded foods from a specific category.  **Example** > ```&category=Plant Based Foods```  (optional)
country = 'country_example' # str | #### Filter the search to only include branded foods that are sold in a specific country.  **Example** > ```&country=United States```  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter.  (optional)
diet = 'diet_example' # str | #### Filter the search to only include branded foods that are considered compatible with a specific diet.  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter.  (optional)
ingredient = 'ingredient_example' # str | #### Filter the search to only include branded foods that contain a specific ingredient.  **Example** > ```&ingredient=Salt```  (optional)
keyword = 'keyword_example' # str | #### Filter the search to only include branded foods that are associated with a specific keyword.  **Example** > ```&keyword=Organic```  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter.  (optional)
mineral = 'mineral_example' # str | #### Filter the search to only include branded foods that contain a specific mineral.  **Example** > ```&mineral=Potassium```  (optional)
nutrient = 'nutrient_example' # str | #### Filter the search to only include branded foods that contain a specific nutrient.  **Example** > ```&nutrient=Caffeine```  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter.  (optional)
palm_oil = 'palm_oil_example' # str | #### Filter the search to only include branded foods that contain a specific ingredient made using palm oil.  **Example** > ```&palm_oil=E160a Beta Carotene```  (optional)
trace = 'trace_example' # str | ### Filter the search to only include branded foods that contain a specific trace ingredient.  **Example** > ```&trace=Tree Nuts```  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter.  (optional)
vitamin = 'vitamin_example' # str | #### Filter the search to only include branded foods that contain a specific vitamin.  **Example** > ```&vitamin=Biotin```  (optional)
limit = 56 # int | #### Set maximum number of records you want the API to return. The default value is \"**10**.\"  **Example** > ```&limit=10```  (optional)
page = 56 # int | #### This is how you paginate the search result. By default, you will see the first 10 records. You must increment the page number to access the next 10 records, and so on. The default value is \"**1**.\"  **Example** > ```&page=1```  (optional)
user_id = 'user_id_example' # str | #### **Only required for Premium subscribers.** The unique identifier assigned to each user on your platform. This can be any string of letters or numbers and doesn't have to relate to your own database. [Learn more](https://desk.zoho.com/portal/chompthis/en/kb/articles/monthly-active-users)  **Example** > ```&user_id=fehef8w4ha```  (optional)

try:
    # Get data for branded food items using various search parameters
    api_response = api_instance.food_branded_search_php_get(allergen=allergen, brand=brand, category=category, country=country, diet=diet, ingredient=ingredient, keyword=keyword, mineral=mineral, nutrient=nutrient, palm_oil=palm_oil, trace=trace, vitamin=vitamin, limit=limit, page=page, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->food_branded_search_php_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allergen** | **str**| #### Filter the search to only include branded foods that contain a specific allergen.  **Example** &gt; &#x60;&#x60;&#x60;&amp;allergen&#x3D;Peanuts&#x60;&#x60;&#x60;  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter.  | [optional] 
 **brand** | **str**| #### Filter the search to only include branded foods that are owned by a specific brand.  **Example** &gt; &#x60;&#x60;&#x60;&amp;brand&#x3D;Starbucks&#x60;&#x60;&#x60;  | [optional] 
 **category** | **str**| #### Filter the search to only include branded foods from a specific category.  **Example** &gt; &#x60;&#x60;&#x60;&amp;category&#x3D;Plant Based Foods&#x60;&#x60;&#x60;  | [optional] 
 **country** | **str**| #### Filter the search to only include branded foods that are sold in a specific country.  **Example** &gt; &#x60;&#x60;&#x60;&amp;country&#x3D;United States&#x60;&#x60;&#x60;  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter.  | [optional] 
 **diet** | **str**| #### Filter the search to only include branded foods that are considered compatible with a specific diet.  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter.  | [optional] 
 **ingredient** | **str**| #### Filter the search to only include branded foods that contain a specific ingredient.  **Example** &gt; &#x60;&#x60;&#x60;&amp;ingredient&#x3D;Salt&#x60;&#x60;&#x60;  | [optional] 
 **keyword** | **str**| #### Filter the search to only include branded foods that are associated with a specific keyword.  **Example** &gt; &#x60;&#x60;&#x60;&amp;keyword&#x3D;Organic&#x60;&#x60;&#x60;  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter.  | [optional] 
 **mineral** | **str**| #### Filter the search to only include branded foods that contain a specific mineral.  **Example** &gt; &#x60;&#x60;&#x60;&amp;mineral&#x3D;Potassium&#x60;&#x60;&#x60;  | [optional] 
 **nutrient** | **str**| #### Filter the search to only include branded foods that contain a specific nutrient.  **Example** &gt; &#x60;&#x60;&#x60;&amp;nutrient&#x3D;Caffeine&#x60;&#x60;&#x60;  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter.  | [optional] 
 **palm_oil** | **str**| #### Filter the search to only include branded foods that contain a specific ingredient made using palm oil.  **Example** &gt; &#x60;&#x60;&#x60;&amp;palm_oil&#x3D;E160a Beta Carotene&#x60;&#x60;&#x60;  | [optional] 
 **trace** | **str**| ### Filter the search to only include branded foods that contain a specific trace ingredient.  **Example** &gt; &#x60;&#x60;&#x60;&amp;trace&#x3D;Tree Nuts&#x60;&#x60;&#x60;  **Important Note**: This parameter cannot be used alone. It must be paired with at least 1 additional parameter.  | [optional] 
 **vitamin** | **str**| #### Filter the search to only include branded foods that contain a specific vitamin.  **Example** &gt; &#x60;&#x60;&#x60;&amp;vitamin&#x3D;Biotin&#x60;&#x60;&#x60;  | [optional] 
 **limit** | **int**| #### Set maximum number of records you want the API to return. The default value is \&quot;**10**.\&quot;  **Example** &gt; &#x60;&#x60;&#x60;&amp;limit&#x3D;10&#x60;&#x60;&#x60;  | [optional] 
 **page** | **int**| #### This is how you paginate the search result. By default, you will see the first 10 records. You must increment the page number to access the next 10 records, and so on. The default value is \&quot;**1**.\&quot;  **Example** &gt; &#x60;&#x60;&#x60;&amp;page&#x3D;1&#x60;&#x60;&#x60;  | [optional] 
 **user_id** | **str**| #### **Only required for Premium subscribers.** The unique identifier assigned to each user on your platform. This can be any string of letters or numbers and doesn&#x27;t have to relate to your own database. [Learn more](https://desk.zoho.com/portal/chompthis/en/kb/articles/monthly-active-users)  **Example** &gt; &#x60;&#x60;&#x60;&amp;user_id&#x3D;fehef8w4ha&#x60;&#x60;&#x60;  | [optional] 

### Return type

[**BrandedFoodObject**](BrandedFoodObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **food_ingredient_search_php_get**
> IngredientObject food_ingredient_search_php_get(find, limit=limit, user_id=user_id)

Get raw/generic food ingredient item(s)

## Get data for a specific ingredient or a specific set of ingredients.  **You must have a Food API key to use this endpoint.** Get a [Food API key](https://chompthis.com/api/).  **Example #1: Single Ingredient** > ```https://chompthis.com/api/v2/food/ingredient/search.php?api_key=API_KEY&find=raw broccoli```  **Example #2: Set of Ingredients** > ```https://chompthis.com/api/v2/food/ingredient/search.php?api_key=API_KEY&find=raw broccoli,mashed potatoes,chicken drumstick```  **Tips**   * Expose ingredient endpoints by using our **[food lookup tool](https://chompthis.com/api/lookup.php)**.  > This API endpoint is only available to Standard and Premium API subscribers. Please consider upgrading your subscription if you are subscribed to the Limited plan. **[Read this](https://desk.zoho.com/portal/chompthis/kb/articles/can-i-upgrade-downgrade-my-subscription)** if you aren't sure how to upgrade your subscription. 

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
find = 'find_example' # str | Search our database for a single ingredient or a specific set of ingredients.  **Example #1: Single Ingredient** > ```&find=raw broccoli```  **Example #2: Set of Ingredients** > ```&find=raw broccoli,buttermilk waffle,mashed potatoes```  **Important Notes**    * Comma-separated lists cannot contain more than **10 ingredients**. You must perform additional API calls if you are looking up more than 10 ingredients. 
limit = 56 # int | #### Set maximum number of records you want the API to return, per search term. The default value is \"**1**.\"  **Example** > ```&limit=3```  (optional)
user_id = 'user_id_example' # str | #### **Only required for Premium subscribers.** The unique identifier assigned to each user on your platform. This can be any string of letters or numbers and doesn't have to relate to your own database. [Learn more](https://desk.zoho.com/portal/chompthis/en/kb/articles/monthly-active-users)  **Example** > ```&user_id=fehef8w4ha```  (optional)

try:
    # Get raw/generic food ingredient item(s)
    api_response = api_instance.food_ingredient_search_php_get(find, limit=limit, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->food_ingredient_search_php_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **find** | **str**| Search our database for a single ingredient or a specific set of ingredients.  **Example #1: Single Ingredient** &gt; &#x60;&#x60;&#x60;&amp;find&#x3D;raw broccoli&#x60;&#x60;&#x60;  **Example #2: Set of Ingredients** &gt; &#x60;&#x60;&#x60;&amp;find&#x3D;raw broccoli,buttermilk waffle,mashed potatoes&#x60;&#x60;&#x60;  **Important Notes**    * Comma-separated lists cannot contain more than **10 ingredients**. You must perform additional API calls if you are looking up more than 10 ingredients.  | 
 **limit** | **int**| #### Set maximum number of records you want the API to return, per search term. The default value is \&quot;**1**.\&quot;  **Example** &gt; &#x60;&#x60;&#x60;&amp;limit&#x3D;3&#x60;&#x60;&#x60;  | [optional] 
 **user_id** | **str**| #### **Only required for Premium subscribers.** The unique identifier assigned to each user on your platform. This can be any string of letters or numbers and doesn&#x27;t have to relate to your own database. [Learn more](https://desk.zoho.com/portal/chompthis/en/kb/articles/monthly-active-users)  **Example** &gt; &#x60;&#x60;&#x60;&amp;user_id&#x3D;fehef8w4ha&#x60;&#x60;&#x60;  | [optional] 

### Return type

[**IngredientObject**](IngredientObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recipe_id_php_get**
> RecipeObject recipe_id_php_get(id, user_id=user_id)

Get a recipe by ID

## Get a specific recipe using an ID.  **You must have a Recipe API key to use this endpoint.** Get a [Recipe API key](https://chompthis.com/api/recipes/).  **Example** > ```https://chompthis.com/api/v2/recipe/id.php?api_key=API_KEY&id=RECIPE_ID``` 

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
id = 'id_example' # str | #### A recipe ID. Recipe IDs are exposed in the /recipe/search and /recipe/ingredient endpoints.  **Example** > ```&list=tdm_1143_0459d0028fcf8990724785b9e6775037``` 
user_id = 'user_id_example' # str | #### **Only required for Premium subscribers.** The unique identifier assigned to each user on your platform. This can be any string of letters or numbers and doesn't have to relate to your own database. [Learn more](https://desk.zoho.com/portal/chompthis/en/kb/articles/monthly-active-users)  **Example** > ```&user_id=fehef8w4ha```  (optional)

try:
    # Get a recipe by ID
    api_response = api_instance.recipe_id_php_get(id, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->recipe_id_php_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| #### A recipe ID. Recipe IDs are exposed in the /recipe/search and /recipe/ingredient endpoints.  **Example** &gt; &#x60;&#x60;&#x60;&amp;list&#x3D;tdm_1143_0459d0028fcf8990724785b9e6775037&#x60;&#x60;&#x60;  | 
 **user_id** | **str**| #### **Only required for Premium subscribers.** The unique identifier assigned to each user on your platform. This can be any string of letters or numbers and doesn&#x27;t have to relate to your own database. [Learn more](https://desk.zoho.com/portal/chompthis/en/kb/articles/monthly-active-users)  **Example** &gt; &#x60;&#x60;&#x60;&amp;user_id&#x3D;fehef8w4ha&#x60;&#x60;&#x60;  | [optional] 

### Return type

[**RecipeObject**](RecipeObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recipe_ingredient_php_get**
> RecipeObject recipe_ingredient_php_get(list, limit=limit, page=page, user_id=user_id)

Get recipes using a list of ingredients

## Get recipes that include all ingredients from a list.  **You must have a Recipe API key to use this endpoint.** Get a [Recipe API key](https://chompthis.com/api/recipes/).  **Example #1** > ```https://chompthis.com/api/v2/recipe/ingredient.php?api_key=API_KEY&list=INGREDIENT```  **Example #2** > ```https://chompthis.com/api/v2/recipe/ingredient.php?api_key=API_KEY&list=INGREDIENT,INGREDIENT,INGREDIENT``` 

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
list = 'list_example' # str | #### A single ingredient, or a comma-separated list of up to 3 ingredients. Recipes with each of these ingredients will be returned. **You can pass in up to 3 ingredients at a time.**  **Example** > ```&list=cheese,tomato,milk``` 
limit = 56 # int | #### Set maximum number of records you want the API to return. The default value is \"**3**.\"  **Example** > ```&limit=3```  (optional)
page = 56 # int | #### This is how you paginate the search result. By default, you will see the first 3 records. You must increment the page number to access the next 3 records, and so on. The default value is \"**1**.\"  **Example** > ```&page=1```  (optional)
user_id = 'user_id_example' # str | #### **Only required for Premium subscribers.** The unique identifier assigned to each user on your platform. This can be any string of letters or numbers and doesn't have to relate to your own database. [Learn more](https://desk.zoho.com/portal/chompthis/en/kb/articles/monthly-active-users)  **Example** > ```&user_id=fehef8w4ha```  (optional)

try:
    # Get recipes using a list of ingredients
    api_response = api_instance.recipe_ingredient_php_get(list, limit=limit, page=page, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->recipe_ingredient_php_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| #### A single ingredient, or a comma-separated list of up to 3 ingredients. Recipes with each of these ingredients will be returned. **You can pass in up to 3 ingredients at a time.**  **Example** &gt; &#x60;&#x60;&#x60;&amp;list&#x3D;cheese,tomato,milk&#x60;&#x60;&#x60;  | 
 **limit** | **int**| #### Set maximum number of records you want the API to return. The default value is \&quot;**3**.\&quot;  **Example** &gt; &#x60;&#x60;&#x60;&amp;limit&#x3D;3&#x60;&#x60;&#x60;  | [optional] 
 **page** | **int**| #### This is how you paginate the search result. By default, you will see the first 3 records. You must increment the page number to access the next 3 records, and so on. The default value is \&quot;**1**.\&quot;  **Example** &gt; &#x60;&#x60;&#x60;&amp;page&#x3D;1&#x60;&#x60;&#x60;  | [optional] 
 **user_id** | **str**| #### **Only required for Premium subscribers.** The unique identifier assigned to each user on your platform. This can be any string of letters or numbers and doesn&#x27;t have to relate to your own database. [Learn more](https://desk.zoho.com/portal/chompthis/en/kb/articles/monthly-active-users)  **Example** &gt; &#x60;&#x60;&#x60;&amp;user_id&#x3D;fehef8w4ha&#x60;&#x60;&#x60;  | [optional] 

### Return type

[**RecipeObject**](RecipeObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recipe_random_php_get**
> RecipeObject recipe_random_php_get(limit=limit, user_id=user_id)

Get random popular recipes

## Get random recipes that have instructions and nutrients  **You must have a Recipe API key to use this endpoint.** Get a [Recipe API key](https://chompthis.com/api/recipes/).  **Example** > ```https://chompthis.com/api/v2/recipe/random.php?api_key=API_KEY``` 

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
limit = 56 # int | #### Set maximum number of records you want the API to return. The default value is \"**5**.\"  **Example** > ```&limit=5```  (optional)
user_id = 'user_id_example' # str | #### **Only required for Premium subscribers.** The unique identifier assigned to each user on your platform. This can be any string of letters or numbers and doesn't have to relate to your own database. [Learn more](https://desk.zoho.com/portal/chompthis/en/kb/articles/monthly-active-users)  **Example** > ```&user_id=fehef8w4ha```  (optional)

try:
    # Get random popular recipes
    api_response = api_instance.recipe_random_php_get(limit=limit, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->recipe_random_php_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| #### Set maximum number of records you want the API to return. The default value is \&quot;**5**.\&quot;  **Example** &gt; &#x60;&#x60;&#x60;&amp;limit&#x3D;5&#x60;&#x60;&#x60;  | [optional] 
 **user_id** | **str**| #### **Only required for Premium subscribers.** The unique identifier assigned to each user on your platform. This can be any string of letters or numbers and doesn&#x27;t have to relate to your own database. [Learn more](https://desk.zoho.com/portal/chompthis/en/kb/articles/monthly-active-users)  **Example** &gt; &#x60;&#x60;&#x60;&amp;user_id&#x3D;fehef8w4ha&#x60;&#x60;&#x60;  | [optional] 

### Return type

[**RecipeObject**](RecipeObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recipe_search_php_get**
> RecipeObject recipe_search_php_get(title, excluded_cuisine=excluded_cuisine, included_cuisine=included_cuisine, excluded_ingredient=excluded_ingredient, included_ingredient=included_ingredient, nutrients_required=nutrients_required, limit=limit, page=page, user_id=user_id)

Get recipes using a title and optional filters

## Get recipes using a title and optional filters.  **You must have a Recipe API key to use this endpoint.** Get a [Recipe API key](https://chompthis.com/api/recipes/).  **Example**  > ```https://chompthis.com/api/v2/recipe/search.php?api_key=API_KEY&title=TITLE``` 

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
title = 'title_example' # str | #### A recipe title  **Example** > ```&title=Banana Bread``` 
excluded_cuisine = 'excluded_cuisine_example' # str | #### A specific cuisine you want excluded from results  **Example** > ```&excluded_cuisine=Italian```  (optional)
included_cuisine = 'included_cuisine_example' # str | #### A specific cuisine you want included in results  **Example** > ```&included_cuisine=Chinese```  (optional)
excluded_ingredient = 'excluded_ingredient_example' # str | #### Recipes with this ingredient will be excluded from results  **Example** > ```&excluded_ingredient=egg```  (optional)
included_ingredient = 'included_ingredient_example' # str | #### Only recipes with this ingredient will be returned  **Example** > ```&included_ingredient=apple```  (optional)
nutrients_required = 56 # int | #### Optionally require all recipes to include nutrition info. Recipes with, or without, nutrition info are returned by default.  **Example** > ```&nutrients_required=1```  (optional)
limit = 56 # int | #### Set maximum number of records you want the API to return. The default value is \"**5**.\"  **Example** > ```&limit=3```  (optional)
page = 56 # int | #### This is how you paginate the search result. By default, you will see the first 5 records. You must increment the page number to access the next 5 records, and so on. The default value is \"**1**.\"  **Example** > ```&page=1```  (optional)
user_id = 'user_id_example' # str | #### **Only required for Premium subscribers.** The unique identifier assigned to each user on your platform. This can be any string of letters or numbers and doesn't have to relate to your own database. [Learn more](https://desk.zoho.com/portal/chompthis/en/kb/articles/monthly-active-users)  **Example** > ```&user_id=fehef8w4ha```  (optional)

try:
    # Get recipes using a title and optional filters
    api_response = api_instance.recipe_search_php_get(title, excluded_cuisine=excluded_cuisine, included_cuisine=included_cuisine, excluded_ingredient=excluded_ingredient, included_ingredient=included_ingredient, nutrients_required=nutrients_required, limit=limit, page=page, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->recipe_search_php_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| #### A recipe title  **Example** &gt; &#x60;&#x60;&#x60;&amp;title&#x3D;Banana Bread&#x60;&#x60;&#x60;  | 
 **excluded_cuisine** | **str**| #### A specific cuisine you want excluded from results  **Example** &gt; &#x60;&#x60;&#x60;&amp;excluded_cuisine&#x3D;Italian&#x60;&#x60;&#x60;  | [optional] 
 **included_cuisine** | **str**| #### A specific cuisine you want included in results  **Example** &gt; &#x60;&#x60;&#x60;&amp;included_cuisine&#x3D;Chinese&#x60;&#x60;&#x60;  | [optional] 
 **excluded_ingredient** | **str**| #### Recipes with this ingredient will be excluded from results  **Example** &gt; &#x60;&#x60;&#x60;&amp;excluded_ingredient&#x3D;egg&#x60;&#x60;&#x60;  | [optional] 
 **included_ingredient** | **str**| #### Only recipes with this ingredient will be returned  **Example** &gt; &#x60;&#x60;&#x60;&amp;included_ingredient&#x3D;apple&#x60;&#x60;&#x60;  | [optional] 
 **nutrients_required** | **int**| #### Optionally require all recipes to include nutrition info. Recipes with, or without, nutrition info are returned by default.  **Example** &gt; &#x60;&#x60;&#x60;&amp;nutrients_required&#x3D;1&#x60;&#x60;&#x60;  | [optional] 
 **limit** | **int**| #### Set maximum number of records you want the API to return. The default value is \&quot;**5**.\&quot;  **Example** &gt; &#x60;&#x60;&#x60;&amp;limit&#x3D;3&#x60;&#x60;&#x60;  | [optional] 
 **page** | **int**| #### This is how you paginate the search result. By default, you will see the first 5 records. You must increment the page number to access the next 5 records, and so on. The default value is \&quot;**1**.\&quot;  **Example** &gt; &#x60;&#x60;&#x60;&amp;page&#x3D;1&#x60;&#x60;&#x60;  | [optional] 
 **user_id** | **str**| #### **Only required for Premium subscribers.** The unique identifier assigned to each user on your platform. This can be any string of letters or numbers and doesn&#x27;t have to relate to your own database. [Learn more](https://desk.zoho.com/portal/chompthis/en/kb/articles/monthly-active-users)  **Example** &gt; &#x60;&#x60;&#x60;&amp;user_id&#x3D;fehef8w4ha&#x60;&#x60;&#x60;  | [optional] 

### Return type

[**RecipeObject**](RecipeObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

