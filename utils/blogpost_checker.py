import boto3
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.request import urlopen

feed_url = "https://avogadbro.blogspot.com/feeds/posts/default"


def get_post(blog_table: boto3.resource, post_id: str):
    """
    Attempts to fetch post from blog_post table.
    """
    response = blog_table.get_item(Key={"post_id": post_id})
    return response.get("Item")


def parse_feed():
    """
    Grabs RSS feed for the blog and looks for new entries.
    """
    with urlopen(feed_url) as data:  # nosec
        raw_xml = data.read()

    publised_fmt = "%Y-%m-%dT%H:%M:%S.%f%z"

    parsed_xml = BeautifulSoup(raw_xml, "xml")

    # I'd be shocked if blogger didn't keep this in order but
    latest_published_at = 0
    for post in parsed_xml.findAll("entry"):
        published_at = int(
            datetime.strptime(
                post.select("published")[0].text, publised_fmt
            ).timestamp()
        )
        if published_at > latest_published_at:
            latest_post = post
            latest_published_at = published_at

    dynamodb = boto3.resource("dynamodb")
    blog_table = dynamodb.Table("avobot_blog_posts")
    latest_id = latest_post.select("id")[0].text
    if not get_post(blog_table, latest_id):
        print("New blogpost detected; updating table.")
        post_title = latest_post.select("title")[0].text
        blog_table.put_item(
            Item={
                "post_id": latest_id,
                "published_at": latest_published_at,
                "title": post_title,
            }
        )
    # tweet about it
    else:
        print("No new posts detected.")


if __name__ == "__main__":
    parse_feed()
