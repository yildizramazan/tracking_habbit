import requests
import datetime






pixela_endpoint = "https://pixe.la/v1/users"


# this piece of code gets the date in the required form(yyyymmdd).
now = str(datetime.datetime.now).split(" ")[0].split("-")
DATE_NOW = ""
for i in now:
    DATE_NOW = DATE_NOW + i



#!!!CHANGE THESE TO YOUR INFORMATION BEFORE YOU RUN THE PROGRAM
USERNAME = "example123"
TOKEN = "exampletoken123"
GRAPH_ID = "exampleid123"

headers = {
    "X-USER-TOKEN": TOKEN
}


def first():
    choices = input("What do you want to do?\n"
                    "type 'create' to create an account\n"
                    "type 'graph' to create a new graph\n"
                    "type 'post' to post data for today\n"
                    "type 'update' to update data for any date\n"
                    "type 'delete' to delete data for any date: ").lower()
    return choices



# ------------------------DEFINITION OF CREATE ACCOUNT FUNCTION------------------------ #


def create_acc():
    username_input = input("Set a username that is probably not taken. ")
    token_input = input("Create a token. It will be unique to you. ")
    user_params = dict(token=token_input, username=username_input, agreeTermsOfService="yes", notMinor="yes")
    response_create_acc = requests.post(url=pixela_endpoint, json=user_params)
    print(response_create_acc.text)


# ------------------------DEFINITION OF CREATE GRAPH FUNCTION------------------------ #



def create_graph():
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    colors = ["green", "red", "blue", "yellow", "purple", "black"]
    colors_japan = ["shibafu", "momiji", "sora", "ichou", "ajisai", "kuro"]
    index = int(input(f"Please enter the index number of the color you want your graph be: {colors}"))
    graph_config = {
        "id": GRAPH_ID,
        "name": "Cycling Graph",
        "unit": "Km",
        "type": "float",
        "color": colors_japan[index-1]
    }

    response_create_graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response_create_graph.text)


# ------------------------DEFINITION OF POST VALUE TO GRAPH FUNCTION------------------------ #

def value_posting():
    post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    quantity_input = float(input("What is quantity? "))
    post_value = {
        "date": DATE_NOW,
        "quantity": str(quantity_input),
    }
    response_post_value = requests.post(url=post_endpoint, json=post_value, headers=headers)
    print(response_post_value.text)


# ------------------------DEFINITION OF UPDATE ANY VALUE FUNCTION------------------------ #


def update_value():
    update_year = int(input("what is the year you want to update? "))
    update_month = int(input("what is the month you want to update? "))
    update_day = int(input("what is the day you want to update? "))
    updated_quantity = str(input("what is updated quantity? "))
    update_date = str(datetime.datetime(year=update_year, month=update_month, day=update_day)).split(" ")[0].split("-")
    required_form_date = ""

    for n in update_date:
        required_form_date = required_form_date + n

    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{required_form_date}"

    update_params = {
        "quantity": updated_quantity
    }
    print(update_date, required_form_date, update_endpoint)
    response_update = requests.put(url=update_endpoint, json=update_params, headers=headers)
    print(response_update.text)


# ------------------------DEFINITION OF DELETE ANY VALUE FUNCTION------------------------ #


def delete():

    delete_year = int(input("what is the year you want to delete? "))
    delete_month = int(input("what is the month you want to delete? "))
    delete_day = int(input("what is the day you want to delete? "))
    delete_date = str(datetime.datetime(year=delete_year, month=delete_month, day=delete_day)).split(" ")[0].split("-")
    delete_required_date = ""

    for m in delete_date:
        delete_required_date = delete_required_date + m


    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{delete_required_date}"
    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)


choice_holder = first()

if choice_holder == "create":
    create_acc()
elif choice_holder == "graph":
    create_graph()
elif choice_holder == "post":
    value_posting()
elif  choice_holder == "update":
    update_value()
elif choice_holder == "delete":
    delete()
