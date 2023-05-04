import requests
from functions.request_checker import request_checker


print("\n############## WELCOME TO URL EXTRACTOR TOOL ##############\n")
url = input("Please enter the url: ")

if url.startswith("https://") or url.startswith("http://"):
    try:
        req = requests.get(url)
        request_checker(req)
    except:
        print("\033[1;91m ERROR HAPPENED, i think the url is not working \n")
else:
    print("\033[1;34m\nexample: https://test.com \n")
    exit(1)
