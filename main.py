def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid input. Please try again."

    return wrapper

contacts = {}

@input_error
def add_contact(params):
    name, phone = params
    contacts[name] = phone
    return f"Contact {name} with phone {phone} added."

@input_error
def change_phone(params):
    name, phone = params
    if name in contacts:
        contacts[name] = phone
        return f"Phone number updated for {name}. New phone number: {phone}"
    else:
        raise KeyError

@input_error
def show_phone(name):
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        raise KeyError

def show_all_contacts():
    if not contacts:
        return "No contacts found."
    result = "Contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result

def handle_command(command):
    command = command.lower()
    if command == "hello":
        return "How can I help you?"
    elif command.startswith("add "):
        params = command[4:].split(" ")
        if len(params) == 2:
            return add_contact(params)
        else:
            raise ValueError
    elif command.startswith("change "):
        params = command[7:].split(" ")
        if len(params) == 2:
            return change_phone(params)
        else:
            raise ValueError
    elif command.startswith("phone "):
        name = command[6:]
        return show_phone(name)
    elif command == "show all":
        return show_all_contacts()
    elif command in ["good bye", "close", "exit"]:
        return "Good bye!"
    else:
        raise ValueError

def main():
    while True:
        user_input = input("Enter a command: ")
        if user_input == ".":
            break
        response = handle_command(user_input)
        print(response)

if __name__ == "__main__":
    main()