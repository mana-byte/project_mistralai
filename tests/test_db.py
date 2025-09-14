import db.db as db


def test_get_avg_calories_by_name():
    assert db.get_avg_calories_by_name("NonExistentFood") is None
    assert db.get_avg_calories_by_name("Apple") is not None


def test_get_eatan_foods_from_past_n_meals():
    results = db.get_eatan_foods_from_past_n_meals(1)
    assert results is not None


def test_get_eaten_foods_calories_from_past_n_meals():
    results = db.get_eaten_foods_calories_from_past_n_meals(1)
    assert results is not None


def test_get_all_foods_eaten():
    results = db.get_all_foods_eaten()
    assert results is not None


def test_get_number_of_times_food_eaten_by_name():
    assert db.get_number_of_times_food_eaten_by_name("NonExistentFood")["times"] == 0
    assert db.get_number_of_times_food_eaten_by_name("Apple")["times"] >= 0
