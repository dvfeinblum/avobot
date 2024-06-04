from setuptools import setup

setup(
    name="Avobot",
    description="Avobot from twitter fame.",
    url="https://github.com/dvfeinblum/avobot/",
    python_requires=">=3.8",
    install_requires=[
        "boto3 ~= 1.17.83",
        "beautifulsoup4 ~= 4.9.3",
        "boto3 ~= 1.17.83",
        "lxml ~= 4.9.1",
        "pre-commit ~= 2.12.1",
        "pyyaml ~= 5.4.1",
        "requests ~=2.32.0",
        "requests_oauthlib ~= 1.3.0",
    ],
)
