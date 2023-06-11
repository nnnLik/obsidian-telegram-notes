import json
from typing import Dict
from decouple import config


API_TOKEN = config("API_TOKEN")
POSTGRES_URL = config("POSTGRES_URL")


def get_base_messages() -> Dict[str, str]:
    with open("src/utils/msg/base.json", "r") as f:
        msgs: Dict[str, str] = json.load(f)
        return msgs


MESSAGES = get_base_messages()
