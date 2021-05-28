import boto3
from datetime import datetime

from requests.models import Response


def parse_created_at(date_string: str) -> int:
    """
    For some horrid reason, the twitter api
    gives a created at date in the response body
    that looks like "Wed Oct 10 20:19:24 +0000 2018"
    """
    date_fmt = "%a %b %d %H:%M:%S %z %Y"

    return int(datetime.strptime(date_string, date_fmt).timestamp())


def remember_tweet(resp: Response):
    """
    Stores tweet in avo's brain for later use.
    """
    dynamodb = boto3.resource("dynamodb")
    brain = dynamodb.Table("avobot_tweets")
    brain.put_item(
        Item={
            "tweet_id": resp["id"],
            "created_at": parse_created_at(resp["created_at"]),
            "text": resp["text"],
        }
    )
