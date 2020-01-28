# IngredientObjectItems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Item name as provided by brand owner or as shown on packaging | [optional] 
**categories** | **list[str]** |  | [optional] 
**nutrients** | [**list[IngredientObjectNutrients]**](IngredientObjectNutrients.md) | An array containing nutrient informatio objects for this food item | [optional] 
**calorie_conversion_factor** | [**IngredientObjectCalorieConversionFactor**](IngredientObjectCalorieConversionFactor.md) |  | [optional] 
**protein_conversion_factor** | **float** | The multiplication factor used to calculate protein from nitrogen | [optional] 
**components** | [**list[IngredientObjectComponents]**](IngredientObjectComponents.md) | An array of objects containing the constituent parts of a food (e.g. bone is a component of meat) | [optional] 
**portions** | [**list[IngredientObjectPortions]**](IngredientObjectPortions.md) | An array of objects containing information on discrete amounts of a food found in this item | [optional] 
**common_name** | **str** | Common name associated with this item. These generally clarify what the item is (e.g. when the brand name is \&quot;BRAND&#x27;s Spicy Enchilada\&quot; the common name may be \&quot;Chicken enchilada\&quot;) | [optional] 
**footnote** | **str** | Comments on any unusual aspects of this item. Examples might include unusual aspects of the food overall. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

