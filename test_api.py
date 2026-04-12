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

print("=== Test POST /predict ===")
print("(Nhập 0 để dừng)")
while True:
    city = input("\nNhập tên thành phố: ")
    if city == "0":
        print("Dừng test!")
        break
    res = requests.post(f"{BASE_URL}/predict", json={"city": city})
    if res.status_code == 404:
        print(f"Lỗi 404: Không tìm thấy thành phố '{city}'!")
    else:
        print(res.json())