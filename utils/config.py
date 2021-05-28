import yaml


class Config:
    """
    Simple wrapper around secrets file for easy access
    """

    def __init__(self, secrets_path):
        with open(secrets_path, "r") as f:
            secrets = yaml.safe_load(f)
        try:
            self.consumer_key = secrets["api_key"]
            self.consumer_secret = secrets["api_secret_key"]
            self.token = secrets["access_token"]
            self.token_secret = secrets["access_token_secret"]
        except KeyError:
            print(f"Failed to load secrets from {secrets_path}")
            raise
