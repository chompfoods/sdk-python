# coding: utf-8

# flake8: noqa
"""
    Chomp Food & Recipe Database API Documentation

    ## Important An **[API key](https://chompthis.com/api/)** is required for access to this API. * Get a **Food Data API** key at **[https://chompthis.com/api](https://chompthis.com/api/)**. * Get a **Recipe Data API** key at **[https://chompthis.com/api/recipes](https://chompthis.com/api/recipes/)**.  ### Getting Started   * Subscribe to the **[Food Data API](https://chompthis.com/api/#pricing)** or the **[Recipe Data API](https://chompthis.com/api/recipes/#pricing)**.   * Scroll down and click the \"**Authorize**\" button.   * Enter your API key into the \"**value**\" input, click the \"**Authorize**\" button, then click the \"**Close**\" button.   * Scroll down to the section titled \"**default**\" and click on the API endpoint you wish to use.   * Click the \"**Try it out**\" button.   * Enter the information the endpoint requires.   * Click the \"**Execute**\" button.  ### Example    * Branded food response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/branded-food-response-object.json)**   * Ingredient response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/ingredient-response-object.json)**   * Recipe response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/example-recipe-response.json)**   * Error response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/error-response-object.json)**  ### How Do I Find My API Key?   * Your API key was sent to the email address you used to create your subscription.   * You will also find your API key in the **[Client Center](https://chompthis.com/api/manage.php)**.   * Read **[this article](https://desk.zoho.com/portal/chompthis/kb/articles/how-do-i-find-my-api-key)** for more information.  ### I'm a Premium subscriber. How do I access the API?   * All Premium subscribers must pass in a unique user ID for each user on their platform that is accessing data from the Chomp API. A user ID can be any string of letters and numbers that you assign to your user. Simply add \"user_id\" as a URL parameter when calling the API. *You must add a \"user_id\" URL parameter to every call you make to ANY endpoint.*     * **Example**        > ```ENDPOINT.php?api_key=API_KEY&code=CODE&user_id=USER_ID```  ### Helpful Links   * **Help & Support**     * [Knowledge Base &raquo;](https://desk.zoho.com/portal/chompthis/kb/chomp)     * [Support &raquo;](https://chompthis.com/api/ticket-new.php)     * [Client Center &raquo;](https://chompthis.com/api/manage.php)   * **Pricing**     * [Food Data API Subscription Options &raquo;](https://chompthis.com/api/)     * [Recipe Data API Subscription Options &raquo;](https://chompthis.com/api/recipes/)     * [Food Data API Cost Calculator &raquo;](https://chompthis.com/api/cost-calculator.php)     * [Recipe Data API Cost Calculator &raquo;](https://chompthis.com/api/recipes/cost-calculator.php)   * **Guidelines**     * [Terms & License &raquo;](https://chompthis.com/api/terms.php)     * [Attribution &raquo;](https://chompthis.com/api/docs/attribution.php)   # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
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
from swagger_client.models.recipe_object import RecipeObject
from swagger_client.models.recipe_object_attributes import RecipeObjectAttributes
from swagger_client.models.recipe_object_ingredients import RecipeObjectIngredients
from swagger_client.models.recipe_object_items import RecipeObjectItems
from swagger_client.models.recipe_object_meta import RecipeObjectMeta
from swagger_client.models.recipe_object_meta_images import RecipeObjectMetaImages
from swagger_client.models.recipe_object_nutrients import RecipeObjectNutrients
from swagger_client.models.recipe_object_nutrients_calories import RecipeObjectNutrientsCalories
