# BrandedFoodObjectItems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **str** | EAN/UPC barcode | [optional] 
**name** | **str** | Item name as provided by brand owner or as shown on packaging | [optional] 
**brand** | **str** | The brand name that owns this item | [optional] 
**ingredients** | [**BrandedFoodObjectIngredients**](BrandedFoodObjectIngredients.md) |  | [optional] 
**package** | [**BrandedFoodObjectPackage**](BrandedFoodObjectPackage.md) |  | [optional] 
**serving** | [**BrandedFoodObjectServing**](BrandedFoodObjectServing.md) |  | [optional] 
**categories** | **list[str]** |  | [optional] 
**nutrients** | [**BrandedFoodObjectNutrients**](BrandedFoodObjectNutrients.md) |  | [optional] 
**calorie_conversion_factor** | [**BrandedFoodObjectCalorieConversionFactor**](BrandedFoodObjectCalorieConversionFactor.md) |  | [optional] 
**protein_conversion_factor** | **float** | The multiplication factor used to calculate protein from nitrogen | [optional] 
**diet_labels** | [**BrandedFoodObjectDietLabels**](BrandedFoodObjectDietLabels.md) |  | [optional] 
**diet_flags** | [**list[BrandedFoodObjectDietFlags]**](BrandedFoodObjectDietFlags.md) | An array of ingredient objects that were flagged while grading this item for compatibility with each diet | [optional] 
**packaging_photos** | [**BrandedFoodObjectPackagingPhotos**](BrandedFoodObjectPackagingPhotos.md) |  | [optional] 
**components** | [**list[BrandedFoodObjectComponents]**](BrandedFoodObjectComponents.md) | An array of objects containing the constituent parts of a food (e.g. bone is a component of meat) | [optional] 
**portions** | [**list[BrandedFoodObjectPortions]**](BrandedFoodObjectPortions.md) | An array of objects containing information on discrete amounts of a food found in this item | [optional] 
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
**common_name** | **str** | Common names associated with this item. These generally clarify what the item is (e.g. when the brand name is \&quot;BRAND&#x27;s Spicy Enchilada\&quot; the common name may be \&quot;Chicken enchilada\&quot;) | [optional] 
**description** | **str** | A description of this item | [optional] 
**keywords** | **list[str]** | An array of keywords that can be used to describe this item | [optional] 
**footnote** | **str** | Comments on any unusual aspects of this item. Examples might include unusual aspects of the food overall. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

