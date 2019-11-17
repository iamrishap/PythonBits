import requests
import json

def get_open_pull_requests(repo=None, user=None):
    '''
    Function to read the open pull requests in a repository
    :param repo: name of the repository
    :param user: username
    :return: List of open pull requests
    '''
    if not repo:
        print("Enter repo URL")
        repo = input()
    if not user:
        print("Input username")
        user = input()
    r = requests.get("https://api.github.com/repos/" + user + "/" + repo + "/pulls?state=open")
    if r.status_code in range(200,300):
        result = json.loads(r)
        print("Found {} open pull requests for the repo {}".format(len(result), repo))
        for val in result:
            print("Pull request : {} , URL : {}").format(val["title"], val["url"])
        return result
    else:
        print("API failed to read. Reponse code : " + r.status_code)


def get_closed_pull_requests(repo=None, user=None):
    '''
    Function to read the closed pull requests in a repository
    :param repo: name of the repository
    :param user: username
    :return: List of closed pull requests
    '''
    if not repo:
        print("Enter repo URL")
        repo = input()
    if not user:
        print("Input username")
        user = input()
    r = requests.get("https://api.github.com/repos/" + user + "/" + repo + "/pulls?state=closed")
    if r.status_code in range(200,300):
        result = json.loads(r)
        print("Found {} closed pull requests for the repo {}".format(len(result), repo))
        for val in result:
            print("Pull request : {} , URL : {}").format(val["title"], val["url"])
        return result
    else:
        print("API failed to read. Reponse code : " + r.status_code)


def merge_open_pull_requests():
    '''
    Function to merge the open pull requests in a repository
    :return: None
    '''
    print("Enter repo URL")
    repo = input()
    print("Input username")
    user = input()
    pull_requests = get_open_pull_requests(repo, user)
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    for pull_request in pull_requests:
        data = '{"commit_title": "Merging the pull request", "commit_message": "My commit message", "sha": "'+ pull_request["merge_commit_sha"] +'", "merge_method": "merge"}'
        r = requests.put("https://api.github.com/repos/" + user + "/" + repo + "/pulls/" + pull_request["number"] + "/merge", headers=headers, data=data)
        if r.status_code == 200:
            result = json.loads(r)
            print("Merge for the pull request {} successful".format(pull_request["number"]))
            return result
        else:
            print("Failed to add subscriber to the list. Reponse code : " + r.status_code)


def run_console_app():
    choice = 1
    while choice != 4:
        print("Choose option:")
        print("1. See a list of closed pull requests for a given repo")
        print("2. See a list of open pull requests for a given repo")
        print("3. Merge open pull requests for a given repo")
        print("4. Exit")
        choice = input()
        if choice == 1:
            get_closed_pull_requests()
        elif choice == 2:
            get_open_pull_requests()
        elif choice == 3:
            merge_open_pull_requests()


if __name__ == "__main__":
    run_console_app()