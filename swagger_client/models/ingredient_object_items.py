# coding: utf-8

"""
    Chomp Food Database API Documentation

    __Important:__   - An __[API key](https://chompthis.com/api/)__ is required for access to this API. Get yours at __[https://chompthis.com/api](https://chompthis.com/api/)__.  -----  __Getting Started:__   - __[Subscribe](https://chompthis.com/api/#pricing)__ to the API.   - Scroll down and click the \"__Authorize__\" button.   - Enter your API key into the \"__value__\" input, click the \"__Authorize__\" button, then click the \"__Close__\" button.   - Scroll down to the section titled \"__default__\" and click on the API endpoint you wish to use.   - Click the \"__Try it out__\" button.   - Enter the information the endpoint requires.   - Click the \"__Execute__\" button.  __Example:__    - Branded Food: __[View example](https://raw.githubusercontent.com/chompfoods/examples/master/branded-food-response-object.json)__ API response object.   - Ingredient: __[View example](https://raw.githubusercontent.com/chompfoods/examples/master/ingredient-response-object.json)__ API response object.  -----  __How Do I Find My API Key?__   - Your API key was sent to the email address you used to create your subscription.   - You will also find your API key in the __[Client Center](https://chompthis.com/api/manage.php)__.   - _Read __[this article](https://desk.zoho.com/portal/chompthis/kb/articles/how-do-i-find-my-api-key)__ for more information._  ||| | ------- | -------- | | [Knowledge Base](https://desk.zoho.com/portal/chompthis/kb/chomp) | [Pricing](https://chompthis.com/api/) | | [Attribution](https://chompthis.com/api/docs/attribution.php) | [Cost Calculator](https://chompthis.com/api/cost-calculator.php) | | [Terms & License](https://chompthis.com/api/terms.php) | [Database Search](https://chompthis.com/api/lookup.php) | | [Support](https://chompthis.com/api/ticket-new.php) | [Query Builder](https://chompthis.com/api/build.php) | | [Client Center](https://chompthis.com/api/manage.php) | |   # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class IngredientObjectItems(object):
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
        'name': 'str',
        'categories': 'list[str]',
        'nutrients': 'IngredientObjectNutrients',
        'calorie_conversion_factor': 'BrandedFoodObjectCalorieConversionFactor',
        'protein_conversion_factor': 'float',
        'diet_labels': 'BrandedFoodObjectDietLabels',
        'components': 'list[BrandedFoodObjectComponents]',
        'portions': 'list[BrandedFoodObjectPortions]',
        'common_names': 'str',
        'description': 'str',
        'footnote': 'str'
    }

    attribute_map = {
        'name': 'name',
        'categories': 'categories',
        'nutrients': 'nutrients',
        'calorie_conversion_factor': 'calorie_conversion_factor',
        'protein_conversion_factor': 'protein_conversion_factor',
        'diet_labels': 'diet_labels',
        'components': 'components',
        'portions': 'portions',
        'common_names': 'common_names',
        'description': 'description',
        'footnote': 'footnote'
    }

    def __init__(self, name=None, categories=None, nutrients=None, calorie_conversion_factor=None, protein_conversion_factor=None, diet_labels=None, components=None, portions=None, common_names=None, description=None, footnote=None):  # noqa: E501
        """IngredientObjectItems - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._categories = None
        self._nutrients = None
        self._calorie_conversion_factor = None
        self._protein_conversion_factor = None
        self._diet_labels = None
        self._components = None
        self._portions = None
        self._common_names = None
        self._description = None
        self._footnote = None
        self.discriminator = None
        if name is not None:
            self.name = name
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
        if components is not None:
            self.components = components
        if portions is not None:
            self.portions = portions
        if common_names is not None:
            self.common_names = common_names
        if description is not None:
            self.description = description
        if footnote is not None:
            self.footnote = footnote

    @property
    def name(self):
        """Gets the name of this IngredientObjectItems.  # noqa: E501

        Item name as provided by brand owner or as shown on packaging  # noqa: E501

        :return: The name of this IngredientObjectItems.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IngredientObjectItems.

        Item name as provided by brand owner or as shown on packaging  # noqa: E501

        :param name: The name of this IngredientObjectItems.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def categories(self):
        """Gets the categories of this IngredientObjectItems.  # noqa: E501


        :return: The categories of this IngredientObjectItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this IngredientObjectItems.


        :param categories: The categories of this IngredientObjectItems.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    @property
    def nutrients(self):
        """Gets the nutrients of this IngredientObjectItems.  # noqa: E501


        :return: The nutrients of this IngredientObjectItems.  # noqa: E501
        :rtype: IngredientObjectNutrients
        """
        return self._nutrients

    @nutrients.setter
    def nutrients(self, nutrients):
        """Sets the nutrients of this IngredientObjectItems.


        :param nutrients: The nutrients of this IngredientObjectItems.  # noqa: E501
        :type: IngredientObjectNutrients
        """

        self._nutrients = nutrients

    @property
    def calorie_conversion_factor(self):
        """Gets the calorie_conversion_factor of this IngredientObjectItems.  # noqa: E501


        :return: The calorie_conversion_factor of this IngredientObjectItems.  # noqa: E501
        :rtype: BrandedFoodObjectCalorieConversionFactor
        """
        return self._calorie_conversion_factor

    @calorie_conversion_factor.setter
    def calorie_conversion_factor(self, calorie_conversion_factor):
        """Sets the calorie_conversion_factor of this IngredientObjectItems.


        :param calorie_conversion_factor: The calorie_conversion_factor of this IngredientObjectItems.  # noqa: E501
        :type: BrandedFoodObjectCalorieConversionFactor
        """

        self._calorie_conversion_factor = calorie_conversion_factor

    @property
    def protein_conversion_factor(self):
        """Gets the protein_conversion_factor of this IngredientObjectItems.  # noqa: E501

        The multiplication factor used to calculate protein from nitrogen  # noqa: E501

        :return: The protein_conversion_factor of this IngredientObjectItems.  # noqa: E501
        :rtype: float
        """
        return self._protein_conversion_factor

    @protein_conversion_factor.setter
    def protein_conversion_factor(self, protein_conversion_factor):
        """Sets the protein_conversion_factor of this IngredientObjectItems.

        The multiplication factor used to calculate protein from nitrogen  # noqa: E501

        :param protein_conversion_factor: The protein_conversion_factor of this IngredientObjectItems.  # noqa: E501
        :type: float
        """

        self._protein_conversion_factor = protein_conversion_factor

    @property
    def diet_labels(self):
        """Gets the diet_labels of this IngredientObjectItems.  # noqa: E501


        :return: The diet_labels of this IngredientObjectItems.  # noqa: E501
        :rtype: BrandedFoodObjectDietLabels
        """
        return self._diet_labels

    @diet_labels.setter
    def diet_labels(self, diet_labels):
        """Sets the diet_labels of this IngredientObjectItems.


        :param diet_labels: The diet_labels of this IngredientObjectItems.  # noqa: E501
        :type: BrandedFoodObjectDietLabels
        """

        self._diet_labels = diet_labels

    @property
    def components(self):
        """Gets the components of this IngredientObjectItems.  # noqa: E501

        An array of objects containing the constituent parts of a food (e.g. bone is a component of meat)  # noqa: E501

        :return: The components of this IngredientObjectItems.  # noqa: E501
        :rtype: list[BrandedFoodObjectComponents]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this IngredientObjectItems.

        An array of objects containing the constituent parts of a food (e.g. bone is a component of meat)  # noqa: E501

        :param components: The components of this IngredientObjectItems.  # noqa: E501
        :type: list[BrandedFoodObjectComponents]
        """

        self._components = components

    @property
    def portions(self):
        """Gets the portions of this IngredientObjectItems.  # noqa: E501

        An array of objects containing information on discrete amounts of a food found in this item  # noqa: E501

        :return: The portions of this IngredientObjectItems.  # noqa: E501
        :rtype: list[BrandedFoodObjectPortions]
        """
        return self._portions

    @portions.setter
    def portions(self, portions):
        """Sets the portions of this IngredientObjectItems.

        An array of objects containing information on discrete amounts of a food found in this item  # noqa: E501

        :param portions: The portions of this IngredientObjectItems.  # noqa: E501
        :type: list[BrandedFoodObjectPortions]
        """

        self._portions = portions

    @property
    def common_names(self):
        """Gets the common_names of this IngredientObjectItems.  # noqa: E501

        Common names associated with this item. These generally clarify what the item is (e.g. when the brand name is \"BRAND's Spicy Enchilada\" the common name may be \"Chicken enchilada\")  # noqa: E501

        :return: The common_names of this IngredientObjectItems.  # noqa: E501
        :rtype: str
        """
        return self._common_names

    @common_names.setter
    def common_names(self, common_names):
        """Sets the common_names of this IngredientObjectItems.

        Common names associated with this item. These generally clarify what the item is (e.g. when the brand name is \"BRAND's Spicy Enchilada\" the common name may be \"Chicken enchilada\")  # noqa: E501

        :param common_names: The common_names of this IngredientObjectItems.  # noqa: E501
        :type: str
        """

        self._common_names = common_names

    @property
    def description(self):
        """Gets the description of this IngredientObjectItems.  # noqa: E501

        A description of this item  # noqa: E501

        :return: The description of this IngredientObjectItems.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IngredientObjectItems.

        A description of this item  # noqa: E501

        :param description: The description of this IngredientObjectItems.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def footnote(self):
        """Gets the footnote of this IngredientObjectItems.  # noqa: E501

        Comments on any unusual aspects of this item. Examples might include unusual aspects of the food overall.  # noqa: E501

        :return: The footnote of this IngredientObjectItems.  # noqa: E501
        :rtype: str
        """
        return self._footnote

    @footnote.setter
    def footnote(self, footnote):
        """Sets the footnote of this IngredientObjectItems.

        Comments on any unusual aspects of this item. Examples might include unusual aspects of the food overall.  # noqa: E501

        :param footnote: The footnote of this IngredientObjectItems.  # noqa: E501
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
        if issubclass(IngredientObjectItems, dict):
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
        if not isinstance(other, IngredientObjectItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
