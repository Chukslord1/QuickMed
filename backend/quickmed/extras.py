import string
import random

def generate_password(minimum=16, maximum=25):
    # Generates a random password
    # specify all uppercase, lowercase, numeric and special characters so our passwords contain them
    uppercase, lowercase =  string.ascii_letters[:26], string.ascii_letters[26:]
    char_list = ""
    # this ensures that every generated password has uppercase, lowercase, numeric, special characters
    while len(char_list) < maximum:
        for chars in [uppercase, lowercase, string.digits, string.punctuation]:
            char_list += "".join(random.sample(chars, random.randint(1, 3)))

    password = "".join(random.sample(char_list, random.randint(minimum, maximum)))
    return password

def get_user_history(user, mode="short", test_type="all"):
    if test_type != "all":
        # Select test by test type
        pass
    history_table = [{"ID": 5000, "type": "Malaria Test", "result": "positive", "date": "01/10/2019 11:59:20", "notes": "Sample Test"}] * 10
    if mode == "short":
        history_table = history_table[:5]

    return history_table

def get_billing_history(user):
    billing_table = [{"ID": 12345, "date": "01/10/2019 11:59:20", "amount": 1000000, "card": "1234-5678-9012-xxxx", "status": "paid"}] * 10

    return billing_table