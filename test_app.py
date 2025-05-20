import requests
import subprocess
import time

def test_time_route():
    # Запуск приложения в фоне
    proc = subprocess.Popen(["python", "app.py"])
    time.sleep(2)  # Даем время запуску сервера

    response = requests.get("http://localhost:5000/time")
    data = response.json()
    assert data["time"] != 0, "Time should not be zero"

    proc.terminate()

def test_metrics_route():
    proc = subprocess.Popen(["python3", "app.py"])
    time.sleep(2)

    # Вызов /time для увеличения счетчика
    requests.get("http://localhost:5000/time")
    response = requests.get("http://localhost:5000/metrics")
    data = response.json()
    assert data["count"] == 1, "Count should be 1 after one request"

    proc.terminate()
