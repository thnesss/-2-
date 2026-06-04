import pytest
from main import Ingredient

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