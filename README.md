# swagger-client
## Important An **[API key](https://chompthis.com/api/)** is required for access to this API. Get yours at **[https://chompthis.com/api](https://chompthis.com/api/)**.  ### Getting Started   * **[Subscribe](https://chompthis.com/api/#pricing)** to the API.   * Scroll down and click the \"**Authorize**\" button.   * Enter your API key into the \"**value**\" input, click the \"**Authorize**\" button, then click the \"**Close**\" button.   * Scroll down to the section titled \"**default**\" and click on the API endpoint you wish to use.   * Click the \"**Try it out**\" button.   * Enter the information the endpoint requires.   * Click the \"**Execute**\" button.  ### Example    * Branded food response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/branded-food-response-object.json)**   * Ingredient response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/ingredient-response-object.json)**  ### How Do I Find My API Key?   * Your API key was sent to the email address you used to create your subscription.   * You will also find your API key in the **[Client Center](https://chompthis.com/api/manage.php)**.   * Read **[this article](https://desk.zoho.com/portal/chompthis/kb/articles/how-do-i-find-my-api-key)** for more information.  ||| | ------- | -------- | | [Knowledge Base](https://desk.zoho.com/portal/chompthis/kb/chomp) | [Pricing](https://chompthis.com/api/) | | [Attribution](https://chompthis.com/api/docs/attribution.php) | [Cost Calculator](https://chompthis.com/api/cost-calculator.php) | | [Terms & License](https://chompthis.com/api/terms.php) | [Database Search](https://chompthis.com/api/lookup.php) | | [Support](https://chompthis.com/api/ticket-new.php) | [Query Builder](https://chompthis.com/api/build.php) | | [Client Center](https://chompthis.com/api/manage.php) | | 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0-oas3
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

