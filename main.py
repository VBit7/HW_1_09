"""
Homework Assignment. Python Core. Module 9
For a description of the task, please refer to the README.md file
"""
def input_error(func):
    """
    Decorator function to handle common input errors in the wrapped function.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Invalid input. Please try again."

    return wrapper


contacts = {}


@input_error
def hello(*args):
    """
    Greets the user with a standard message.
    """
    return "How can I help you?"


@input_error
def add(params: list) -> str:
    """
    Adds a new contact to the database.

    Parameters:
        params (list): A list containing the name and phone number of the contact.

    Returns:
        str: A message indicating the success or failure of the operation.
             - If the contact with the given name already exists, suggests using the 'change' command.
             - If the contact is successfully added, confirms the addition with the name and phone number.
    """
    name, phone = params

    if name not in contacts:
        contacts[name] = phone
        result = f"Contact {name} with phone {phone} added."
    else:
        result = f"Contact {name} already exists. Use the 'change' command to modify the number."

    return result


@input_error
def change(params: list) -> str:
    """
    Updates the phone number of an existing contact in the database.

    Parameters:
        params (list): A list containing the name and new phone number of the contact.

    Returns:
        str: A message indicating the success or failure of the operation.
             - If the contact with the given name is found, updates the phone number and confirms the change.
             - If the contact is not found, notifies that the contact is not in the database.
    """
    if len(params) != 2:
        raise ValueError
    name, phone = params
    if name in contacts:
        contacts[name] = phone
        result = f"Phone number updated for {name}. New phone number: {phone}"
    else:
        result = f"Contact '{name}' not found in the database."

    return result


@input_error
def phone(params: list) -> str:
    """
    Outputs the phone number for the specified contact.

    Parameters:
        params (list): A list containing the name of the contact.

    Returns:
        str: A message indicating the success or failure of the operation.
             - If the contact with the given name is found, displays the phone number.
             - If the contact is not found, notifies that the contact is not in the database.
    """
    name = params[0]
    if name in contacts:
        result = f"Phone number for {name}: {contacts[name]}"
    else:
        result = f"Contact '{name}' not found in the database."

    return result


@input_error
def show(params: list) -> str:
    """
    Displays all saved contacts with their phone numbers.

    Parameters:
        params (list): A list containing the command 'all' to show all contacts.

    Returns:
        str: A message displaying all saved contacts and their phone numbers.
             - If no contacts are found, a message indicating that no contacts are available.
    """
    if not contacts:
        return "No contacts found."

    command = params[0]

    if command == "all":
        result = "Contacts:\n"
        for name, phone in contacts.items():
            result += f"   {name}: {phone}\n"
    else:
        raise IndexError

    return result


def help(params: list) -> str:
    """
    Displays a list of possible commands and their descriptions.

    Usage:
        help [language]  - Displays a list of available commands and their descriptions.
                           - Optional: Provide 'ua' or 'ukr' as a parameter to get the help message in Ukrainian.

    Parameters:
        params (list): A list containing an optional language parameter ('ua' or 'ukr').

    Returns:
        str: A message containing the list of possible commands and their descriptions in English or Ukrainian.    
    """
    help_msg = """
    Possible commands:
        hello                       - responds with "How can I help you?"
        add name phone              - saves a new contact
                                        name    - contact's name
                                        phone   - phone number, separated by a space
        change name phone           - updates the phone number of an existing contact
                                        name    - contact's name
                                        phone   - new phone number, separated by a space
        phone name                  - outputs the phone number for the specified contact
                                        name    - name of the contact whose number needs to be shown
        show all                    - displays all saved contacts with phone numbers
        good bye | close | exit     - any of these commands will terminate the bot's operation
        help                        - displays this text
    """

    if len(params) != 0:
        if params[0] in ["ua", "ukr"]:
            help_msg = """
    Можливі команди:
        hello                       - відповідає "How can I help you?"
        add name phone              - зберігає новий контакт
                                        name     - ім'я контакту
                                        phone    - номер телефону, обов'язково через пробіл
        change name phone           - зберігає новий номер телефону існуючого контакту
                                        name     - ім'я контакту
                                        phone    - номер телефону, обов'язково через пробіл
        phone name                  - виводить номер телефону для зазначеного контакту
                                        name     - ім'я контакту, чий номер треба показати
        show all                    - виводить всі збереженні контакти з номерами телефонів
        good bye | close | exit     - по будь-якій з цих команд бот завершує свою роботу
        help                        - виводить цей текст
    """
    return help_msg


commands = {
    "hello": hello,
    "add": add,
    "change": change,
    "phone": phone,
    "show": show,
    "help": help,
}


def main():
    """
    Main function to execute a simple command-line bot.

    The bot continuously prompts the user to enter commands until the user types 'good bye', 'close', 'exit', or '.'.
    It processes user input, executes corresponding commands, and provides responses.

    Commands:
        - 'good bye', 'close', 'exit', or '.' to terminate the bot.
        - Type 'help' to see available commands.

    Returns:
        None    
    """
    while True:
        user_input = input("Enter a command: ").lower().strip()

        if user_input in ["good bye", "close", "exit", "."]:
            break

        params = user_input.split(" ")

        while "" in params:
            params.remove("")

        if params[0] in commands:
            response = commands[params[0]](params[1:])
            print(response)
        else:
            print("Unknown command. Type 'help' to see available commands.")

    print("Good bye!")


if __name__ == "__main__":
    main()
