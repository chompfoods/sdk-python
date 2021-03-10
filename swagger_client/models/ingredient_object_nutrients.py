# coding: utf-8

"""
    Chomp Food & Recipe Database API Documentation

    ## Important An **[API key](https://chompthis.com/api/)** is required for access to this API. * Get a **Food Data API** key at **[https://chompthis.com/api](https://chompthis.com/api/)**. * Get a **Recipe Data API** key at **[https://chompthis.com/api/recipes](https://chompthis.com/api/recipes/)**.  ### Getting Started   * Subscribe to the **[Food Data API](https://chompthis.com/api/#pricing)** or the **[Recipe Data API](https://chompthis.com/api/recipes/#pricing)**.   * Scroll down and click the \"**Authorize**\" button.   * Enter your API key into the \"**value**\" input, click the \"**Authorize**\" button, then click the \"**Close**\" button.   * Scroll down to the section titled \"**default**\" and click on the API endpoint you wish to use.   * Click the \"**Try it out**\" button.   * Enter the information the endpoint requires.   * Click the \"**Execute**\" button.  ### Example    * Branded food response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/branded-food-response-object.json)**   * Ingredient response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/ingredient-response-object.json)**   * Recipe response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/example-recipe-response.json)**   * Error response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/error-response-object.json)**  ### How Do I Find My API Key?   * Your API key was sent to the email address you used to create your subscription.   * You will also find your API key in the **[Client Center](https://chompthis.com/api/manage.php)**.   * Read **[this article](https://desk.zoho.com/portal/chompthis/kb/articles/how-do-i-find-my-api-key)** for more information.  ### I'm a Premium subscriber. How do I access the API?   * All Premium subscribers must pass in a unique user ID for each user on their platform that is accessing data from the Chomp API. A user ID can be any string of letters and numbers that you assign to your user. Simply add \"user_id\" as a URL parameter when calling the API. *You must add a \"user_id\" URL parameter to every call you make to ANY endpoint.*     * **Example**        > ```ENDPOINT.php?api_key=API_KEY&code=CODE&user_id=USER_ID```  ### Helpful Links   * **Help & Support**     * [Knowledge Base &raquo;](https://desk.zoho.com/portal/chompthis/kb/chomp)     * [Support &raquo;](https://chompthis.com/api/ticket-new.php)     * [Client Center &raquo;](https://chompthis.com/api/manage.php)   * **Pricing**     * [Food Data API Subscription Options &raquo;](https://chompthis.com/api/)     * [Recipe Data API Subscription Options &raquo;](https://chompthis.com/api/recipes/)     * [Food Data API Cost Calculator &raquo;](https://chompthis.com/api/cost-calculator.php)     * [Recipe Data API Cost Calculator &raquo;](https://chompthis.com/api/recipes/cost-calculator.php)   * **Guidelines**     * [Terms & License &raquo;](https://chompthis.com/api/terms.php)     * [Attribution &raquo;](https://chompthis.com/api/docs/attribution.php)   # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class IngredientObjectNutrients(object):
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
        'per_100g': 'float',
        'measurement_unit': 'str',
        'min': 'float',
        'max': 'float',
        'median': 'float',
        'rank': 'int',
        'data_points': 'int',
        'footnote': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'per_100g': 'per_100g',
        'measurement_unit': 'measurement_unit',
        'min': 'min',
        'max': 'max',
        'median': 'median',
        'rank': 'rank',
        'data_points': 'data_points',
        'footnote': 'footnote',
        'description': 'description'
    }

    def __init__(self, name=None, per_100g=None, measurement_unit=None, min=None, max=None, median=None, rank=None, data_points=None, footnote=None, description=None):  # noqa: E501
        """IngredientObjectNutrients - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._per_100g = None
        self._measurement_unit = None
        self._min = None
        self._max = None
        self._median = None
        self._rank = None
        self._data_points = None
        self._footnote = None
        self._description = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if per_100g is not None:
            self.per_100g = per_100g
        if measurement_unit is not None:
            self.measurement_unit = measurement_unit
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if median is not None:
            self.median = median
        if rank is not None:
            self.rank = rank
        if data_points is not None:
            self.data_points = data_points
        if footnote is not None:
            self.footnote = footnote
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this IngredientObjectNutrients.  # noqa: E501

        Nutrient name  # noqa: E501

        :return: The name of this IngredientObjectNutrients.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IngredientObjectNutrients.

        Nutrient name  # noqa: E501

        :param name: The name of this IngredientObjectNutrients.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def per_100g(self):
        """Gets the per_100g of this IngredientObjectNutrients.  # noqa: E501

        Amount of the nutrient per 100g of food  # noqa: E501

        :return: The per_100g of this IngredientObjectNutrients.  # noqa: E501
        :rtype: float
        """
        return self._per_100g

    @per_100g.setter
    def per_100g(self, per_100g):
        """Sets the per_100g of this IngredientObjectNutrients.

        Amount of the nutrient per 100g of food  # noqa: E501

        :param per_100g: The per_100g of this IngredientObjectNutrients.  # noqa: E501
        :type: float
        """

        self._per_100g = per_100g

    @property
    def measurement_unit(self):
        """Gets the measurement_unit of this IngredientObjectNutrients.  # noqa: E501

        The unit used for the measure of this nutrient  # noqa: E501

        :return: The measurement_unit of this IngredientObjectNutrients.  # noqa: E501
        :rtype: str
        """
        return self._measurement_unit

    @measurement_unit.setter
    def measurement_unit(self, measurement_unit):
        """Sets the measurement_unit of this IngredientObjectNutrients.

        The unit used for the measure of this nutrient  # noqa: E501

        :param measurement_unit: The measurement_unit of this IngredientObjectNutrients.  # noqa: E501
        :type: str
        """

        self._measurement_unit = measurement_unit

    @property
    def min(self):
        """Gets the min of this IngredientObjectNutrients.  # noqa: E501

        Minimum nutrient value  # noqa: E501

        :return: The min of this IngredientObjectNutrients.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this IngredientObjectNutrients.

        Minimum nutrient value  # noqa: E501

        :param min: The min of this IngredientObjectNutrients.  # noqa: E501
        :type: float
        """

        self._min = min

    @property
    def max(self):
        """Gets the max of this IngredientObjectNutrients.  # noqa: E501

        Maximum nutrient value  # noqa: E501

        :return: The max of this IngredientObjectNutrients.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this IngredientObjectNutrients.

        Maximum nutrient value  # noqa: E501

        :param max: The max of this IngredientObjectNutrients.  # noqa: E501
        :type: float
        """

        self._max = max

    @property
    def median(self):
        """Gets the median of this IngredientObjectNutrients.  # noqa: E501

        Median nutrient value  # noqa: E501

        :return: The median of this IngredientObjectNutrients.  # noqa: E501
        :rtype: float
        """
        return self._median

    @median.setter
    def median(self, median):
        """Sets the median of this IngredientObjectNutrients.

        Median nutrient value  # noqa: E501

        :param median: The median of this IngredientObjectNutrients.  # noqa: E501
        :type: float
        """

        self._median = median

    @property
    def rank(self):
        """Gets the rank of this IngredientObjectNutrients.  # noqa: E501

        Nutrient rank  # noqa: E501

        :return: The rank of this IngredientObjectNutrients.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this IngredientObjectNutrients.

        Nutrient rank  # noqa: E501

        :param rank: The rank of this IngredientObjectNutrients.  # noqa: E501
        :type: int
        """

        self._rank = rank

    @property
    def data_points(self):
        """Gets the data_points of this IngredientObjectNutrients.  # noqa: E501

        Number of observations on which the value is based  # noqa: E501

        :return: The data_points of this IngredientObjectNutrients.  # noqa: E501
        :rtype: int
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        """Sets the data_points of this IngredientObjectNutrients.

        Number of observations on which the value is based  # noqa: E501

        :param data_points: The data_points of this IngredientObjectNutrients.  # noqa: E501
        :type: int
        """

        self._data_points = data_points

    @property
    def footnote(self):
        """Gets the footnote of this IngredientObjectNutrients.  # noqa: E501

        Comments on any unusual aspect of the food nutrient. Examples might include why a nutrient value is different than typically expected.  # noqa: E501

        :return: The footnote of this IngredientObjectNutrients.  # noqa: E501
        :rtype: str
        """
        return self._footnote

    @footnote.setter
    def footnote(self, footnote):
        """Sets the footnote of this IngredientObjectNutrients.

        Comments on any unusual aspect of the food nutrient. Examples might include why a nutrient value is different than typically expected.  # noqa: E501

        :param footnote: The footnote of this IngredientObjectNutrients.  # noqa: E501
        :type: str
        """

        self._footnote = footnote

    @property
    def description(self):
        """Gets the description of this IngredientObjectNutrients.  # noqa: E501

        Description of the nutrient source  # noqa: E501

        :return: The description of this IngredientObjectNutrients.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IngredientObjectNutrients.

        Description of the nutrient source  # noqa: E501

        :param description: The description of this IngredientObjectNutrients.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(IngredientObjectNutrients, dict):
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
        if not isinstance(other, IngredientObjectNutrients):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
