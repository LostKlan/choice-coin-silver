import tweepy
from decouple import config

api_key = config("API_KEY")
api_secret_key = config("API_SECRET_KEY")
access_key = config("ACCESS_KEY")
access_secret_key = config("ACCESS_SECRET_KEY")

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_key, access_secret_key)
api = tweepy.API(auth, wait_on_rate_limit=True)


SOCIAL_MEDIA_START = "The voting procedure has started successfully. If you're registered, do join the program to vote at https://127.0.0.1:5000/start"

SOCIAL_MEDIA_SEND = "The voting procedure ended successfully. You can view the results at https://127.0.0.1:5000/end"

RESULT_IMAGE_PATH = "./static/img/plot.png"


def postStartMessage(message):
    api.update_status(message)


def postEndMessage(filename, message):
    api.update_status_with_media(filename=filename, status=message)
