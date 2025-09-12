import sqlite3

try:
    connection = sqlite3.connect("food.db")
    try:
        cur = connection.cursor()
        create_eaten_food_querry = """
            CREATE TABLE IF NOT EXISTS EatenFood (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    food_id INTEGER NOT NULL,
                    calories INTEGER NOT NULL,
                    ingredients TEXT NOT NULL,
                    FOREIGN KEY(food_id) REFERENCES Foods(id)
                    );
        """
        create_food_querry = """
            CREATE TABLE IF NOT EXISTS Foods (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    average_calories INTEGER NOT NULL
                    );
        """

        cur.execute(create_food_querry)
        cur.execute(create_eaten_food_querry)

        connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()
except Exception as e:
    print(e)
