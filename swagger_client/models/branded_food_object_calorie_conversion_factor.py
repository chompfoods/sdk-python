# coding: utf-8

"""
    Chomp Food Database API Documentation

    __Important:__   - An __[API key](https://chompthis.com/api/)__ is required for access to this API.   - Get yours at __[https://chompthis.com/api](https://chompthis.com/api/)__.  -----  __Getting Started:__   - __[Subscribe](https://chompthis.com/api/#pricing)__ to the API.   - Scroll down and click the \"__Authorize__\" button.   - Enter your API key into the \"__value__\" input, click the \"__Authorize__\" button, then click the \"__Close__\" button.   - Scroll down to the section titled \"__default__\" and click on the API endpoint you wish to use.   - Click the \"__Try it out__\" button.   - Enter the information the endpoint requires.   - Click the \"__Execute__\" button.  __Example:__    - __[View example](https://raw.githubusercontent.com/chompfoods/examples/master/response-object.json)__ API response object.  -----  __How Do I Find My API Key?__   - Your API key was sent to the email address you used to create your subscription.   - You will also find your API key in the __[Client Center](https://chompthis.com/api/manage.php)__.   - _Read __[this article](https://desk.zoho.com/portal/chompthis/kb/articles/how-do-i-find-my-api-key)__ for more information._  ||| | ------- | -------- | | [Knowledge Base](https://desk.zoho.com/portal/chompthis/kb/chomp) | [Pricing](https://chompthis.com/api/) | | [Attribution](https://chompthis.com/api/docs/attribution.php) | [Cost Calculator](https://chompthis.com/api/cost-calculator.php) | | [Terms & License](https://chompthis.com/api/terms.php) | [Database Search](https://chompthis.com/api/lookup.php) | | [Support](https://chompthis.com/api/ticket-new.php) | [Query Builder](https://chompthis.com/api/build.php) | | [Client Center](https://chompthis.com/api/manage.php) | |   # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class BrandedFoodObjectCalorieConversionFactor(object):
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
        'protein_value': 'float',
        'fat_value': 'float',
        'carbohydrate_value': 'float'
    }

    attribute_map = {
        'protein_value': 'protein_value',
        'fat_value': 'fat_value',
        'carbohydrate_value': 'carbohydrate_value'
    }

    def __init__(self, protein_value=None, fat_value=None, carbohydrate_value=None):  # noqa: E501
        """BrandedFoodObjectCalorieConversionFactor - a model defined in Swagger"""  # noqa: E501
        self._protein_value = None
        self._fat_value = None
        self._carbohydrate_value = None
        self.discriminator = None
        if protein_value is not None:
            self.protein_value = protein_value
        if fat_value is not None:
            self.fat_value = fat_value
        if carbohydrate_value is not None:
            self.carbohydrate_value = carbohydrate_value

    @property
    def protein_value(self):
        """Gets the protein_value of this BrandedFoodObjectCalorieConversionFactor.  # noqa: E501

        The multiplication factor for protein  # noqa: E501

        :return: The protein_value of this BrandedFoodObjectCalorieConversionFactor.  # noqa: E501
        :rtype: float
        """
        return self._protein_value

    @protein_value.setter
    def protein_value(self, protein_value):
        """Sets the protein_value of this BrandedFoodObjectCalorieConversionFactor.

        The multiplication factor for protein  # noqa: E501

        :param protein_value: The protein_value of this BrandedFoodObjectCalorieConversionFactor.  # noqa: E501
        :type: float
        """

        self._protein_value = protein_value

    @property
    def fat_value(self):
        """Gets the fat_value of this BrandedFoodObjectCalorieConversionFactor.  # noqa: E501

        The multiplication factor for fat  # noqa: E501

        :return: The fat_value of this BrandedFoodObjectCalorieConversionFactor.  # noqa: E501
        :rtype: float
        """
        return self._fat_value

    @fat_value.setter
    def fat_value(self, fat_value):
        """Sets the fat_value of this BrandedFoodObjectCalorieConversionFactor.

        The multiplication factor for fat  # noqa: E501

        :param fat_value: The fat_value of this BrandedFoodObjectCalorieConversionFactor.  # noqa: E501
        :type: float
        """

        self._fat_value = fat_value

    @property
    def carbohydrate_value(self):
        """Gets the carbohydrate_value of this BrandedFoodObjectCalorieConversionFactor.  # noqa: E501

        The multiplication factor for carbohydrates  # noqa: E501

        :return: The carbohydrate_value of this BrandedFoodObjectCalorieConversionFactor.  # noqa: E501
        :rtype: float
        """
        return self._carbohydrate_value

    @carbohydrate_value.setter
    def carbohydrate_value(self, carbohydrate_value):
        """Sets the carbohydrate_value of this BrandedFoodObjectCalorieConversionFactor.

        The multiplication factor for carbohydrates  # noqa: E501

        :param carbohydrate_value: The carbohydrate_value of this BrandedFoodObjectCalorieConversionFactor.  # noqa: E501
        :type: float
        """

        self._carbohydrate_value = carbohydrate_value

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
        if issubclass(BrandedFoodObjectCalorieConversionFactor, dict):
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
        if not isinstance(other, BrandedFoodObjectCalorieConversionFactor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
