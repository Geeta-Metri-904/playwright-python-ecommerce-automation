
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv(
    "BASE_URL",
    "https://www.saucedemo.com/"
)

USERNAME = os.getenv(
    "USERNAME",
    "standard_user"
)

PASSWORD = os.getenv(
    "PASSWORD",
    "secret_sauce"
)

DEFAULT_TIMEOUT = int(
    os.getenv("DEFAULT_TIMEOUT", "10000")
)
