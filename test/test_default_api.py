# coding: utf-8

"""
    Chomp Food Database API Documentation

    __Important:__   - An __[API key](https://chompthis.com/api/)__ is required for access to this API.   - Get yours at __[https://chompthis.com/api](https://chompthis.com/api/)__.  -----  __Getting Started:__   - __[Subscribe](https://chompthis.com/api/#pricing)__ to the API.   - Scroll down and click the \"__Authorize__\" button.   - Enter your API key into the \"__value__\" input, click the \"__Authorize__\" button, then click the \"__Close__\" button.   - Scroll down to the section titled \"__default__\" and click on the API endpoint you wish to use.   - Click the \"__Try it out__\" button.   - Enter the information the endpoint requires.   - Click the \"__Execute__\" button.  __Example:__    - __[View example](https://raw.githubusercontent.com/chompfoods/examples/master/response-object.json)__ API response object.  -----  __How Do I Find My API Key?__   - Your API key was sent to the email address you used to create your subscription.   - You will also find your API key in the __[Client Center](https://chompthis.com/api/manage.php)__.   - _Read __[this article](https://desk.zoho.com/portal/chompthis/kb/articles/how-do-i-find-my-api-key)__ for more information._  ||| | ------- | -------- | | [Knowledge Base](https://desk.zoho.com/portal/chompthis/kb/chomp) | [Pricing](https://chompthis.com/api/) | | [Attribution](https://chompthis.com/api/docs/attribution.php) | [Cost Calculator](https://chompthis.com/api/cost-calculator.php) | | [Terms & License](https://chompthis.com/api/terms.php) | [Database Search](https://chompthis.com/api/lookup.php) | | [Support](https://chompthis.com/api/ticket-new.php) | [Query Builder](https://chompthis.com/api/build.php) | | [Client Center](https://chompthis.com/api/manage.php) | |   # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.default_api import DefaultApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_food_branded_barcode_php_get(self):
        """Test case for food_branded_barcode_php_get

        Get a branded food item using a barcode  # noqa: E501
        """
        pass

    def test_food_branded_id_php_get(self):
        """Test case for food_branded_id_php_get

        Get a branded food item using an ID number  # noqa: E501
        """
        pass

    def test_food_branded_name_php_get(self):
        """Test case for food_branded_name_php_get

        Get a branded food item by name  # noqa: E501
        """
        pass

    def test_food_branded_search_php_get(self):
        """Test case for food_branded_search_php_get

        Get data for branded food items using various search parameters  # noqa: E501
        """
        pass

    def test_ingredient_search_php_get(self):
        """Test case for ingredient_search_php_get

        Get raw/generic food ingredient item(s)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
