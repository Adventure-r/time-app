from flask import Flask
import time

app = Flask(__name__)
request_count = 0

@app.route("/time")
def get_time():
    global request_count
    request_count += 1
    return {"time": int(time.time())}

@app.route("/metrics")
def metrics():
    return {"count": request_count}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
