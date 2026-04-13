# LAB_01: Weather AI API

## Thông tin sinh viên
- **Họ tên:** Nguyễn Lê Anh Kiên
- **MSSV:** 24120196
- **Lớp:** 24CTT3

---

## 🤖 Model sử dụng
- **Tên model:** `sshleifer/distilbart-cnn-12-6`
- **Link model:** https://huggingface.co/sshleifer/distilbart-cnn-12-6
- **Loại:** Summarization (Tóm tắt văn bản -> Đọc mô tả thời tiết và đánh giá)

---

## 📖 Mô tả hệ thống
Hệ thống API dự báo thời tiết kết hợp AI:
1. Nhận tên thành phố từ người dùng
2. Gọi **OpenWeatherMap API** để lấy dữ liệu thời tiết thực tế
3. Đưa dữ liệu vào mô hình AI **DistilBART** để sinh mô tả tự nhiên
4. Trả về kết quả dạng JSON

---

## Hướng dẫn cài đặt

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
    "temperature_celsius": 30.04,
    "feels_like_celsius": 35.14,
    "humidity_percent": 70,
    "description": "light rain",
    "wind_speed_ms": 3.09
  },
  "ai_analysis": {
    "sentiment": "POSITIVE",
    "ai_comment": "Thời tiết hôm nay khá dễ chịu! (Độ tin cậy: 97.81%)",
    "suggestion": "Trời nóng, nên mang theo nước và kem chống nắng."
  }
}
```

---

## 🎬 Video Demo 
(Vì dung lượng quá mức nên không thể up trực tiếp lên github, em xin phép gắn link drive ạ. Comment này nhằm xác nhận buổi thực hành Thầy hướng dẫn em có đi học hihi)
https://drive.google.com/drive/folders/1rMkSqOax1SWFri65wtpc5_-zNTvd10ns?hl=vi