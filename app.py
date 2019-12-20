from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def get_version():
    response = jsonify({'version': '1'})
    response.status_code = 200
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10347)
