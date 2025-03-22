import json
import os
import re
import platform
import logging

LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")


def init_logger():
    logging.basicConfig(
        level=getattr(logging, LOGGING_LEVEL),
        format="%(asctime)s [%(levelname)-5.5s] - %(name)s:%(filename)s:%(lineno)d - %(message)s",
        handlers=[logging.StreamHandler()],
    )

    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)


init_logger()
logger = logging.getLogger(__name__)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Connection": "keep-alive",
    "Accept-Language": "en-US,en;q=0.9,lt;q=0.8,et;q=0.7,de;q=0.6",
}


def json_dump(data: json, filename: str = "data.json", open_type: str = "w"):
    """
    :param data: [required]
    :param filename: default="data.json"
    :param open_type: default="w", [w-write, a-append]
    """
    if not re.match(".*\.json", filename):
        filename = f"{filename}.json"

    if platform.system() == "Windows":
        filename = filename.replace("/", "\\")

    if platform.system() != "Windows" and "/" in filename:
        directory = re.search(".*\/", filename).group()
        if not os.path.exists(directory):
            os.makedirs(directory)

    with open(filename, open_type) as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def json_load(filename: str = "data.json", open_type: str = "r") -> json:
    """
    :param filename: default="data.json"
    :param open_type: default="r"
    :return: dict
    """
    if platform.system() == "Windows":
        filename = filename.replace("/", "\\")

    if not re.match(".*\.json", filename):
        filename = f"{filename}.json"

    if not os.path.isfile(filename):
        return []

    with open(filename, open_type) as f:
        return json.load(f)
