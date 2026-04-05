# 🌤️ Weather AI API

## Thông tin sinh viên
- **Họ tên:** Nguyễn Lê Anh Kiên
- **MSSV:** 24120196
- **Lớp:** 24CTT3

---

## 🤖 Model sử dụng
- **Tên model:** `sshleifer/distilbart-cnn-12-6`
- **Link model:** https://huggingface.co/sshleifer/distilbart-cnn-12-6
- **Loại:** Summarization (Tóm tắt văn bản)

---

## 📖 Mô tả hệ thống
Hệ thống API dự báo thời tiết kết hợp AI:
1. Nhận tên thành phố từ người dùng
2. Gọi **OpenWeatherMap API** để lấy dữ liệu thời tiết thực tế
3. Đưa dữ liệu vào mô hình AI **DistilBART** để sinh mô tả tự nhiên
4. Trả về kết quả dạng JSON

---

## ⚙️ Hướng dẫn cài đặt

```bash
pip install -r requirements.txt
```

Tạo file `.env` trong thư mục dự án:
```
OPENWEATHER_API_KEY=your_api_key_here
```

---

## 🚀 Hướng dẫn chạy chương trình

```bash
uvicorn main:app --reload
```

Server chạy tại: http://127.0.0.1:8000
Test API tại: http://127.0.0.1:8000/docs

---

## 📡 Hướng dẫn gọi API

### GET /
```
GET http://127.0.0.1:8000/
```
**Response:**
```json
{
  "message": "Chào mừng đến với Weather AI API!",
  "description": "API dự báo thời tiết kết hợp mô hình AI từ Hugging Face",
  "model": "sshleifer/distilbart-cnn-12-6"
}
```

---

### GET /health
```
GET http://127.0.0.1:8000/health
```
**Response:**
```json
{
  "status": "ok",
  "model_loaded": true,
  "openweather_key_set": true
}
```

---

### POST /predict
```
POST http://127.0.0.1:8000/predict
Content-Type: application/json

{
  "city": "Ho Chi Minh City"
}
```
**Response:**
```json
{
  "city": "Ho Chi Minh City",
  "country": "VN",
  "weather_data": {
    "temperature_celsius": 32.5,
    "feels_like_celsius": 36.0,
    "humidity_percent": 80,
    "description": "overcast clouds",
    "wind_speed_ms": 4.5
  },
  "ai_summary": "Ho Chi Minh City is hot and humid with overcast clouds. Temperature is 32.5 degrees Celsius with 80% humidity."
}
```

---

## 🎬 Video Demo
[Điền link video YouTube/Drive vào đây]