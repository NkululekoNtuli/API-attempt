from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    #mock data to be retrived by the API becaues it is not connected to a database as yet.
    user_data = {
        "user_id": user_id,
        "name": "Nkululeko",
        "email": "Mzamo@gmail.com"
    }

    extra = request.args.get("extra")#making a get request while adding A key and value?
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200#defualt for succes

@app.route("/create-user", methods=["POST"])#making post request(requires an API tester)
def creat_user():
    data = request.get_json()

    return jsonify(data), 201#??


if __name__ == '__main__':
    app.run(debug=True)