import requests
import json

def get_client_lists():
    '''
    Function to read the lists within a client
    :return: None
    '''
    print("Enter client ID")
    client_id = input()
    r = requests.get("https://api.createsend.com/api/v3.2/clients/" + client_id + "/lists.json")
    if r.status_code in range(200, 300):
        result = json.loads(r)
        print("Found {} lists for the client ID {}".format(len(result), client_id))
        for val in result:
            print("Name : {} , ListID : {}").format(val["Name"], val["ListID"])
        return result
    else:
        print("API failed to read. Reponse code : " + r.status_code)


def create_list():
    '''
    Function to create a new list
    :return: ListID of the newly created list
    '''
    print("Enter client ID")
    client_id = input()
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    data = '{"Title": "Website Subscribers", "UnsubscribePage": "http://www.example.com/unsubscribed.html", "UnsubscribeSetting": "AllClientLists", "ConfirmedOptIn": false, "ConfirmationSuccessPage": "http://www.example.com/joined.html" }'
    r = requests.post("https://api.createsend.com/api/v3.2/lists/" + client_id + ".json", headers=headers, data=data)
    if r.status_code == 201:
        result = json.loads(r)
        print("List successfully created")
        return result
    else:
        print("Failed to create the list. Reponse code : " + r.status_code)


def add_subscriber_to_list(list_id):
    '''
    Function to add a subsciber (email) within a list
    :param list_id:
    :return:
    '''
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    data = '{"EmailAddress": "subscriber@example.com", "Name": "New Subscriber", "CustomFields": [{"Key": "website", "Value": "http://example.com"}, {"Key": "interests", "Value": "magic"}, {"Key": "interests", "Value": "romantic walks"}], "Resubscribe": true,     "RestartSubscriptionBasedAutoresponders": true, "ConsentToTrack":"Yes"}'
    r = requests.post("https://api.createsend.com/api/v3.2/subscribers/" + list_id + ".json", headers=headers, data=data)
    if r.status_code == 201:
        result = json.loads(r)
        print("List subscriber added successfully")
        return result
    else:
        print("Failed to add subscriber to the list. Reponse code : " + r.status_code)


def run_console_app():
    choice = 1
    while choice != 3:
        print("Choose option:")
        print("1. See all lists for a given client")
        print("2. Create a list, and add a single email address (‘subscriber’) to that list, for a given client")
        print("3. Exit")
        choice = input()
        if choice == 1:
            get_client_lists()
        elif choice == 2:
            list_id = create_list()
            add_subscriber_to_list(list_id)


if __name__ == "__main__":
    run_console_app()
