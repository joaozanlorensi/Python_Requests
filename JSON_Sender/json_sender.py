from requests import *
import json

def main():
    url = ""
    my_data = json.dumps(
        {
            "language" : "python",
            "version"  :  "3.8.2"
        })
    r = post(url, data=my_data)
    print(r.status_code)
    print(r.json())
    return None

if __name__ == "__main__":
    main()