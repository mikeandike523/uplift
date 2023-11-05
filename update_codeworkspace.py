# A script to deal with the wierd issue where
# Vscode doesnt support comma seperated list of languages in codeworkspace file

import os
import re
import copy

# Deal with the fact that jsonc (even without comments) can be invalid json
import jstyleson

template_file = os.path.join(os.path.dirname(__file__),"uplift.template.code-workspace")

with open(template_file, "r", encoding="utf-8") as fl:
    config = jstyleson.load(fl)

config_settings = config["settings"]

# A function to determine if a string represents a multi-language-key
def is_multi_language_key(settings_key: str):
    return bool(re.search(r"^\[.*?,.*?\]$", settings_key))

keys = list(config_settings.keys())

for key in keys:
    if is_multi_language_key(key):
        language_list_string = key[1:-1]
        language_list = list(map(lambda x: x.strip(),
                                 language_list_string.split(",")))
        settings_content = copy.deepcopy(config_settings[key])
        del config_settings[key]
        for language in language_list:
            new_key = f"[{language}]"
            config_settings[new_key] = settings_content

with open(template_file, "w", encoding="utf-8") as fl:
    jstyleson.dump(config, fl)





