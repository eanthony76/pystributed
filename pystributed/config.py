
import json
import os

DEFAULT_CONFIG = {
    "setting1": "default_value1",
    "setting2": "default_value2",
}

# Path to the external config.json file
CONFIG_PATH = os.path.expanduser("~/.pystributed/config.json")

def load_config():
    """Load configuration from external JSON file with fallback to defaults."""
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r') as file:
            user_config = json.load(file)
        return {**DEFAULT_CONFIG, **user_config}
    return DEFAULT_CONFIG

CONFIG = load_config()
