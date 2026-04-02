from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()

app = FastAPI(
    title="Weather AI API",
    description="Dự báo thời tiết kết hợp AI (Hugging Face)",
    version="1.0.0"
)

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Load model Hugging Face
print("Đang load model AI...")
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
print("Model đã sẵn sàng!")


class WeatherRequest(BaseModel):
    city: str


@app.get("/")
def root():
    return {
        "message": "Chào mừng đến với Weather AI API!",
        "description": "API dự báo thời tiết kết hợp mô hình AI từ Hugging Face",
        "model": "distilbert-base-uncased-finetuned-sst-2-english",
        "endpoints": {
            "GET /": "Thông tin API",
            "GET /health": "Kiểm tra trạng thái hệ thống",
            "POST /predict": "Dự báo thời tiết theo thành phố"
        }
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_loaded": classifier is not None,
        "openweather_key_set": OPENWEATHER_API_KEY is not None
    }


@app.post("/predict")
def predict(request: WeatherRequest):
    city = request.city.strip()

    if not city:
        raise HTTPException(status_code=400, detail="Tên thành phố không được để trống!")

    # Gọi OpenWeatherMap API
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "en"
    }

    weather_response = requests.get(url, params=params)

    if weather_response.status_code == 404:
        raise HTTPException(status_code=404, detail=f"Không tìm thấy thành phố: {city}")
    elif weather_response.status_code == 401:
        raise HTTPException(status_code=401, detail="API key OpenWeatherMap không hợp lệ!")
    elif weather_response.status_code != 200:
        raise HTTPException(status_code=500, detail="Lỗi khi gọi OpenWeatherMap API!")

    data = weather_response.json()

    # Lấy thông tin thời tiết
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]
    country = data["sys"]["country"]

    # Ghép thành câu mô tả thời tiết để đưa vào AI phân tích
    text = f"The weather is {description} with temperature {temp} degrees and humidity {humidity} percent."

    # Gọi model AI phân tích cảm xúc thời tiết (tốt/xấu)
    try:
        ai_result = classifier(text)
        sentiment = ai_result[0]["label"]
        score = round(ai_result[0]["score"] * 100, 2)

        if sentiment == "POSITIVE":
            ai_comment = f"Thời tiết hôm nay khá dễ chịu! (Độ tin cậy: {score}%)"
        else:
            ai_comment = f"Thời tiết hôm nay không được tốt lắm. (Độ tin cậy: {score}%)"
    except Exception as e:
        ai_comment = f"Không thể phân tích AI: {str(e)}"

    # Gợi ý theo nhiệt độ
    if temp > 35:
        suggestion = "Trời rất nóng, hạn chế ra ngoài và uống nhiều nước!"
    elif temp > 30:
        suggestion = "Trời nóng, nên mang theo nước và kem chống nắng."
    elif temp > 20:
        suggestion = "Thời tiết dễ chịu, thích hợp cho các hoạt động ngoài trời."
    else:
        suggestion = "Trời mát/lạnh, nhớ mặc áo ấm khi ra ngoài."

    return {
        "city": city,
        "country": country,
        "weather_data": {
            "temperature_celsius": temp,
            "feels_like_celsius": feels_like,
            "humidity_percent": humidity,
            "description": description,
            "wind_speed_ms": wind_speed
        },
        "ai_analysis": {
            "sentiment": sentiment,
            "ai_comment": ai_comment,
            "suggestion": suggestion
        }
    }