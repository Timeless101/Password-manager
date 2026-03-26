import re
import string

#Naming restrictions.
def data_validation_name(data):
    if len(data) > 0 and len(data) < 14:
        if not re.search(r"\d", data):
            if not any(char in string.punctuation for char in data):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

#Password restrictions.
def password_validation_name(data):
    if len(data) >= 6 and len(data) < 24:
        return True
    else:
        return False