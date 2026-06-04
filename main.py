class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self.quantity = quantity 
        self.unit = unit
    
    @property
    def quantity(self) -> float:
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity=value
    
    def __str__(self) -> str:
        return f"{self.name}: {self.quantity} {self.unit}"
    
    def __repr__(self) -> str:
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Ingredient):
            return NotImplemented
        return self.name==other.name and self.unit==other.unit
    

class Recipe:
    def __init__(self, title: str, ingredients: list=None):
        self.title = title
        self.ingredients = ingredients.copy() if ingredients else []
    
    def add_ingredient(self, ingredient: Ingredient):
        for e in self.ingredients:
            if e == ingredient:
                e.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)
    
    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        try:
            return float(ratio)> 0
        except (TypeError, ValueError):
            return False
    
    def scale(self, ratio: float) -> 'Recipe':
        if not self.is_valid_ratio(ratio):
            raise ValueError(f"Коэффициент масштабирования должен быть положительным числом, получено: {ratio}")
        ratio = float(ratio)
        list =[]
        for ing in self.ingredients:
            list.append(Ingredient(ing.name, ing.quantity * ratio, ing.unit))
        return Recipe(self.title, list)
    
    def __len__(self) -> int:
        return len(self.ingredients)
    
    def __str__(self) -> str:
        str = "\n".join(f"  - {ing}" for ing in self.ingredients)
        return f"{self.title}:\n{str}"
    
class ShoppingList:
    def __init__(self):
        self._items=[]
    
    def add_recipe(self, recipe: Recipe, portions: float):
        if portions<=0:
            raise ValueError("Количество порций должно быть положительным")
        nrecipe= recipe.scale(portions)
        for ingredient in nrecipe.ingredients:
            self._items.append((ingredient, recipe.title))
    
    def remove_recipe(self, title: str):
        self._items = [item for item in self._items if item[1]!=title]
    
    def get_list(self):
        sum= {}
        for i, b in self._items:
            key = (i.name, i.unit)
            if key in sum:
                sum[key] += i.quantity
            else:
                sum[key] = i .quantity
        result = [Ingredient(name, quantity, unit) for (name, unit), quantity in sum.items()]
        result.sort(key=lambda x: x.name)
        return result
    
    def __add__(self, other: 'ShoppingList'):
        new_list = ShoppingList()
        new_list._items = self._items.copy() + other._items.copy()
        return new_list
    

class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: list = None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type
    
    def scale(self, ratio: float):
        nrecipe=super().scale(ratio)
        return DietaryRecipe(nrecipe.title, self.diet_type,nrecipe.ingredients)
    
    def __str__(self) -> str:
        return f"[{self.diet_type}] {self.title}:\n"+"\n".join(f"  - {ing}" for ing in self.ingredients)