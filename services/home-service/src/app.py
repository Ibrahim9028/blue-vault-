



from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({
        "service": "Blue Vault Home Service",
        "status": "UP",
        "message": "Welcome to Blue Vault"
    })


@app.get("/health")
def health():
    return jsonify({
        "status": "UP"
    })


@app.get("/live")
def live():
    return jsonify({
        "status": "ALIVE"
    })


@app.get("/ready")
def ready():
    return jsonify({
        "status": "READY"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
