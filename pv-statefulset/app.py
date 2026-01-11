from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

app = Flask(__name__)

def get_collection():
    client = MongoClient(
        "mongodb://mongodb:27017/",
        serverSelectionTimeoutMS=2000
    )
    return client["emaildb"]["emails"]

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        collection = get_collection()

        if request.method == "POST":
            email = request.form["email"]
            collection.insert_one({"email": email})
            return redirect("/")

        emails = list(collection.find({}, {"_id": 0}))
        return render_template("index.html", emails=emails, db_up=True)

    except ServerSelectionTimeoutError:
        # MongoDB is down
        return render_template(
            "index.html",
            emails=[],
            db_up=False
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
