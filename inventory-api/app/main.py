from flask import Flask, jsonify

app = Flask(__name__)

servers = [
    {"id": 1, "hostname": "web-prod-01", "ip": "10.0.0.1", "status": "up"},
    {"id": 2, "hostname": "db-prod-01", "ip": "10.0.0.2", "status": "down"},
]


@app.route("/api/v1/health", methods=["GET"])
def health():
    return jsonify({"status": "OK", "version": "1.0"}), 200


@app.route("/api/v1/servers", methods=["GET"])
def get_servers():
    return jsonify({"servers": servers, "count": len(servers)}), 200


@app.route("/api/v1/servers/<int:server_id>", methods=["GET"])
def get_server_by_id(server_id):
    for server in servers:
        if server["id"] == server_id:
            return jsonify(server), 200
    return jsonify({"error": "Server not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)