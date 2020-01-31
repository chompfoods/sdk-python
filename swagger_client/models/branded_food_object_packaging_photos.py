# coding: utf-8

"""
    Chomp Food Database API Documentation

    ## Important An **[API key](https://chompthis.com/api/)** is required for access to this API. Get yours at **[https://chompthis.com/api](https://chompthis.com/api/)**.  ### Getting Started   * **[Subscribe](https://chompthis.com/api/#pricing)** to the API.   * Scroll down and click the \"**Authorize**\" button.   * Enter your API key into the \"**value**\" input, click the \"**Authorize**\" button, then click the \"**Close**\" button.   * Scroll down to the section titled \"**default**\" and click on the API endpoint you wish to use.   * Click the \"**Try it out**\" button.   * Enter the information the endpoint requires.   * Click the \"**Execute**\" button.  ### Example    * Branded food response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/branded-food-response-object.json)**   * Ingredient response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/ingredient-response-object.json)**   * Error response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/error-response-object.json)**  ### How Do I Find My API Key?   * Your API key was sent to the email address you used to create your subscription.   * You will also find your API key in the **[Client Center](https://chompthis.com/api/manage.php)**.   * Read **[this article](https://desk.zoho.com/portal/chompthis/kb/articles/how-do-i-find-my-api-key)** for more information.  ### Helpful Links   * **Help & Support**     * [Knowledge Base &raquo;](https://desk.zoho.com/portal/chompthis/kb/chomp)     * [Support &raquo;](https://chompthis.com/api/ticket-new.php)     * [Client Center &raquo;](https://chompthis.com/api/manage.php)   * **Pricing**     * [Subscription Options &raquo;](https://chompthis.com/api/)     * [Cost Calculator &raquo;](https://chompthis.com/api/cost-calculator.php)   * **Guidelines**     * [Terms & License &raquo;](https://chompthis.com/api/terms.php)     * [Attribution &raquo;](https://chompthis.com/api/docs/attribution.php)   # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class BrandedFoodObjectPackagingPhotos(object):
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
        'front': 'BrandedFoodObjectPackagingPhotosFront',
        'nutrition': 'BrandedFoodObjectPackagingPhotosNutrition',
        'ingredients': 'BrandedFoodObjectPackagingPhotosIngredients'
    }

    attribute_map = {
        'front': 'front',
        'nutrition': 'nutrition',
        'ingredients': 'ingredients'
    }

    def __init__(self, front=None, nutrition=None, ingredients=None):  # noqa: E501
        """BrandedFoodObjectPackagingPhotos - a model defined in Swagger"""  # noqa: E501
        self._front = None
        self._nutrition = None
        self._ingredients = None
        self.discriminator = None
        if front is not None:
            self.front = front
        if nutrition is not None:
            self.nutrition = nutrition
        if ingredients is not None:
            self.ingredients = ingredients

    @property
    def front(self):
        """Gets the front of this BrandedFoodObjectPackagingPhotos.  # noqa: E501


        :return: The front of this BrandedFoodObjectPackagingPhotos.  # noqa: E501
        :rtype: BrandedFoodObjectPackagingPhotosFront
        """
        return self._front

    @front.setter
    def front(self, front):
        """Sets the front of this BrandedFoodObjectPackagingPhotos.


        :param front: The front of this BrandedFoodObjectPackagingPhotos.  # noqa: E501
        :type: BrandedFoodObjectPackagingPhotosFront
        """

        self._front = front

    @property
    def nutrition(self):
        """Gets the nutrition of this BrandedFoodObjectPackagingPhotos.  # noqa: E501


        :return: The nutrition of this BrandedFoodObjectPackagingPhotos.  # noqa: E501
        :rtype: BrandedFoodObjectPackagingPhotosNutrition
        """
        return self._nutrition

    @nutrition.setter
    def nutrition(self, nutrition):
        """Sets the nutrition of this BrandedFoodObjectPackagingPhotos.


        :param nutrition: The nutrition of this BrandedFoodObjectPackagingPhotos.  # noqa: E501
        :type: BrandedFoodObjectPackagingPhotosNutrition
        """

        self._nutrition = nutrition

    @property
    def ingredients(self):
        """Gets the ingredients of this BrandedFoodObjectPackagingPhotos.  # noqa: E501


        :return: The ingredients of this BrandedFoodObjectPackagingPhotos.  # noqa: E501
        :rtype: BrandedFoodObjectPackagingPhotosIngredients
        """
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        """Sets the ingredients of this BrandedFoodObjectPackagingPhotos.


        :param ingredients: The ingredients of this BrandedFoodObjectPackagingPhotos.  # noqa: E501
        :type: BrandedFoodObjectPackagingPhotosIngredients
        """

        self._ingredients = ingredients

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
        if issubclass(BrandedFoodObjectPackagingPhotos, dict):
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
        if not isinstance(other, BrandedFoodObjectPackagingPhotos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
