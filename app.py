from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, UAS PKPL!"

if __name__ == "__main__":
    # Port 8080 sering digunakan untuk aplikasi web di dalam container
    app.run(host='0.0.0.0', port=8080)