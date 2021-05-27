from setuptools import setup

setup(
    name="Avobot",
    description="Avobot from twitter fame.",
    url="https://github.com/dvfeinblum/avobot/",
    python_requires=">=3.8",
    install_requires=[
        "pyyaml ~= 5.4.1",
        "requests ~= 2.25.1",
        "requests_oauthlib ~= 1.3.0",
        "pre-commit ~= 2.12.1",
    ],
)
