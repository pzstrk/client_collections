import twitter
import json
import os

class Twitter():
    def __init__(self, accountId = "default"):
        config_file = open(os.path.join(os.path.dirname(__file__), ".twitter.config.json"), "r")
        config = json.load(config_file)

        if len(accountId) == 0:
            accountId = "default"

        self.__consumer_key = config[accountId]["consumer_key"],
        self.__consumer_secret = config[accountId]["consumer_secret"],
        self.__access_token_key = config[accountId]["access_token_key"],
        self.__access_token_secret = config[accountId]["access_token_secret"]

        self.__client = twitter.Api(
            consumer_key = self.__consumer_key,
            consumer_secret = self.__consumer_secret,
            access_token_key = self.__access_token_key,
            access_token_secret = self.__access_token_secret,
        )

    def post(self, media):
        self.__client.PostUpdate(status='', media=media)

if __name__ == "__main__":
    test_client = Twitter()

