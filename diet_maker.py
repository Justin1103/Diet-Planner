from diet_planner import db
from sqlalchemy import func
from random import randint, random, choice, sample
from models import *

actions = [
    [
        "Posiekaj {}.",
        "Potnij na plasterki {}.",
        "Potnij w kostkę {}.",
        "Włóż {} do miski.",
        "Podgrzej na patelni {}.",
        "Odgrzej {} w mikrofali.",
        "Włóż {} do garnka.",
        "Oczyść {}.",
        "Piecz {}.",
        "Zmiel {}.",
        "Poszatkuj {}.",
        "Zetrzyj {} do garnka.",
        "Umyj {}.",
        "Schłódź {}.",
        "{} umyj i osusz papierowym ręcznikiem.",
        "Przekrój {} wzdłuż i delikatnie rozbij tłuczkiem.",
        "Obierz {}.",
        "{} pokrój w ćwiartki i podsmaż na patelni.",
        "Rozpuść {}.",
        "Ubij {}",
    ],
    [
        "Wymieszaj {} z {}.",
        "Zmiksuj {} z {}.",
        "Dodaj {} do {} i dokładnie wymieszaj.",
        "Na patelni podsmaż {} i {}.",
        "{} połącz z {}.",
        "Obtocz {} w {}.",
        "{} ponacinaj nożem i w powstałe kieszonki wsuń {}.",
        "{} oraz {} przepuść przez maszynkę do mielenia.",
        "Połóż {} na {}.",
        "{} pomieszaj z roztartym na miazgę {}",
        "Wyłóż {} na miskę i pokryj {}.",
        "Zwiń {} w rulon i do środka włóż {}.",
        "{} nałóż na {}, następnie zroluj."
    ],
    [
        "Wymieszaj w misce {}, {} oraz {}.",
        "Zmiksuj ze sobą {}, {} i {}.",
        "Połącz {} w dużej misce z {} i {}.",
        "Przygotuj aromatyczną marynatę mieszając {} z {} i natrzyj nią {}.",
    ]
]


def create_meal(calories):
    ingredients_count = randint(3, 5)
    ingredients = Product.query.order_by(func.random()).limit(ingredients_count).all()
    amounts = {}
    for ingredient in ingredients:
        if ingredients_count > 1:
            ingredient_calories = int((calories / ingredients_count) * (1 - (random() / 2) - 0.25))
            calories -= ingredient_calories
            ingredients_count -= 1
        else:
            ingredient_calories = calories
        amounts[ingredient.name] = [ingredient_calories, int((ingredient_calories * 100) / ingredient.calories)]
    return amounts


def create_recipe(calories):
    amounts = create_meal(calories)
    names = [name for name, _ in amounts.items()]
    steps = randint(len(amounts), len(amounts) + 2)
    instructions = []
    for step in range(steps):
        products_to_use = randint(1, 3)
        action = choice(actions[products_to_use - 1])
        instruction = action.format(*sample(names, products_to_use))
        instructions.append(instruction)
    return amounts, instructions
