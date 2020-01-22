# coding: utf-8

"""
    Chomp Food Database API Documentation

    ## Important An **[API key](https://chompthis.com/api/)** is required for access to this API. Get yours at **[https://chompthis.com/api](https://chompthis.com/api/)**.  ### Getting Started   * **[Subscribe](https://chompthis.com/api/#pricing)** to the API.   * Scroll down and click the \"**Authorize**\" button.   * Enter your API key into the \"**value**\" input, click the \"**Authorize**\" button, then click the \"**Close**\" button.   * Scroll down to the section titled \"**default**\" and click on the API endpoint you wish to use.   * Click the \"**Try it out**\" button.   * Enter the information the endpoint requires.   * Click the \"**Execute**\" button.  ### Example    * Branded food response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/branded-food-response-object.json)**   * Ingredient response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/ingredient-response-object.json)**  ### How Do I Find My API Key?   * Your API key was sent to the email address you used to create your subscription.   * You will also find your API key in the **[Client Center](https://chompthis.com/api/manage.php)**.   * Read **[this article](https://desk.zoho.com/portal/chompthis/kb/articles/how-do-i-find-my-api-key)** for more information.  ||| | ------- | -------- | | [Knowledge Base](https://desk.zoho.com/portal/chompthis/kb/chomp) | [Pricing](https://chompthis.com/api/) | | [Attribution](https://chompthis.com/api/docs/attribution.php) | [Cost Calculator](https://chompthis.com/api/cost-calculator.php) | | [Terms & License](https://chompthis.com/api/terms.php) | [Database Search](https://chompthis.com/api/lookup.php) | | [Support](https://chompthis.com/api/ticket-new.php) | [Query Builder](https://chompthis.com/api/build.php) | | [Client Center](https://chompthis.com/api/manage.php) | |   # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class BrandedFoodObjectItems(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'barcode': 'str',
        'name': 'str',
        'brand': 'str',
        'ingredients': 'BrandedFoodObjectIngredients',
        'package': 'BrandedFoodObjectPackage',
        'serving': 'BrandedFoodObjectServing',
        'categories': 'list[str]',
        'nutrients': 'BrandedFoodObjectNutrients',
        'calorie_conversion_factor': 'BrandedFoodObjectCalorieConversionFactor',
        'protein_conversion_factor': 'float',
        'diet_labels': 'BrandedFoodObjectDietLabels',
        'diet_flags': 'list[BrandedFoodObjectDietFlags]',
        'packaging_photos': 'BrandedFoodObjectPackagingPhotos',
        'components': 'list[BrandedFoodObjectComponents]',
        'portions': 'list[BrandedFoodObjectPortions]',
        'allergens': 'list[str]',
        'brand_list': 'list[str]',
        'countries': 'list[str]',
        'country_details': 'BrandedFoodObjectCountryDetails',
        'palm_oil_ingredients': 'list[str]',
        'ingredient_list': 'list[str]',
        'has_english_ingredients': 'bool',
        'minerals': 'list[str]',
        'traces': 'list[str]',
        'vitamins': 'list[str]',
        'common_names': 'list[str]',
        'description': 'str',
        'keywords': 'list[str]',
        'footnote': 'str'
    }

    attribute_map = {
        'barcode': 'barcode',
        'name': 'name',
        'brand': 'brand',
        'ingredients': 'ingredients',
        'package': 'package',
        'serving': 'serving',
        'categories': 'categories',
        'nutrients': 'nutrients',
        'calorie_conversion_factor': 'calorie_conversion_factor',
        'protein_conversion_factor': 'protein_conversion_factor',
        'diet_labels': 'diet_labels',
        'diet_flags': 'diet_flags',
        'packaging_photos': 'packaging_photos',
        'components': 'components',
        'portions': 'portions',
        'allergens': 'allergens',
        'brand_list': 'brand_list',
        'countries': 'countries',
        'country_details': 'country_details',
        'palm_oil_ingredients': 'palm_oil_ingredients',
        'ingredient_list': 'ingredient_list',
        'has_english_ingredients': 'has_english_ingredients',
        'minerals': 'minerals',
        'traces': 'traces',
        'vitamins': 'vitamins',
        'common_names': 'common_names',
        'description': 'description',
        'keywords': 'keywords',
        'footnote': 'footnote'
    }

    def __init__(self, barcode=None, name=None, brand=None, ingredients=None, package=None, serving=None, categories=None, nutrients=None, calorie_conversion_factor=None, protein_conversion_factor=None, diet_labels=None, diet_flags=None, packaging_photos=None, components=None, portions=None, allergens=None, brand_list=None, countries=None, country_details=None, palm_oil_ingredients=None, ingredient_list=None, has_english_ingredients=None, minerals=None, traces=None, vitamins=None, common_names=None, description=None, keywords=None, footnote=None):  # noqa: E501
        """BrandedFoodObjectItems - a model defined in Swagger"""  # noqa: E501
        self._barcode = None
        self._name = None
        self._brand = None
        self._ingredients = None
        self._package = None
        self._serving = None
        self._categories = None
        self._nutrients = None
        self._calorie_conversion_factor = None
        self._protein_conversion_factor = None
        self._diet_labels = None
        self._diet_flags = None
        self._packaging_photos = None
        self._components = None
        self._portions = None
        self._allergens = None
        self._brand_list = None
        self._countries = None
        self._country_details = None
        self._palm_oil_ingredients = None
        self._ingredient_list = None
        self._has_english_ingredients = None
        self._minerals = None
        self._traces = None
        self._vitamins = None
        self._common_names = None
        self._description = None
        self._keywords = None
        self._footnote = None
        self.discriminator = None
        if barcode is not None:
            self.barcode = barcode
        if name is not None:
            self.name = name
        if brand is not None:
            self.brand = brand
        if ingredients is not None:
            self.ingredients = ingredients
        if package is not None:
            self.package = package
        if serving is not None:
            self.serving = serving
        if categories is not None:
            self.categories = categories
        if nutrients is not None:
            self.nutrients = nutrients
        if calorie_conversion_factor is not None:
            self.calorie_conversion_factor = calorie_conversion_factor
        if protein_conversion_factor is not None:
            self.protein_conversion_factor = protein_conversion_factor
        if diet_labels is not None:
            self.diet_labels = diet_labels
        if diet_flags is not None:
            self.diet_flags = diet_flags
        if packaging_photos is not None:
            self.packaging_photos = packaging_photos
        if components is not None:
            self.components = components
        if portions is not None:
            self.portions = portions
        if allergens is not None:
            self.allergens = allergens
        if brand_list is not None:
            self.brand_list = brand_list
        if countries is not None:
            self.countries = countries
        if country_details is not None:
            self.country_details = country_details
        if palm_oil_ingredients is not None:
            self.palm_oil_ingredients = palm_oil_ingredients
        if ingredient_list is not None:
            self.ingredient_list = ingredient_list
        if has_english_ingredients is not None:
            self.has_english_ingredients = has_english_ingredients
        if minerals is not None:
            self.minerals = minerals
        if traces is not None:
            self.traces = traces
        if vitamins is not None:
            self.vitamins = vitamins
        if common_names is not None:
            self.common_names = common_names
        if description is not None:
            self.description = description
        if keywords is not None:
            self.keywords = keywords
        if footnote is not None:
            self.footnote = footnote

    @property
    def barcode(self):
        """Gets the barcode of this BrandedFoodObjectItems.  # noqa: E501

        EAN/UPC barcode  # noqa: E501

        :return: The barcode of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: str
        """
        return self._barcode

    @barcode.setter
    def barcode(self, barcode):
        """Sets the barcode of this BrandedFoodObjectItems.

        EAN/UPC barcode  # noqa: E501

        :param barcode: The barcode of this BrandedFoodObjectItems.  # noqa: E501
        :type: str
        """

        self._barcode = barcode

    @property
    def name(self):
        """Gets the name of this BrandedFoodObjectItems.  # noqa: E501

        Item name as provided by brand owner or as shown on packaging  # noqa: E501

        :return: The name of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BrandedFoodObjectItems.

        Item name as provided by brand owner or as shown on packaging  # noqa: E501

        :param name: The name of this BrandedFoodObjectItems.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def brand(self):
        """Gets the brand of this BrandedFoodObjectItems.  # noqa: E501

        The brand name that owns this item  # noqa: E501

        :return: The brand of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this BrandedFoodObjectItems.

        The brand name that owns this item  # noqa: E501

        :param brand: The brand of this BrandedFoodObjectItems.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def ingredients(self):
        """Gets the ingredients of this BrandedFoodObjectItems.  # noqa: E501


        :return: The ingredients of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: BrandedFoodObjectIngredients
        """
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        """Sets the ingredients of this BrandedFoodObjectItems.


        :param ingredients: The ingredients of this BrandedFoodObjectItems.  # noqa: E501
        :type: BrandedFoodObjectIngredients
        """

        self._ingredients = ingredients

    @property
    def package(self):
        """Gets the package of this BrandedFoodObjectItems.  # noqa: E501


        :return: The package of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: BrandedFoodObjectPackage
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this BrandedFoodObjectItems.


        :param package: The package of this BrandedFoodObjectItems.  # noqa: E501
        :type: BrandedFoodObjectPackage
        """

        self._package = package

    @property
    def serving(self):
        """Gets the serving of this BrandedFoodObjectItems.  # noqa: E501


        :return: The serving of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: BrandedFoodObjectServing
        """
        return self._serving

    @serving.setter
    def serving(self, serving):
        """Sets the serving of this BrandedFoodObjectItems.


        :param serving: The serving of this BrandedFoodObjectItems.  # noqa: E501
        :type: BrandedFoodObjectServing
        """

        self._serving = serving

    @property
    def categories(self):
        """Gets the categories of this BrandedFoodObjectItems.  # noqa: E501


        :return: The categories of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this BrandedFoodObjectItems.


        :param categories: The categories of this BrandedFoodObjectItems.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    @property
    def nutrients(self):
        """Gets the nutrients of this BrandedFoodObjectItems.  # noqa: E501


        :return: The nutrients of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: BrandedFoodObjectNutrients
        """
        return self._nutrients

    @nutrients.setter
    def nutrients(self, nutrients):
        """Sets the nutrients of this BrandedFoodObjectItems.


        :param nutrients: The nutrients of this BrandedFoodObjectItems.  # noqa: E501
        :type: BrandedFoodObjectNutrients
        """

        self._nutrients = nutrients

    @property
    def calorie_conversion_factor(self):
        """Gets the calorie_conversion_factor of this BrandedFoodObjectItems.  # noqa: E501


        :return: The calorie_conversion_factor of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: BrandedFoodObjectCalorieConversionFactor
        """
        return self._calorie_conversion_factor

    @calorie_conversion_factor.setter
    def calorie_conversion_factor(self, calorie_conversion_factor):
        """Sets the calorie_conversion_factor of this BrandedFoodObjectItems.


        :param calorie_conversion_factor: The calorie_conversion_factor of this BrandedFoodObjectItems.  # noqa: E501
        :type: BrandedFoodObjectCalorieConversionFactor
        """

        self._calorie_conversion_factor = calorie_conversion_factor

    @property
    def protein_conversion_factor(self):
        """Gets the protein_conversion_factor of this BrandedFoodObjectItems.  # noqa: E501

        The multiplication factor used to calculate protein from nitrogen  # noqa: E501

        :return: The protein_conversion_factor of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: float
        """
        return self._protein_conversion_factor

    @protein_conversion_factor.setter
    def protein_conversion_factor(self, protein_conversion_factor):
        """Sets the protein_conversion_factor of this BrandedFoodObjectItems.

        The multiplication factor used to calculate protein from nitrogen  # noqa: E501

        :param protein_conversion_factor: The protein_conversion_factor of this BrandedFoodObjectItems.  # noqa: E501
        :type: float
        """

        self._protein_conversion_factor = protein_conversion_factor

    @property
    def diet_labels(self):
        """Gets the diet_labels of this BrandedFoodObjectItems.  # noqa: E501


        :return: The diet_labels of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: BrandedFoodObjectDietLabels
        """
        return self._diet_labels

    @diet_labels.setter
    def diet_labels(self, diet_labels):
        """Sets the diet_labels of this BrandedFoodObjectItems.


        :param diet_labels: The diet_labels of this BrandedFoodObjectItems.  # noqa: E501
        :type: BrandedFoodObjectDietLabels
        """

        self._diet_labels = diet_labels

    @property
    def diet_flags(self):
        """Gets the diet_flags of this BrandedFoodObjectItems.  # noqa: E501

        An array of ingredient objects that were flagged while grading this item for compatibility with each diet  # noqa: E501

        :return: The diet_flags of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: list[BrandedFoodObjectDietFlags]
        """
        return self._diet_flags

    @diet_flags.setter
    def diet_flags(self, diet_flags):
        """Sets the diet_flags of this BrandedFoodObjectItems.

        An array of ingredient objects that were flagged while grading this item for compatibility with each diet  # noqa: E501

        :param diet_flags: The diet_flags of this BrandedFoodObjectItems.  # noqa: E501
        :type: list[BrandedFoodObjectDietFlags]
        """

        self._diet_flags = diet_flags

    @property
    def packaging_photos(self):
        """Gets the packaging_photos of this BrandedFoodObjectItems.  # noqa: E501


        :return: The packaging_photos of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: BrandedFoodObjectPackagingPhotos
        """
        return self._packaging_photos

    @packaging_photos.setter
    def packaging_photos(self, packaging_photos):
        """Sets the packaging_photos of this BrandedFoodObjectItems.


        :param packaging_photos: The packaging_photos of this BrandedFoodObjectItems.  # noqa: E501
        :type: BrandedFoodObjectPackagingPhotos
        """

        self._packaging_photos = packaging_photos

    @property
    def components(self):
        """Gets the components of this BrandedFoodObjectItems.  # noqa: E501

        An array of objects containing the constituent parts of a food (e.g. bone is a component of meat)  # noqa: E501

        :return: The components of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: list[BrandedFoodObjectComponents]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this BrandedFoodObjectItems.

        An array of objects containing the constituent parts of a food (e.g. bone is a component of meat)  # noqa: E501

        :param components: The components of this BrandedFoodObjectItems.  # noqa: E501
        :type: list[BrandedFoodObjectComponents]
        """

        self._components = components

    @property
    def portions(self):
        """Gets the portions of this BrandedFoodObjectItems.  # noqa: E501

        An array of objects containing information on discrete amounts of a food found in this item  # noqa: E501

        :return: The portions of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: list[BrandedFoodObjectPortions]
        """
        return self._portions

    @portions.setter
    def portions(self, portions):
        """Sets the portions of this BrandedFoodObjectItems.

        An array of objects containing information on discrete amounts of a food found in this item  # noqa: E501

        :param portions: The portions of this BrandedFoodObjectItems.  # noqa: E501
        :type: list[BrandedFoodObjectPortions]
        """

        self._portions = portions

    @property
    def allergens(self):
        """Gets the allergens of this BrandedFoodObjectItems.  # noqa: E501

        An array of ingredients in this item that may cause allergic reactions in people  # noqa: E501

        :return: The allergens of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._allergens

    @allergens.setter
    def allergens(self, allergens):
        """Sets the allergens of this BrandedFoodObjectItems.

        An array of ingredients in this item that may cause allergic reactions in people  # noqa: E501

        :param allergens: The allergens of this BrandedFoodObjectItems.  # noqa: E501
        :type: list[str]
        """

        self._allergens = allergens

    @property
    def brand_list(self):
        """Gets the brand_list of this BrandedFoodObjectItems.  # noqa: E501

        An array of brands we have associated with this item. Some items are sold by more than 1 brand.  # noqa: E501

        :return: The brand_list of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._brand_list

    @brand_list.setter
    def brand_list(self, brand_list):
        """Sets the brand_list of this BrandedFoodObjectItems.

        An array of brands we have associated with this item. Some items are sold by more than 1 brand.  # noqa: E501

        :param brand_list: The brand_list of this BrandedFoodObjectItems.  # noqa: E501
        :type: list[str]
        """

        self._brand_list = brand_list

    @property
    def countries(self):
        """Gets the countries of this BrandedFoodObjectItems.  # noqa: E501

        An array of countries where this item is sold  # noqa: E501

        :return: The countries of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this BrandedFoodObjectItems.

        An array of countries where this item is sold  # noqa: E501

        :param countries: The countries of this BrandedFoodObjectItems.  # noqa: E501
        :type: list[str]
        """

        self._countries = countries

    @property
    def country_details(self):
        """Gets the country_details of this BrandedFoodObjectItems.  # noqa: E501


        :return: The country_details of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: BrandedFoodObjectCountryDetails
        """
        return self._country_details

    @country_details.setter
    def country_details(self, country_details):
        """Sets the country_details of this BrandedFoodObjectItems.


        :param country_details: The country_details of this BrandedFoodObjectItems.  # noqa: E501
        :type: BrandedFoodObjectCountryDetails
        """

        self._country_details = country_details

    @property
    def palm_oil_ingredients(self):
        """Gets the palm_oil_ingredients of this BrandedFoodObjectItems.  # noqa: E501

        An array of ingredients made from palm oil  # noqa: E501

        :return: The palm_oil_ingredients of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._palm_oil_ingredients

    @palm_oil_ingredients.setter
    def palm_oil_ingredients(self, palm_oil_ingredients):
        """Sets the palm_oil_ingredients of this BrandedFoodObjectItems.

        An array of ingredients made from palm oil  # noqa: E501

        :param palm_oil_ingredients: The palm_oil_ingredients of this BrandedFoodObjectItems.  # noqa: E501
        :type: list[str]
        """

        self._palm_oil_ingredients = palm_oil_ingredients

    @property
    def ingredient_list(self):
        """Gets the ingredient_list of this BrandedFoodObjectItems.  # noqa: E501

        An array of this item's ingredients  # noqa: E501

        :return: The ingredient_list of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._ingredient_list

    @ingredient_list.setter
    def ingredient_list(self, ingredient_list):
        """Sets the ingredient_list of this BrandedFoodObjectItems.

        An array of this item's ingredients  # noqa: E501

        :param ingredient_list: The ingredient_list of this BrandedFoodObjectItems.  # noqa: E501
        :type: list[str]
        """

        self._ingredient_list = ingredient_list

    @property
    def has_english_ingredients(self):
        """Gets the has_english_ingredients of this BrandedFoodObjectItems.  # noqa: E501

        A boolean indicating if we have English ingredients for this item  # noqa: E501

        :return: The has_english_ingredients of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: bool
        """
        return self._has_english_ingredients

    @has_english_ingredients.setter
    def has_english_ingredients(self, has_english_ingredients):
        """Sets the has_english_ingredients of this BrandedFoodObjectItems.

        A boolean indicating if we have English ingredients for this item  # noqa: E501

        :param has_english_ingredients: The has_english_ingredients of this BrandedFoodObjectItems.  # noqa: E501
        :type: bool
        """

        self._has_english_ingredients = has_english_ingredients

    @property
    def minerals(self):
        """Gets the minerals of this BrandedFoodObjectItems.  # noqa: E501

        An array of minerals that this item contains  # noqa: E501

        :return: The minerals of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._minerals

    @minerals.setter
    def minerals(self, minerals):
        """Sets the minerals of this BrandedFoodObjectItems.

        An array of minerals that this item contains  # noqa: E501

        :param minerals: The minerals of this BrandedFoodObjectItems.  # noqa: E501
        :type: list[str]
        """

        self._minerals = minerals

    @property
    def traces(self):
        """Gets the traces of this BrandedFoodObjectItems.  # noqa: E501

        An array of trace ingredients that may be found in this item  # noqa: E501

        :return: The traces of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._traces

    @traces.setter
    def traces(self, traces):
        """Sets the traces of this BrandedFoodObjectItems.

        An array of trace ingredients that may be found in this item  # noqa: E501

        :param traces: The traces of this BrandedFoodObjectItems.  # noqa: E501
        :type: list[str]
        """

        self._traces = traces

    @property
    def vitamins(self):
        """Gets the vitamins of this BrandedFoodObjectItems.  # noqa: E501

        An array of vitamins that are found in this item  # noqa: E501

        :return: The vitamins of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._vitamins

    @vitamins.setter
    def vitamins(self, vitamins):
        """Sets the vitamins of this BrandedFoodObjectItems.

        An array of vitamins that are found in this item  # noqa: E501

        :param vitamins: The vitamins of this BrandedFoodObjectItems.  # noqa: E501
        :type: list[str]
        """

        self._vitamins = vitamins

    @property
    def common_names(self):
        """Gets the common_names of this BrandedFoodObjectItems.  # noqa: E501

        An array containing other names commonly associated with this item. These generally clarify what the item is (e.g. when the brand name is \"BRAND's Spicy Enchilada\" a common name may be \"Chicken enchilada\")  # noqa: E501

        :return: The common_names of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._common_names

    @common_names.setter
    def common_names(self, common_names):
        """Sets the common_names of this BrandedFoodObjectItems.

        An array containing other names commonly associated with this item. These generally clarify what the item is (e.g. when the brand name is \"BRAND's Spicy Enchilada\" a common name may be \"Chicken enchilada\")  # noqa: E501

        :param common_names: The common_names of this BrandedFoodObjectItems.  # noqa: E501
        :type: list[str]
        """

        self._common_names = common_names

    @property
    def description(self):
        """Gets the description of this BrandedFoodObjectItems.  # noqa: E501

        A description of this item  # noqa: E501

        :return: The description of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BrandedFoodObjectItems.

        A description of this item  # noqa: E501

        :param description: The description of this BrandedFoodObjectItems.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def keywords(self):
        """Gets the keywords of this BrandedFoodObjectItems.  # noqa: E501

        An array of keywords that can be used to describe this item  # noqa: E501

        :return: The keywords of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this BrandedFoodObjectItems.

        An array of keywords that can be used to describe this item  # noqa: E501

        :param keywords: The keywords of this BrandedFoodObjectItems.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def footnote(self):
        """Gets the footnote of this BrandedFoodObjectItems.  # noqa: E501

        Comments on any unusual aspects of this item. Examples might include unusual aspects of the food overall.  # noqa: E501

        :return: The footnote of this BrandedFoodObjectItems.  # noqa: E501
        :rtype: str
        """
        return self._footnote

    @footnote.setter
    def footnote(self, footnote):
        """Sets the footnote of this BrandedFoodObjectItems.

        Comments on any unusual aspects of this item. Examples might include unusual aspects of the food overall.  # noqa: E501

        :param footnote: The footnote of this BrandedFoodObjectItems.  # noqa: E501
        :type: str
        """

        self._footnote = footnote

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BrandedFoodObjectItems, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BrandedFoodObjectItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
