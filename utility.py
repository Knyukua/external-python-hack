from datetime import datetime

def timestamp():
    return datetime.now().time().replace(microsecond=0)

def prefix():
    return f'[{timestamp()}] PyEx | '