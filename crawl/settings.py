import yaml


def get_app_settings():
    with open("settings.yaml", "r") as settings_file:
        settings = yaml.load(settings_file)
        return settings

    return {}
