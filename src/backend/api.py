from fastapi import FastAPI, File
import cv2
import backend.app as app_module
from fastapi.responses import JSONResponse
import db.db as db_module

app = FastAPI()


@app.get("/foods")
async def get_all_foods_eaten():
    try:
        results = db_module.get_all_foods_eaten()
    except Exception as e:
        print("[ERROR] in /foods: " + str(e))
        return JSONResponse(content={"error": "Internal Server Error"}, status_code=500)
    return JSONResponse(content=results, status_code=200)


@app.get("/foods/{name}")
async def get_number_of_times_food_eaten(name: str):
    try:
        results = db_module.get_number_of_times_food_eaten_by_name(name)
    except Exception as e:
        print("[ERROR] in /foods/{name}: " + str(e))
        return JSONResponse(content={"error": "Internal Server Error"}, status_code=500)
    return JSONResponse(content=results, status_code=200)


@app.get("/cal/{name}")
async def get_avg_calories(name: str):
    try:
        results = db_module.get_avg_calories_by_name(name)
    except Exception as e:
        print("[ERROR] in /cal/{name}: " + str(e))
        return JSONResponse(content={"error": "Internal Server Error"}, status_code=500)
    if results is None:
        return JSONResponse(content={"error": "Food not found"}, status_code=404)
    return JSONResponse(content=results, status_code=200)


@app.get("/foods/hist/{past_meals}")
async def item(past_meals: int):
    try:
        results = db_module.get_eatan_foods_from_past_n_meals(past_meals)
    except Exception as e:
        print("[ERROR] in /foods/{past_meals}: " + str(e))
        return JSONResponse(content={"error": "Internal Server Error"}, status_code=500)
    return JSONResponse(content=results, status_code=200)


@app.get("/cal/hist/{past_meals}")
async def get_calories_from_past_meals(past_meals: int):
    try:
        results = db_module.get_eaten_foods_calories_from_past_n_meals(past_meals)
    except Exception as e:
        print("[ERROR] in /cal/{past_meals}: " + str(e))
        return JSONResponse(content={"error": "Internal Server Error"}, status_code=500)
    return JSONResponse(content=results, status_code=200)


@app.post("/foods")
async def analyze_image(file: bytes = File(...)):
    try:
        nparr = np.frombuffer(file, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        results = app_module.inference_img(img)
    except Exception as e:
        print("[ERROR] in /foods POST: " + str(e))
        return JSONResponse(content={"error": "Internal Server Error"}, status_code=500)
    if results == 1:
        return JSONResponse(
            content={"error": "Image processing failed"}, status_code=400
        )
    return JSONResponse(content=results, status_code=200)
