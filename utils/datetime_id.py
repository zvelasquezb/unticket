from datetime import datetime

def get_id():
    now = datetime.now()
    timestamp = int(now.timestamp())
    return hex(timestamp)[2:]

def get_id_():
    now = datetime.now()
    timestamp = int(now.timestamp())
    return int(timestamp)