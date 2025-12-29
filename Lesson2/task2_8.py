def create_user_settings():
    """Creates new settings"""
    setting = {
        "theme": "white",
        "language": "ua",
        "notifications": "email"
    }

    def set_value(key: str, value: str) -> dict:
        """Changes setting by its key-value"""
        if key in setting:
            setting[key] = value
            print(f"Setting '{key}' is set with value '{value}'")
        else:
            print('Unknown setting')
        return setting

    def get_setting_by_key(key: str) -> str:
        """Gives value of exact setting inputted as a key"""
        print(setting.get(key))
        return setting.get(key)

    def get_setting() -> dict:
        """Gives all settings that have been already set"""
        print(f"{setting}")
        return setting

    return set_value, get_setting_by_key, get_setting


set_new_value, get_settings_by_key, get_settings = create_user_settings()
get_settings()
set_new_value("theme", "black")
get_settings()
set_new_value("lang", "en")
get_settings_by_key("language")
