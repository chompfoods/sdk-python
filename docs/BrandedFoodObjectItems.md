# BrandedFoodObjectItems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **str** | EAN/UPC barcode | [optional] 
**name** | **str** | Item name as provided by brand owner or as shown on packaging | [optional] 
**brand** | **str** | The brand name that owns this item | [optional] 
**ingredients** | **str** | This food item&#x27;s ingredients from greatest quantity to least | [optional] 
**package** | [**BrandedFoodObjectPackage**](BrandedFoodObjectPackage.md) |  | [optional] 
**serving** | [**BrandedFoodObjectServing**](BrandedFoodObjectServing.md) |  | [optional] 
**categories** | **list[str]** |  | [optional] 
**nutrients** | [**list[BrandedFoodObjectNutrients]**](BrandedFoodObjectNutrients.md) | An array containing nutrient informatio objects for this food item | [optional] 
**diet_labels** | [**BrandedFoodObjectDietLabels**](BrandedFoodObjectDietLabels.md) |  | [optional] 
**diet_flags** | [**list[BrandedFoodObjectDietFlags]**](BrandedFoodObjectDietFlags.md) | An array of ingredient objects that were flagged while grading this item for compatibility with each diet | [optional] 
**packaging_photos** | [**BrandedFoodObjectPackagingPhotos**](BrandedFoodObjectPackagingPhotos.md) |  | [optional] 
**allergens** | **list[str]** | An array of ingredients in this item that may cause allergic reactions in people | [optional] 
**brand_list** | **list[str]** | An array of brands we have associated with this item. Some items are sold by more than 1 brand. | [optional] 
**countries** | **list[str]** | An array of countries where this item is sold | [optional] 
**country_details** | [**BrandedFoodObjectCountryDetails**](BrandedFoodObjectCountryDetails.md) |  | [optional] 
**palm_oil_ingredients** | **list[str]** | An array of ingredients made from palm oil | [optional] 
**ingredient_list** | **list[str]** | An array of this item&#x27;s ingredients | [optional] 
**has_english_ingredients** | **bool** | A boolean indicating if we have English ingredients for this item | [optional] 
**minerals** | **list[str]** | An array of minerals that this item contains | [optional] 
**traces** | **list[str]** | An array of trace ingredients that may be found in this item | [optional] 
**vitamins** | **list[str]** | An array of vitamins that are found in this item | [optional] 
**description** | **str** | A description of this item | [optional] 
**keywords** | **list[str]** | An array of keywords that can be used to describe this item | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

