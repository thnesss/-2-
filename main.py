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