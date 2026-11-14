
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv(
    "BASE_URL",
    "https://www.saucedemo.com/"
)

BROWSER = os.getenv("BROWSER", "chromium")

HEADLESS = os.getenv(
    "HEADLESS", "true"
).lower() == "true"

DEFAULT_TIMEOUT = int(
    os.getenv("DEFAULT_TIMEOUT", "10000")
)

USERNAME = os.getenv(
    "USERNAME", "standard_user"
)

PASSWORD = os.getenv(
    "PASSWORD", "secret_sauce"
)
