from requests import *
from getpass import getpass

def getUserInformation():
    print("Github login")

    username = input("Username: ")

    r = get('https://api.github.com/user', auth = (username, getpass("Password: ")))

    user_data = r.json()

    name = user_data["name"]
    public_repos_amt = int(user_data["public_repos"])
    private_repos_amt = int(user_data["total_private_repos"])

    print("\nYour name is %s, you have a total of %d public repositories and you own %d private repositories.\n\n" %
          (name, public_repos_amt, private_repos_amt))
    
    repos_url = user_data["repos_url"]
    getUserPublicReposInformation(repos_url)

    return None

def getUserPublicReposInformation(repos_url):
    r = get(repos_url)
    repos_data = r.json()
    print("Your public repositories are:\n")

    for repo in repos_data:
        print("{0:<50}{1:<255}".format(repo["name"], repo["description"]))

    return None

def main():
    getUserInformation()
    
    return None    

if __name__ == "__main__":
    main()