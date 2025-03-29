import os


# pip install python-dotenv
import dotenv
from icecream import ic



def example():
    ic(acct)
    ic(token)


if __name__ == '__main__':
    dotenv.load_dotenv()
    acct = os.getenv(f"gemini_acct")
    token = os.getenv(f"gemini_token")
    assert acct
    assert token
    example()
