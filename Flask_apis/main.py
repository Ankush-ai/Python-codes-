from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/get-user/<int:user_id>")
def get_user(user_id):
    try:
        # Simulating fetching user data from a database or other source
        user_data = {
            "user_id": user_id,
            "name": "Ankush Srivastava",
            "email": "ankushsri007@gmail.com"
        }

        # Retrieve 'extra' parameter from query string
        extra = request.args.get("extra", None)
        if extra:
            user_data["extra"] = extra

        return jsonify(user_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/create_user",methods=["POST"])
def create_user():
    data=request.get_json()
    return jsonify(data),201
  

if __name__ == "__main__":
    app.run(debug=True)
