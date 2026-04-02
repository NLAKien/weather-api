import requests

BASE_URL = "http://127.0.0.1:8000"

# Test GET /
print("=== Test GET / ===")
res = requests.get(f"{BASE_URL}/")
print(res.json())
print()

# Test GET /health
print("=== Test GET /health ===")
res = requests.get(f"{BASE_URL}/health")
print(res.json())
print()

# Test POST /predict - Thành phố 1
print("=== Test POST /predict - Ho Chi Minh City ===")
res = requests.post(f"{BASE_URL}/predict", json={"city": "Ho Chi Minh City"})
print(res.json())
print()

# Test POST /predict - Thành phố 2
print("=== Test POST /predict - Hanoi ===")
res = requests.post(f"{BASE_URL}/predict", json={"city": "Hanoi"})
print(res.json())
print()

# Test lỗi - thành phố không tồn tại
print("=== Test lỗi - thành phố không tồn tại ===")
res = requests.post(f"{BASE_URL}/predict", json={"city": "abcxyznotacity"})
print(res.status_code, res.json())