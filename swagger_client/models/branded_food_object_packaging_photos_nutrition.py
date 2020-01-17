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


class BrandedFoodObjectPackagingPhotosNutrition(object):
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
        'small': 'str',
        'thumb': 'str',
        'display': 'str'
    }

    attribute_map = {
        'small': 'small',
        'thumb': 'thumb',
        'display': 'display'
    }

    def __init__(self, small=None, thumb=None, display=None):  # noqa: E501
        """BrandedFoodObjectPackagingPhotosNutrition - a model defined in Swagger"""  # noqa: E501
        self._small = None
        self._thumb = None
        self._display = None
        self.discriminator = None
        if small is not None:
            self.small = small
        if thumb is not None:
            self.thumb = thumb
        if display is not None:
            self.display = display

    @property
    def small(self):
        """Gets the small of this BrandedFoodObjectPackagingPhotosNutrition.  # noqa: E501

        Small photo of this item's nutrition label  # noqa: E501

        :return: The small of this BrandedFoodObjectPackagingPhotosNutrition.  # noqa: E501
        :rtype: str
        """
        return self._small

    @small.setter
    def small(self, small):
        """Sets the small of this BrandedFoodObjectPackagingPhotosNutrition.

        Small photo of this item's nutrition label  # noqa: E501

        :param small: The small of this BrandedFoodObjectPackagingPhotosNutrition.  # noqa: E501
        :type: str
        """

        self._small = small

    @property
    def thumb(self):
        """Gets the thumb of this BrandedFoodObjectPackagingPhotosNutrition.  # noqa: E501

        Thumbnail photo of this item's nutrition label  # noqa: E501

        :return: The thumb of this BrandedFoodObjectPackagingPhotosNutrition.  # noqa: E501
        :rtype: str
        """
        return self._thumb

    @thumb.setter
    def thumb(self, thumb):
        """Sets the thumb of this BrandedFoodObjectPackagingPhotosNutrition.

        Thumbnail photo of this item's nutrition label  # noqa: E501

        :param thumb: The thumb of this BrandedFoodObjectPackagingPhotosNutrition.  # noqa: E501
        :type: str
        """

        self._thumb = thumb

    @property
    def display(self):
        """Gets the display of this BrandedFoodObjectPackagingPhotosNutrition.  # noqa: E501

        Full-sized photo of this item's nutrition label  # noqa: E501

        :return: The display of this BrandedFoodObjectPackagingPhotosNutrition.  # noqa: E501
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this BrandedFoodObjectPackagingPhotosNutrition.

        Full-sized photo of this item's nutrition label  # noqa: E501

        :param display: The display of this BrandedFoodObjectPackagingPhotosNutrition.  # noqa: E501
        :type: str
        """

        self._display = display

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
        if issubclass(BrandedFoodObjectPackagingPhotosNutrition, dict):
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
        if not isinstance(other, BrandedFoodObjectPackagingPhotosNutrition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
