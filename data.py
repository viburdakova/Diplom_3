
from helpers.generators import email, password, name

MAIN_URL = 'https://stellarburgers.nomoreparties.site/'
PROFILE_URL = f'{MAIN_URL}account/profile'
FORGOT_PASSWORD = f'{MAIN_URL}forgot-password'
LOGIN_URL = f'{MAIN_URL}login'
ORDER_HISTORY = f'{MAIN_URL}account/order-history'
FEED_URL = f'{MAIN_URL}feed'
CREATE_USER_URL = f"{MAIN_URL}api/auth/register"
DELETE_USER_URL = f"{MAIN_URL}api/auth/user"
USER_ACCOUNT_URL = f'{MAIN_URL}account'

login_data = {
    "email": "test@example.com",
    "password": "password123456789"
}

log_pass_data = {
    "my_email": "viburdakova@gmail.com",
    "my_password":"12345678910"
}

class Payload:

    @staticmethod
    def generate_user_data():
         return {
            "email": email,
            "password": password,
            "name": name,
        }