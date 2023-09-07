from flask import Flask, jsonify, request
from datetime import datetime
import time
app = Flask(__name__)

@app.route('/api', methods = ['GET'])
def index():
    slack = request.args.get("slack_name")
    stack = request.args.get("track")
    res =  {"slack_name":slack,
            "current_day":datetime.now().strftime('%A'),
            "utc_time":datetime.utcnow().isoformat(),
            "track":stack,
            "github_file_url":"https://github.com/DollyPy/01_endpoint/blob/main/main.py",
            "github_repo_url":"https://github.com/DollyPy/01_endpoint",
            "status_code":200
            }
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
