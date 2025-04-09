import os
import json

def get_project_root():
    # Assuming utils/ is always one level down from project root and I didn't change anything
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def load_config(filename="config.json", use_local_model=False):
    project_root = get_project_root()
    config_path = os.path.join(project_root, filename)

    # Load the config JSON
    with open(config_path, "r") as f:
        config = json.load(f)

    for key, value in config.items():
        if key.endswith("_path") and key != "model_path":
            if not os.path.isabs(value):
                config[key] = os.path.join(project_root, value)
        elif key == "model_path" and use_local_model:
            if not os.path.isabs(value):
                config[key] = os.path.join(project_root, value)

    return config