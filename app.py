from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    environment = os.getenv('ENVIRONMENT_NAME', 'Unknown')
    return f"<h1>Environment: {environment}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
