import os
import id_gen
import json
import datetime

current_directory = os.path.dirname(os.path.abspath(__file__))
full_path = os.path.join(current_directory, "settings.json")
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def load_settings(): 
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    
def save_log(name, log):
    settings = load_settings()
    path = settings["logs_path"][name]
    with open(path, 'a', encoding='utf8') as logs:
        logs.write(f"[{time}] [id:{id_gen.gen(15)}]  {log} \n")
