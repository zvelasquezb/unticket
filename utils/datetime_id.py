from datetime import datetime

def get_id():
    now = datetime.now()
    timestamp = int(now.timestamp())
    return hex(timestamp)[2:]