from flask import Flask, jsonify, request
import covid19_news

#TODO: Refactor location setting instruction



app = Flask(__name__)

@app.route("/updates")
def updates():
    """
    Gets recent news updates for coronavirus
    """
    data = { "test": "IN news()" }
    location = request.args.get("location")
    data["updates"] = covid19_news.recent_news(location)

    return jsonify(data)


@app.route("/tweets")
def tweets():
    """
    Gets recent tweets about coronavirus
    """
    data = { "test": "IN tweets()" }
    location = request.args.get("location")

    return jsonify(data)


@app.route("/videos")
def videos():
    """
    Gets recent videos about coronavirus
    """
    data = { "test": "IN videos" }
    location = request.args.get("location")

    return jsonify(data)




if __name__ == "__main__":
    app.run()
