
import os
from datetime import datetime


def create_directory(path):

    os.makedirs(path, exist_ok=True)


def generate_timestamp():

    return datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


def get_screenshot_name(test_name):

    timestamp = generate_timestamp()

    return f"{test_name}_{timestamp}.png"
