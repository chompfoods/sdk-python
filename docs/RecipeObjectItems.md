# RecipeObjectItems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique recipe ID | [optional] 
**title** | **str** | Recipe title | [optional] 
**meta** | [**RecipeObjectMeta**](RecipeObjectMeta.md) |  | [optional] 
**categories** | **list[str]** |  | [optional] 
**author** | **str** | The author of this recipe. You must attribute this author when displaying this recipe. | [optional] 
**keywords** | **list[str]** |  | [optional] 
**topics** | **list[str]** |  | [optional] 
**attributes** | [**RecipeObjectAttributes**](RecipeObjectAttributes.md) |  | [optional] 
**ingredients** | [**list[RecipeObjectIngredients]**](RecipeObjectIngredients.md) | An array containing this recipe&#x27;s ingredients | [optional] 
**base_ingredients** | **list[str]** |  | [optional] 
**nutrients** | [**RecipeObjectNutrients**](RecipeObjectNutrients.md) |  | [optional] 
**diabetic_exchanges** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