try:
    # Get a branded food item using a barcode
    api_response = api_instance.food_branded_barcode_php_get(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->food_branded_barcode_php_get: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | #### The ID number of a branded food item.  **Example #1: Using Chomp ID** > ```&id=15```  **Example #2: Using FDC ID** > ```&id=FDC_ID&source=USDA``` 
source = 'source_example' # str | #### Configure the endpoint to accept food IDs from various data sources. This endpoint defaults to Chomp but can accept FDC IDs.  **Example** > ```&source=Chomp```  **Tips**   * Pass in ```&source=USDA``` if you want to look up food items using a USDA FDC ID.  (optional)

try:
    # Get a branded food item using an ID number
    api_response = api_instance.food_branded_id_php_get(id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->food_branded_id_php_get: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | #### Search for branded food items using a general food name keyword. This does not have to exactly match the \"official\" name for the food.  **Example** > ```&name=Starburst``` 
limit = 56 # int | #### Set maximum number of records you want the API to return.  **Example** > ```&limit=10```  (optional)
page = 56 # int | #### This is how you paginate the search result. By default, you will see the first 10 records. You must increment the page number to access the next 10 records, and so on.  **Example** > ```&page=1```  (optional)

try:
    # Get a branded food item by name
    api_response = api_instance.food_branded_name_php_get(name, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->food_branded_name_php_get: %s\n" % e)

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
limit = 56 # int | #### Set maximum number of records you want the API to return.  **Example** > ```&limit=10```  (optional)
page = 56 # int | #### This is how you paginate the search result. By default, you will see the first 10 records. You must increment the page number to access the next 10 records, and so on.  **Example** > ```&page=1```  (optional)

try:
    # Get data for branded food items using various search parameters
    api_response = api_instance.food_branded_search_php_get(allergen=allergen, brand=brand, category=category, country=country, diet=diet, ingredient=ingredient, keyword=keyword, mineral=mineral, nutrient=nutrient, palm_oil=palm_oil, trace=trace, vitamin=vitamin, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->food_branded_search_php_get: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
find = 56 # int | Search our database for a single ingredient or a specific set of ingredients.  **Example #1: Single Ingredient** > ```&find=broccoli```  **Example #2: Set of Ingredients** > ```&find=broccoli,cauliflower,spinach&list=true```  **Important Notes**    * Set the \"list\" parameter to \"true\" before passing in a comma-separated list of ingredients.   * Comma-separated lists cannot contain more than **15 ingredients**. You must perform additional API calls if you are looking up more than 15 ingredients. 
list = true # bool | #### Setting ```&list=true``` will configure this endpoint to allow searching for ingredients using a comma-separated list. By default, this endpoint will **only** return results for the first ingredient.  **Example** > ```&list=true``` 
raw = true # bool | #### Optionally filter the search result to only include raw ingredients.  **Example** > ```&raw=true```  (optional)
limit = 56 # int | #### Set maximum number of records you want the API to return, per search term.  **Example** > ```&limit=3```  (optional)

try:
    # Get raw/generic food ingredient item(s)
    api_response = api_instance.food_ingredient_search_php_get(find, list, raw=raw, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->food_ingredient_search_php_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://chompthis.com/api/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**food_branded_barcode_php_get**](docs/DefaultApi.md#food_branded_barcode_php_get) | **GET** /food/branded/barcode.php | Get a branded food item using a barcode
*DefaultApi* | [**food_branded_id_php_get**](docs/DefaultApi.md#food_branded_id_php_get) | **GET** /food/branded/id.php | Get a branded food item using an ID number
*DefaultApi* | [**food_branded_name_php_get**](docs/DefaultApi.md#food_branded_name_php_get) | **GET** /food/branded/name.php | Get a branded food item by name
*DefaultApi* | [**food_branded_search_php_get**](docs/DefaultApi.md#food_branded_search_php_get) | **GET** /food/branded/search.php | Get data for branded food items using various search parameters
*DefaultApi* | [**food_ingredient_search_php_get**](docs/DefaultApi.md#food_ingredient_search_php_get) | **GET** /food/ingredient/search.php | Get raw/generic food ingredient item(s)

## Documentation For Models

 - [BrandedFoodObject](docs/BrandedFoodObject.md)
 - [BrandedFoodObjectCountryDetails](docs/BrandedFoodObjectCountryDetails.md)
 - [BrandedFoodObjectDietFlags](docs/BrandedFoodObjectDietFlags.md)
 - [BrandedFoodObjectDietLabels](docs/BrandedFoodObjectDietLabels.md)
 - [BrandedFoodObjectDietLabelsGlutenFree](docs/BrandedFoodObjectDietLabelsGlutenFree.md)
 - [BrandedFoodObjectDietLabelsVegan](docs/BrandedFoodObjectDietLabelsVegan.md)
 - [BrandedFoodObjectDietLabelsVegetarian](docs/BrandedFoodObjectDietLabelsVegetarian.md)
 - [BrandedFoodObjectIngredients](docs/BrandedFoodObjectIngredients.md)
 - [BrandedFoodObjectItems](docs/BrandedFoodObjectItems.md)
 - [BrandedFoodObjectNutrients](docs/BrandedFoodObjectNutrients.md)
 - [BrandedFoodObjectNutrientsChomp](docs/BrandedFoodObjectNutrientsChomp.md)
 - [BrandedFoodObjectNutrientsUsda](docs/BrandedFoodObjectNutrientsUsda.md)
 - [BrandedFoodObjectPackage](docs/BrandedFoodObjectPackage.md)
 - [BrandedFoodObjectPackagingPhotos](docs/BrandedFoodObjectPackagingPhotos.md)
 - [BrandedFoodObjectPackagingPhotosFront](docs/BrandedFoodObjectPackagingPhotosFront.md)
 - [BrandedFoodObjectPackagingPhotosIngredients](docs/BrandedFoodObjectPackagingPhotosIngredients.md)
 - [BrandedFoodObjectPackagingPhotosNutrition](docs/BrandedFoodObjectPackagingPhotosNutrition.md)
 - [BrandedFoodObjectServing](docs/BrandedFoodObjectServing.md)
 - [BrandedFoodObjectServingChomp](docs/BrandedFoodObjectServingChomp.md)
 - [BrandedFoodObjectServingUsda](docs/BrandedFoodObjectServingUsda.md)
 - [IngredientObject](docs/IngredientObject.md)
 - [IngredientObjectCalorieConversionFactor](docs/IngredientObjectCalorieConversionFactor.md)
 - [IngredientObjectComponents](docs/IngredientObjectComponents.md)
 - [IngredientObjectItems](docs/IngredientObjectItems.md)
 - [IngredientObjectNutrients](docs/IngredientObjectNutrients.md)
 - [IngredientObjectPortions](docs/IngredientObjectPortions.md)

## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: URL query string


## Author


