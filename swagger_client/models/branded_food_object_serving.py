# coding: utf-8

"""
    Chomp Food Database API Documentation

    __Important:__   - An __[API key](https://chompthis.com/api/)__ is required for access to this API.   - Get yours at __[https://chompthis.com/api](https://chompthis.com/api/)__.  -----  __Getting Started:__   - __[Subscribe](https://chompthis.com/api/#pricing)__ to the API.   - Scroll down and click the \"__Authorize__\" button.   - Enter your API key into the \"__value__\" input, click the \"__Authorize__\" button, then click the \"__Close__\" button.   - Scroll down to the section titled \"__default__\" and click on the API endpoint you wish to use.   - Click the \"__Try it out__\" button.   - Enter the information the endpoint requires.   - Click the \"__Execute__\" button.  __Example:__    - Branded Food: __[View example](https://raw.githubusercontent.com/chompfoods/examples/master/branded-food-response-object.json)__ API response object.   - Ingredient: __[View example](https://raw.githubusercontent.com/chompfoods/examples/master/ingredient-response-object.json)__ API response object.  -----  __How Do I Find My API Key?__   - Your API key was sent to the email address you used to create your subscription.   - You will also find your API key in the __[Client Center](https://chompthis.com/api/manage.php)__.   - _Read __[this article](https://desk.zoho.com/portal/chompthis/kb/articles/how-do-i-find-my-api-key)__ for more information._  ||| | ------- | -------- | | [Knowledge Base](https://desk.zoho.com/portal/chompthis/kb/chomp) | [Pricing](https://chompthis.com/api/) | | [Attribution](https://chompthis.com/api/docs/attribution.php) | [Cost Calculator](https://chompthis.com/api/cost-calculator.php) | | [Terms & License](https://chompthis.com/api/terms.php) | [Database Search](https://chompthis.com/api/lookup.php) | | [Support](https://chompthis.com/api/ticket-new.php) | [Query Builder](https://chompthis.com/api/build.php) | | [Client Center](https://chompthis.com/api/manage.php) | |   # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class BrandedFoodObjectServing(object):
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
        'size': 'str',
        'size_fulltext': 'str',
        'total': 'int'
    }

    attribute_map = {
        'size': 'size',
        'size_fulltext': 'size_fulltext',
        'total': 'total'
    }

    def __init__(self, size=None, size_fulltext=None, total=None):  # noqa: E501
        """BrandedFoodObjectServing - a model defined in Swagger"""  # noqa: E501
        self._size = None
        self._size_fulltext = None
        self._total = None
        self.discriminator = None
        if size is not None:
            self.size = size
        if size_fulltext is not None:
            self.size_fulltext = size_fulltext
        if total is not None:
            self.total = total

    @property
    def size(self):
        """Gets the size of this BrandedFoodObjectServing.  # noqa: E501

        Serving size with measurement unit (e.g. if measure is 3 tsp, the unit is tsp)  # noqa: E501

        :return: The size of this BrandedFoodObjectServing.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BrandedFoodObjectServing.

        Serving size with measurement unit (e.g. if measure is 3 tsp, the unit is tsp)  # noqa: E501

        :param size: The size of this BrandedFoodObjectServing.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def size_fulltext(self):
        """Gets the size_fulltext of this BrandedFoodObjectServing.  # noqa: E501

        Serving size description  # noqa: E501

        :return: The size_fulltext of this BrandedFoodObjectServing.  # noqa: E501
        :rtype: str
        """
        return self._size_fulltext

    @size_fulltext.setter
    def size_fulltext(self, size_fulltext):
        """Sets the size_fulltext of this BrandedFoodObjectServing.

        Serving size description  # noqa: E501

        :param size_fulltext: The size_fulltext of this BrandedFoodObjectServing.  # noqa: E501
        :type: str
        """

        self._size_fulltext = size_fulltext

    @property
    def total(self):
        """Gets the total of this BrandedFoodObjectServing.  # noqa: E501

        Total servings  # noqa: E501

        :return: The total of this BrandedFoodObjectServing.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this BrandedFoodObjectServing.

        Total servings  # noqa: E501

        :param total: The total of this BrandedFoodObjectServing.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(BrandedFoodObjectServing, dict):
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
        if not isinstance(other, BrandedFoodObjectServing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
