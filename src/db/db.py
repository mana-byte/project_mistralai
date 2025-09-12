import sqlite3
from .init_db import DB_PATH


def connect_db():
    try:
        connection = sqlite3.connect(DB_PATH)
        cur = connection.cursor()
    except Exception as e:
        print(e)
        return None, None
    return connection, cur


# return list of tuples (name, average_calories, times_eaten)
def get_all_foods_eaten():
    connection, cur = connect_db()
    if connection:
        result = cur.execute(
            """SELECT 
                    Foods.name, Foods.average_calories, COUNT(EatenFood.food_id) AS times_eaten
                    FROM
                    Foods
                    LEFT JOIN
                    EatenFood ON EatenFood.food_id = Foods.id
                    GROUP BY
                    Foods.id, Foods.name, Foods.average_calories
                    """
        )
        results = result.fetchall()  # cannot operate on close connection
        connection.close()
        return results


# return int or None
def get_avg_calories_by_name(name):
    connection, cur = connect_db()
    if connection:
        result = cur.execute(
            """SELECT 
                    Foods.average_calories AS avg_calories
                    FROM
                    Foods
                    WHERE
                    Foods.name = ?
                    """,
            (name,),
        )
        results = result.fetchone()
        connection.close()
        return {"average_calories": results[0]} if results else None


# return list of tuples (food_name, eaten_food_id)
def get_eatan_foods_from_past_n_meals(n):
    connection, cur = connect_db()
    if connection:
        result = cur.execute(
            """SELECT 
                    EatenFood.id, Foods.name 
                    FROM
                    Foods
                    JOIN
                    EatenFood ON EatenFood.food_id = Foods.id
                    ORDER BY
                    EatenFood.id DESC
                    LIMIT ?
                    """,
            (n,),
        )
        results = result.fetchall()  # cannot operate on close connection
        connection.close()
        return results


# return list of tuples (eaten_food_id, food_name, calories) + ("Total", total_calories)
def get_eaten_foods_calories_from_past_n_meals(n):
    connection, cur = connect_db()
    if connection:
        result = cur.execute(
            """SELECT 
                    EatenFood.id, Foods.name, EatenFood.calories
                    FROM
                    Foods
                    JOIN
                    EatenFood ON EatenFood.food_id = Foods.id
                    ORDER BY
                    EatenFood.id DESC
                    LIMIT ?
                    """,
            (n,),
        )
        results = result.fetchall()  # cannot operate on close connection
        connection.close()

        if results is None:
            return None
        total_calories = 0
        for r in results:
            total_calories += r[2]
        results.append(("Total", total_calories))

        return results


# return int
def get_number_of_times_food_eaten_by_name(name):
    connection, cur = connect_db()
    if connection:
        result = cur.execute(
            """SELECT 
                    COUNT(EatenFood.food_id) AS times_eaten
                    FROM
                    Foods
                    LEFT JOIN
                    EatenFood ON EatenFood.food_id = Foods.id
                    WHERE
                    Foods.name = ?
                    GROUP BY
                    Foods.id, Foods.name
                    """,
            (name,),
        )
        results = result.fetchone()  # cannot operate on close connection
        connection.close()
        return {"times": results[0]} if results else 0


# return True if success, False if fail
def post_food_eaten(name, calories, ingredients=""):
    connection, cur = connect_db()
    if connection:
        try:
            result = cur.execute(
                """SELECT 
                        Foods.id
                        FROM
                        Foods
                        WHERE
                        Foods.name = ?
                        """,
                (name,),
            )
            food = result.fetchone()
            if food is None:
                cur.execute(
                    """INSERT INTO Foods (name, average_calories) VALUES (?, ?)""",
                    (name, calories),
                )
            food_id = food[0] if food else cur.lastrowid

            cur.execute(
                """INSERT INTO EatenFood (food_id, calories, ingredients) VALUES (?, ?, ?)""",
                (food_id, calories, ingredients),
            )
            connection.commit()
        except Exception as e:
            print(e)
            connection.close()
            return False
        connection.close()
        return True
    return False


if __name__ == "__main__":
    print(get_all_foods_eaten())
    print(get_avg_calories_by_name("Apple"))
    print(get_eatan_foods_from_past_n_meals(3))
    print(get_eaten_foods_calories_from_past_n_meals(3))
    print(get_number_of_times_food_eaten_by_name("Banana"))
