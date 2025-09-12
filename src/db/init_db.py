import sqlite3

DB_PATH = "src/db/food.db"


def create_db():
    try:
        connection = sqlite3.connect(DB_PATH)
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

            cur.execute(
                """INSERT INTO Foods (name, average_calories) VALUES 
                        ('Apple', 52)
                        , ('Banana', 96)
                        , ('Orange', 43)
                        , ('Broccoli', 55)
                        , ('Carrot', 41)
                        """
            )
            cur.execute(
                """
                        INSERT INTO EatenFood (food_id, calories, ingredients) VALUES
                        (1, 50, 'Fresh apple')
                        , (2, 100, 'Ripe banana')
                        , (3, 40, 'Juicy orange')
                        , (1, 55, 'Green apple')
                        , (4, 60, 'Steamed broccoli')
                        , (5, 45, 'Raw carrot')
                        """
            )

            connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    create_db()
