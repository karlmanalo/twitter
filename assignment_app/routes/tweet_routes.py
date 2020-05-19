# assignment_app\routes\tweet_routes.py

from flask import Blueprint, jsonify, request, render_template, redirect
from assignment_app.models import Tweet, db

tweet_routes = Blueprint("tweet_routes", __name__)

@tweet_routes.route("/tweets.json")
def list_tweets():
    tweets = [
        {"id": 1, "tweet": "Tweet 1"},
        {"id": 2, "tweet": "Tweet 2"},
        {"id": 3, "tweet": "Tweet 3"},
    ]
    return jsonify(tweets)

@tweet_routes.route("/tweets")
def list_tweets_assignment():
    tweet_records = Tweet.query.all()
    print(tweet_records)

    return render_template("tweets.html", message="Some tweets:", 
    tweets=tweet_records)

@tweet_routes.route("/tweets/new")
def new_tweet():
    return render_template("new_tweet.html")

@tweet_routes.route("/tweets/create", methods=["POST"])
def create_tweet():
    print("FORM DATA:", dict(request.form))

    new_tweet = Tweet(tweet=request.form["tweet"], 
    username=request.form["username"])
    db.session.add(new_tweet)
    db.session.commit()

    return redirect("/tweets")