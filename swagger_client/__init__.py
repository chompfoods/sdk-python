# coding: utf-8

# flake8: noqa

"""
    Chomp Food Database API Documentation

    ## Important An **[API key](https://chompthis.com/api/)** is required for access to this API. Get yours at **[https://chompthis.com/api](https://chompthis.com/api/)**.  ### Getting Started   * **[Subscribe](https://chompthis.com/api/#pricing)** to the API.   * Scroll down and click the \"**Authorize**\" button.   * Enter your API key into the \"**value**\" input, click the \"**Authorize**\" button, then click the \"**Close**\" button.   * Scroll down to the section titled \"**default**\" and click on the API endpoint you wish to use.   * Click the \"**Try it out**\" button.   * Enter the information the endpoint requires.   * Click the \"**Execute**\" button.  ### Example    * Branded food response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/branded-food-response-object.json)**   * Ingredient response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/ingredient-response-object.json)**  ### How Do I Find My API Key?   * Your API key was sent to the email address you used to create your subscription.   * You will also find your API key in the **[Client Center](https://chompthis.com/api/manage.php)**.   * Read **[this article](https://desk.zoho.com/portal/chompthis/kb/articles/how-do-i-find-my-api-key)** for more information.  ||| | ------- | -------- | | [Knowledge Base](https://desk.zoho.com/portal/chompthis/kb/chomp) | [Pricing](https://chompthis.com/api/) | | [Attribution](https://chompthis.com/api/docs/attribution.php) | [Cost Calculator](https://chompthis.com/api/cost-calculator.php) | | [Terms & License](https://chompthis.com/api/terms.php) | [Database Search](https://chompthis.com/api/lookup.php) | | [Support](https://chompthis.com/api/ticket-new.php) | [Query Builder](https://chompthis.com/api/build.php) | | [Client Center](https://chompthis.com/api/manage.php) | |   # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.default_api import DefaultApi
# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.branded_food_object import BrandedFoodObject
from swagger_client.models.branded_food_object_country_details import BrandedFoodObjectCountryDetails
from swagger_client.models.branded_food_object_diet_flags import BrandedFoodObjectDietFlags
from swagger_client.models.branded_food_object_diet_labels import BrandedFoodObjectDietLabels
from swagger_client.models.branded_food_object_diet_labels_gluten_free import BrandedFoodObjectDietLabelsGlutenFree
from swagger_client.models.branded_food_object_diet_labels_vegan import BrandedFoodObjectDietLabelsVegan
from swagger_client.models.branded_food_object_diet_labels_vegetarian import BrandedFoodObjectDietLabelsVegetarian
from swagger_client.models.branded_food_object_items import BrandedFoodObjectItems
from swagger_client.models.branded_food_object_nutrients import BrandedFoodObjectNutrients
from swagger_client.models.branded_food_object_package import BrandedFoodObjectPackage
from swagger_client.models.branded_food_object_packaging_photos import BrandedFoodObjectPackagingPhotos
from swagger_client.models.branded_food_object_packaging_photos_front import BrandedFoodObjectPackagingPhotosFront
from swagger_client.models.branded_food_object_packaging_photos_ingredients import BrandedFoodObjectPackagingPhotosIngredients
from swagger_client.models.branded_food_object_packaging_photos_nutrition import BrandedFoodObjectPackagingPhotosNutrition
from swagger_client.models.branded_food_object_serving import BrandedFoodObjectServing
from swagger_client.models.ingredient_object import IngredientObject
from swagger_client.models.ingredient_object_calorie_conversion_factor import IngredientObjectCalorieConversionFactor
from swagger_client.models.ingredient_object_components import IngredientObjectComponents
from swagger_client.models.ingredient_object_items import IngredientObjectItems
from swagger_client.models.ingredient_object_nutrients import IngredientObjectNutrients
from swagger_client.models.ingredient_object_portions import IngredientObjectPortions
