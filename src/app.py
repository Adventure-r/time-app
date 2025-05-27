from flask import Flask, jsonify
import time

app = Flask(__name__)

# Счетчик запросов к /time
time_request_count = 0

@app.route('/time', methods=['GET'])
def get_time():
    global time_request_count
    time_request_count += 1
    current_time = int(time.time())
    return jsonify({"time": current_time})

@app.route('/metrics', methods=['GET'])
def get_metrics():
    return jsonify({"count": time_request_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
