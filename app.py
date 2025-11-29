from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(message="Hello from Dockerized app!", status="OK")

if __name__ == "__main__":
    # nasłuch na wszystkich interfejsach, port 5000 (łatwo potem zmapować w Dockerze)
    app.run(host="0.0.0.0", port=5000)
