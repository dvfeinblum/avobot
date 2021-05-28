#!/usr/bin/env python3
from argparse import ArgumentParser
from utils.brain import remember_tweet
import requests
from requests_oauthlib import OAuth1

from utils.config import Config


def initialize_parser():
    """
    Builds a parser for the args coming in. This is probably temporary
    """
    parser = ArgumentParser(description="Send a tweet!")
    parser.add_argument(
        "--secrets", type=str, required=True, help="Path to secrets.yml"
    )
    parser.add_argument("--text", required=True, type=str, help="tweet body")
    return parser.parse_args()


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
