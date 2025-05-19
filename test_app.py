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
    print('End')
