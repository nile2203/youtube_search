from datetime import datetime

import uuid


def get_24_char_uuid():
    uid = uuid.uuid4().hex
    for i in range(0, 8):
        uid = uid[:i] + uid[i + 1:]
    return uid.upper()


def format_datetime_user_friendly(date):
    if not date:
        return ''

    return datetime.strftime(date, '%d %b,%Y %I:%S %p')
