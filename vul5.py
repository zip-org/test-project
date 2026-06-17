from flask import Flask, g, jsonify, request

app = Flask(__name__)

# Mock database of invoices
INVOICES_DB = {
    "101": {"owner_id": "user_alice", "amount": 1500.00, "status": "Pending"},
    "102": {"owner_id": "user_bob", "amount": 45.00, "status": "Paid"},
}


@app.before_request
def mock_authentication():
    # Simulate that Bob is logged in
    g.current_user_id = "user_bob"


### VULNERABLE ROUTE (IDOR on Update) ###
@app.route("/api/v1/invoice/update", methods=["POST"])
def update_invoice():
    """
    VULNERABILITY: The app trusts the 'invoice_id' provided by the client
    and updates the database without verifying if the logged-in user
    actually owns that invoice.
    """
    data = request.get_json()
    invoice_id = data.get("invoice_id")
    new_amount = data.get("amount")

    invoice = INVOICES_DB.get(invoice_id)
    if not invoice:
        return jsonify({"error": "Invoice not found"}), 404

    # IDOR: Modifying the resource blindly based on the ID provided
    invoice["amount"] = new_amount
    return jsonify({"message": f"Invoice {invoice_id} updated successfully!"}), 200


if __name__ == "__main__":
    app.run(debug=True)
