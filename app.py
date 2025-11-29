from flask import Flask, jsonify
import redis

app = Flask(__name__)

# Połączenie z usługą Redis o nazwie 'redis' (zdefiniujemy ją w docker-compose)
r = redis.Redis(host="redis", port=6379, db=0)

@app.route("/")
def hello():
    visits = r.incr("visits")  # inkrementacja licznika odwiedzin
    return jsonify(
        message="Hello from multi-container Docker Compose app!",
        visits=int(visits)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
