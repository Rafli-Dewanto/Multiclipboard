import sys
import clipboard
import json


SAVED_DATA = "clipboard.json"


def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


def remove_data(filepath, key):
    with open(filepath, 'r') as f:
        data = json.load(f)
    del data[key]

    with open(filepath, 'w') as f:
        data = json.dump(data, f)


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")

    elif command == 'load'.lower():
        print(data)
        key = input("Enter a key: ")

        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("Key doesn't exist")

    elif command == 'list'.lower():
        print(data)

    elif command == 'delete'.lower():
        print(data)
        key = input("Input the key of the data that you want to be deleted: ")
        remove_data(SAVED_DATA, key)
        print(f"{key} has been deleted")

    elif command == 'help'.lower():
        print("Commands: save, load, list, delete")

    else:
        print('unknown command')

else:
    print("Pass only one command")
