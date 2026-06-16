from flask import Flask, g, jsonify, request

app = Flask(__name__)

# Mock database
USERS_DB = {
    "1": {"username": "alice", "email": "alice@example.com", "balance": "$5000"},
    "2": {"username": "bob", "email": "bob@example.com", "balance": "$20"},
    "3": {"username": "charlie", "email": "charlie@example.com", "balance": "$150"},
}


# Mock middleware to simulate a logged-in user
@app.before_request
def mock_authentication():
    # Let's assume Bob (user_id "2") is the one logged in and sending this request
    g.current_user_id = "2"


### VULNERABLE ROUTE (IDOR) ###
@app.route("/api/v1/account/<user_id>", methods=["GET"])
def get_account_details(user_id):
    """
    VULNERABILITY: The code checks if the user exists in the database,
    but it NEVER verifies if the logged-in user (g.current_user_id)
    has authorization to view the requested 'user_id' data.
    """
    user_data = USERS_DB.get(user_id)

    if not user_data:
        return jsonify({"error": "User not found"}), 404

    # Returns the data blindly based solely on the URL parameter
    return jsonify(user_data), 200


if __name__ == "__main__":
    app.run(debug=True)
