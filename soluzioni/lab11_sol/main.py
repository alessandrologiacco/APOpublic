from diet.food import Food
from diet.elements import Menu, Recipe


def main():
    # ---------- R1 ----------
    # creo classe food
    food = Food()

    # creo raw materials
    food.define_raw_material("Sugar", 400, 0, 100, 0)
    food.define_raw_material("Mais", 70, 2.7, 12, 1.3)
    food.define_raw_material("Pasta", 350, 12, 72.2, 1.5)
    food.define_raw_material("Olio di oliva", 900, 0, 0, 100)
    food.define_raw_material("Nutella", 530, 6.8, 56, 31)
    food.define_raw_material("Passata di Pomodoro", 36, 2, 5, 0)

    # stampo nomi dei raw material creati
    # ['Mais', 'Nutella', 'Olio di oliva', 'Passata di Pomodoro', 'Pasta', 'Sugar'] (ordine è importante)
    print([mat.name for mat in food.raw_materials])

    # ottengo raw material e stampo proprietà
    raw_mat = food.get_raw_material("Nutella")
    print("Name: {}, Calories: {}, Proteins: {}, Carbs: {}, Fat: {}, per100: {}".format(
            raw_mat.name,
            raw_mat.calories,
            raw_mat.proteins,
            raw_mat.carbs,
            raw_mat.fats,
            raw_mat.per100g
        )
    )   # Name: Nutella, Calories: 530, Proteins: 6.8, Carbs: 56, Fat: 31, per100: True

    # testo eccezione
    food2 = Food()
    food2.define_raw_material("ciao", 1, 1, 1, 1)
    try:
        food2.define_raw_material("ciao", 2, 2, 2, 2)
    except ValueError:
        print("Duplicate raw material correctly detected")  # Duplicate raw material correctly detected

    # --------- R2 -----------
    # creo un prodotto
    food.define_product("Merendina", 150, 4.5, 9.4, 5.3)
    food.define_product("Crackers", 111, 2.6, 17.2, 3.5)

    # stampo nomi dei prodotti creati
    print([prod.name for prod in food.products])    # ['Crackers', 'Merendina'] (ordine è importante)

    # ottengo raw material e stampo proprietà
    prod = food.get_product("Merendina")
    print("Name: {}, Calories: {}, Proteins: {}, Carbs: {}, Fat: {}, per100: {}".format(
            prod.name,
            prod.calories,
            prod.proteins,
            prod.carbs,
            prod.fats,
            prod.per100g
        )
    )   # Name: Merendina, Calories: 150, Proteins: 4.5, Carbs: 9.4, Fat: 5.3, per100: False

    # testo eccezione
    food2 = Food()
    food2.define_product("ciao", 1, 1, 1, 1)
    try:
        food2.define_product("ciao", 2, 2, 2, 2)
    except ValueError:
        print("Duplicate product correctly detected")   # Duplicate product correctly detected

    # --------- R3 -----------
    # creo una ricetta
    r1 = food.create_recipe("Pasta al Pomodoro")
    r2 = food.create_recipe("Zabaglione")

    # uso il fatto che add_ingredient ritorni se stesso per concatenare aggiunte ingredienti
    r1.add_ingredient("Pasta", 70).add_ingredient("Passata di Pomodoro", 30).add_ingredient("Olio di oliva", 5)

    # controllo __repr__
    print(r1)   # Pasta 70.0
                # Passata di Pomodoro 30.0
                # Olio di oliva 5.0

    # ottengo ricette da food
    print([f"{r.name}" for r in food.recipes])  # ['Pasta al Pomodoro', 'Zabaglione']

    # ottengo ricetta da food e stampo proprietà ricetta
    r1 = food.get_recipe("Pasta al Pomodoro")
    print("Name: {}, Calories: {:.1f}, Proteins: {:.1f}, Carbs: {:.1f}, Fats: {:.1f}, per100: {}".format(
            r1.name,
            r1.calories,
            r1.proteins,
            r1.carbs,
            r1.fats,
            r1.per100g
        )
    )   # Name: Pasta al Pomodoro, Calories: 286.5, Proteins: 8.6, Carbs: 49.6, Fats: 5.8, per100: True

    # --------- R5 -----------
    # creo un menù
    menu = food.create_menu("M1");

    # aggiungo ricetta e prodotto al menù usando concatenazione
    menu.add_recipe("Pasta al Pomodoro", 50).add_product("Crackers")

    # stampo le proprietà del menù
    print("Name: {}, Calories: {:.1f}, Proteins: {:.1f}, Carbs: {:.1f}, Fats: {:.1f}, per100: {}".format(
            menu.name,
            menu.calories,
            menu.proteins,
            menu.carbs,
            menu.fats,
            menu.per100g
        )
    )   # Name: M1, Calories: 254.2, Proteins: 6.9, Carbs: 42.0, Fats: 6.4, per100: False


if __name__ == "__main__":
    main()
