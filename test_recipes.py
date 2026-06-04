import pytest
from main import Ingredient, Recipe, ShoppingList

def test_ing1():
    ing= Ingredient("Мука", 500.0, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit =="г"

def test_ing2():
    ing= Ingredient("Мука", 500.0, "г")
    assert str(ing) == "Мука: 500.0 г"
    ing2 = Ingredient("Яйца", 3.0, "шт")
    assert str(ing2) == "Яйца: 3.0 шт"

def test_ing3():
    ing1 = Ingredient("Мука",500.0, "г")
    ing2 = Ingredient("Мука", 1000.0, "г")
    assert ing1 == ing2

def test_ing4():
    ing1 = Ingredient("Мука", 500.0, "г")
    ing2= Ingredient("Сахар", 500.0, "г")
    assert ing1!= ing2

def test_ing5():
    ing1 = Ingredient("Мука", 500.0, "г")
    ing2 = Ingredient("Мука", 500.0, "кг")
    assert ing1 != ing2

def test_recipe1():
    ing= [Ingredient("Мука", 500, "г"), Ingredient("Яйца", 3, "шт")]
    rec = Recipe("Блины", ing)
    assert rec.title == "Блины"
    assert len(rec.ingredients)== 2
    assert rec.ingredients[0].name== "Мука"
    assert rec.ingredients[1].name == "Яйца"

def test_recipe2():
    rec= Recipe("Блины", [])
    ing= Ingredient("Мука", 500, "г")
    rec.add_ingredient(ing)
    assert len(rec.ingredients)== 1
    assert rec.ingredients[0].quantity == 500

def test_recipe3():
    rec= Recipe("Блины", [Ingredient("Мука", 500, "г")])
    ing= Ingredient("Мука",300, "г")
    rec.add_ingredient(ing)
    assert len(rec.ingredients) == 1
    assert rec.ingredients[0].quantity == 800

def test_recipe4():
    rec= Recipe("Блины", [Ingredient("Мука", 500, "г")])
    sc= rec.scale(2)
    assert sc is not rec
    assert rec.ingredients[0].quantity== 500
    assert sc.ingredients[0].quantity == 1000

def test_recipe5():
    rec= Recipe("Блины", [
        Ingredient("Мука", 500, "г"),
        Ingredient("Яйца", 3, "шт")
    ])
    sc= rec.scale(2.5)
    assert sc.ingredients[0].quantity== 1250
    assert sc.ingredients[1].quantity == 7.5

def test_recipe6():
    rec= Recipe("Блины", [Ingredient("Мука",500,"г")])
    with pytest.raises(ValueError):
        rec.scale(-5)

def test_recipe7():
    rec= Recipe("Блины", [
        Ingredient("Мука", 500, "г"),
        Ingredient("Яйца", 3, "шт"),
        Ingredient("Молоко",250,"мл")
    ])
    assert len(rec)== 3



def test_shoppinglist1():
    rec= Recipe("Блины", [Ingredient("Мука", 500, "г"),Ingredient("Яйца",3, "шт")])
    shlist = ShoppingList()
    shlist.add_recipe(rec,2)
    assert len(shlist._items) == 2
    assert shlist._items[0][0].name== "Мука"
    assert shlist._items[0][0].quantity== 1000
    assert shlist._items[0][1] == "Блины"
    assert shlist._items[1][0].name =="Яйца"
    assert shlist._items[1][0].quantity == 6
    assert shlist._items[1][1]== "Блины"

def test_shoppinglist2():
    rec= Recipe("Блины", [Ingredient("Мука", 500, "г")])
    shlist = ShoppingList()
    with pytest.raises(ValueError,match="Количество порций должно быть положительным"):
        shlist.add_recipe(rec,0)
    with pytest.raises(ValueError, match="Количество порций должно быть положительным"):
        shlist.add_recipe(rec,-5)

def test_shoppinglist3():
    rec1= Recipe("Блины", [Ingredient("Мука",500,"г")])
    rec2= Recipe("Оладьи", [Ingredient("Мука",300,"г")])
    shlist = ShoppingList()
    shlist.add_recipe(rec1, 1)
    shlist.add_recipe(rec2, 1)
    assert len(shlist._items) == 2
    shlist.remove_recipe("Блины")
    assert len(shlist._items) == 1
    assert shlist._items[0][1] == "Оладьи"

def test_shoppinglist4():
    rec= Recipe("Блины", [Ingredient("Мука", 500, "г")])
    shlist= ShoppingList()
    shlist.add_recipe(rec,1)
    shlist.remove_recipe("Несуществующий рецепт")
    assert len(shlist._items)== 1

def test_shoppinglist5():
    rec1= Recipe("Блины",[Ingredient("Мука", 500, "г")])
    rec2= Recipe("Оладьи", [Ingredient("Мука", 300, "г")])
    shlist = ShoppingList()
    shlist.add_recipe(rec1, 1)
    shlist.add_recipe(rec2, 1)
    res= shlist.get_list()
    assert len(res)== 1
    assert res[0].name== "Мука"
    assert res[0].quantity == 800
    assert res[0].unit == "г"

def test_shoppinglist6():
    rec= Recipe("Сборный",[
        Ingredient("Яйца", 3, "шт"),
        Ingredient("Мука", 500, "г"),
        Ingredient("Сахар", 200, "г")
    ])
    shlist = ShoppingList()
    shlist.add_recipe(rec, 1)
    res = shlist.get_list()
    assert res[0].name =="Мука"
    assert res[1].name == "Сахар"
    assert res[2].name== "Яйца"

def test_shoppinglist7():
    rec1= Recipe("Блины",[Ingredient("Мука",500, "г")])
    rec2 = Recipe("Оладьи", [Ingredient("Яйца", 3, "шт")])
    l1 = ShoppingList()
    l2 = ShoppingList()
    l1.add_recipe(rec1,1)
    l2.add_recipe(rec2, 1)
    c= l1+ l2
    assert len(c._items)== 2
    assert c._items[0][0].name== "Мука"
    assert c._items[1][0].name == "Яйца"
    assert len(l1._items)== 1
    assert len(l2._items)== 1