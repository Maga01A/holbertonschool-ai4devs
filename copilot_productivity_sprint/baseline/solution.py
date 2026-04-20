import json
import re

def validate_users(file_path):
    # Manual implementation of email regex
    email_regex = r'^[a-z0-9]+@[a-z]+\.[a-z]{2,3}$'
    
    with open(file_path, 'r') as f:
        users = json.load(f)
        
    valid_users = []
    for user in users:
        if re.match(email_regex, user.get('email', '')) and user.get('age', 0) >= 18:
            valid_users.append(user)
    return valid_users
