from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_url_path='')

LOG_FILE = '/home/d/Documents/ping_project.txt'

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/data')
def get_data():
    data = {
        'google.com': 0,
        'msn.com': 0,
        'failures': 0
    }

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            lines = f.readlines()
            for line in lines[-100:]:  # Analyze last 100 entries
                if 'google.com' in line:
                    if 'SUCCESS' in line:
                        data['google.com'] += 1
                    else:
                        data['failures'] += 1
                elif 'msn.com' in line:
                    if 'SUCCESS' in line:
                        data['msn.com'] += 1
                    else:
                        data['failures'] += 1
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
