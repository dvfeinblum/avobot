from argparse import ArgumentParser


def initialize_parser():
    """
    Builds a parser for the args coming in. This is probably temporary
    """
    parser = ArgumentParser(description="Send a tweet!")
    parser.add_argument(
        "--secrets", type=str, required=True, help="Path to secrets.yml"
    )
    parser.add_argument("--text", required=False, type=str, help="tweet body")
    return parser.parse_args()
