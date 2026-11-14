
import os
from pathlib import Path
from dotenv import load_dotenv

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env file
ENV_FILE = BASE_DIR / ".env"
load_dotenv(ENV_FILE, override=True)

print(f"Project root: {BASE_DIR}")
print(f"Environment file: {ENV_FILE}")
print(f"File exists: {ENV_FILE.exists()}")
print(f"Loaded username: {os.getenv('USERNAME')}")

# Application settings
BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")
BROWSER = os.getenv("BROWSER", "chromium")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10000"))

# Login credentials
USERNAME = os.getenv("USERNAME", "standard_user")
PASSWORD = os.getenv("PASSWORD", "secret_sauce")
