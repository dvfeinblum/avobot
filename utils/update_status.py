import requests
from requests_oauthlib import OAuth1

from utils.tweet_memory import remember_tweet
from utils.config import Config
from utils.arg_parser import initialize_parser


def send_tweet(body: str, config: Config):
    """
    Sends a tweet on behalf of the avobot
    """
    update_url = (
        "https://api.twitter.com/1.1/statuses/update.json?include_entities=true"
    )
    auth = OAuth1(
        config.consumer_key, config.consumer_secret, config.token, config.token_secret
    )
    resp = requests.post(update_url, auth=auth, data={"status": body})
    if resp.status_code == 200:
        body = resp.json()
        print(
            "Tweet sent successfully! Here are the details:\n"
            f"created_at: {body['created_at']}\n"
            f"id: {body['id']}\n"
        )
        remember_tweet(body)
    else:
        print(f"Something truly catastrophic happened:\n{resp.json()}")


# To be removed at some point
if __name__ == "__main__":
    args = initialize_parser()
    cfg = Config(args.secrets)
    tweet_text = args.text
    ans = input(
        f"About to send following tweet:\n\n{tweet_text}\n\n" "Enter 'y' to continue.\n"
    )
    if ans.strip().lower() != "y":
        print("Probably for the best...")
        exit(0)
    send_tweet(tweet_text, cfg)
