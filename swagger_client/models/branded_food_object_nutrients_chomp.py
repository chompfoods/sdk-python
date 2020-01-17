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


class BrandedFoodObjectNutrientsChomp(object):
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
        'measurement_unit': 'str',
        'per_100g': 'float',
        'per_serving': 'float',
        'total': 'float'
    }

    attribute_map = {
        'name': 'name',
        'measurement_unit': 'measurement_unit',
        'per_100g': 'per_100g',
        'per_serving': 'per_serving',
        'total': 'total'
    }

    def __init__(self, name=None, measurement_unit=None, per_100g=None, per_serving=None, total=None):  # noqa: E501
        """BrandedFoodObjectNutrientsChomp - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._measurement_unit = None
        self._per_100g = None
        self._per_serving = None
        self._total = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if measurement_unit is not None:
            self.measurement_unit = measurement_unit
        if per_100g is not None:
            self.per_100g = per_100g
        if per_serving is not None:
            self.per_serving = per_serving
        if total is not None:
            self.total = total

    @property
    def name(self):
        """Gets the name of this BrandedFoodObjectNutrientsChomp.  # noqa: E501

        Nutrient name  # noqa: E501

        :return: The name of this BrandedFoodObjectNutrientsChomp.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BrandedFoodObjectNutrientsChomp.

        Nutrient name  # noqa: E501

        :param name: The name of this BrandedFoodObjectNutrientsChomp.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def measurement_unit(self):
        """Gets the measurement_unit of this BrandedFoodObjectNutrientsChomp.  # noqa: E501

        The unit used for measure (e.g. if mesure is 3 tsp, the unit is tsp)  # noqa: E501

        :return: The measurement_unit of this BrandedFoodObjectNutrientsChomp.  # noqa: E501
        :rtype: str
        """
        return self._measurement_unit

    @measurement_unit.setter
    def measurement_unit(self, measurement_unit):
        """Sets the measurement_unit of this BrandedFoodObjectNutrientsChomp.

        The unit used for measure (e.g. if mesure is 3 tsp, the unit is tsp)  # noqa: E501

        :param measurement_unit: The measurement_unit of this BrandedFoodObjectNutrientsChomp.  # noqa: E501
        :type: str
        """

        self._measurement_unit = measurement_unit

    @property
    def per_100g(self):
        """Gets the per_100g of this BrandedFoodObjectNutrientsChomp.  # noqa: E501

        Amount of the nutrient per 100g of food  # noqa: E501

        :return: The per_100g of this BrandedFoodObjectNutrientsChomp.  # noqa: E501
        :rtype: float
        """
        return self._per_100g

    @per_100g.setter
    def per_100g(self, per_100g):
        """Sets the per_100g of this BrandedFoodObjectNutrientsChomp.

        Amount of the nutrient per 100g of food  # noqa: E501

        :param per_100g: The per_100g of this BrandedFoodObjectNutrientsChomp.  # noqa: E501
        :type: float
        """

        self._per_100g = per_100g

    @property
    def per_serving(self):
        """Gets the per_serving of this BrandedFoodObjectNutrientsChomp.  # noqa: E501

        Nutrient value per serving  # noqa: E501

        :return: The per_serving of this BrandedFoodObjectNutrientsChomp.  # noqa: E501
        :rtype: float
        """
        return self._per_serving

    @per_serving.setter
    def per_serving(self, per_serving):
        """Sets the per_serving of this BrandedFoodObjectNutrientsChomp.

        Nutrient value per serving  # noqa: E501

        :param per_serving: The per_serving of this BrandedFoodObjectNutrientsChomp.  # noqa: E501
        :type: float
        """

        self._per_serving = per_serving

    @property
    def total(self):
        """Gets the total of this BrandedFoodObjectNutrientsChomp.  # noqa: E501

        Total nutrient value  # noqa: E501

        :return: The total of this BrandedFoodObjectNutrientsChomp.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this BrandedFoodObjectNutrientsChomp.

        Total nutrient value  # noqa: E501

        :param total: The total of this BrandedFoodObjectNutrientsChomp.  # noqa: E501
        :type: float
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
        if issubclass(BrandedFoodObjectNutrientsChomp, dict):
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
        if not isinstance(other, BrandedFoodObjectNutrientsChomp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
