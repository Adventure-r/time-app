def test_metrics_route():
    proc = subprocess.Popen(["python3", "app.py"])
    time.sleep(2)

    # Вызов /time для увеличения счетчика
    requests.get("http://localhost:5000/time")
    response = requests.get("http://localhost:5000/metrics")
    data = response.json()
    assert data["count"] == 1, "Count should be 1 after one request"

    proc.terminate()
