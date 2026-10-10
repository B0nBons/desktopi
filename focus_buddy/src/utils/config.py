import json
from pathlib import Path
import copy

CONFIG_DIR = Path.home() / ".focus_buddy"
CONFIG_FILE = CONFIG_DIR / "settings.json"

DEFAULT_VARS = {
    "todos" : [],
    "city" : "",
    "music_url" : "",
}

def load_settings():
    settings = copy.deepcopy(DEFAULT_VARS)
    try:
        with open(CONFIG_FILE, "r", encoding = "utf-8") as f:
            settings.update(json.load(f))
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return settings

def save_settings(settings):
    CONFIG_DIR.mkdir(exist_ok = True)
    with open(CONFIG_FILE, "w", encoding = "utf-8") as f:
        json.dump(settings, f, indent = 2)
        
        