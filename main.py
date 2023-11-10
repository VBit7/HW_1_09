def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "KeyError"
        except ValueError:
            return "ValueError"
        except IndexError:
            return "IndexError"
    
    return wrapper


contacts = {}


# "hello"      - відповідає у консоль "How can I help you?
# "add ..."    - зберігає у словнику новий контакт. Замість ... - ім'я та номер телефону, обов'язково через пробіл.
# "change ..." - зберігає в пам'яті новий номер телефону існуючого контакту. Замість ... - ім'я та номер телефону, обов'язково через пробіл.
# "phone ...." - виводить у консоль номер телефону для зазначеного контакту. Замість ... - ім'я контакту, чий номер треба показати.
# "show all"   - виводить всі збереженні контакти з номерами телефонів у консоль.
# "good bye", "close", "exit" - по будь-якій з цих команд бот завершує свою роботу.


@input_error
def hello(params):
    return "How can I help you?"


@input_error
def add(params):
    return "add"


@input_error
def change(params):
    return "change"


@input_error
def phone(params):
    return "phone"


@input_error
def show(params):
    return "show all"


def help(params):
    help_msg = """
        "hello" - Responds in the console with "How can I help you?"
        
        "add ..." - Saves a new contact in the dictionary.
            Replace "..." with the name and phone number, separated by a space.
        
        "change ..." - Updates the phone number of an existing contact in memory.
            Replace "..." with the name and new phone number, separated by a space.
        
        "phone ...." - Outputs the phone number for the specified contact to the console.
            Replace "..." with the name of the contact whose number needs to be shown.
        
        "show all" - Displays all saved contacts with phone numbers in the console.
        
        "good bye", "close", "exit" - Any of these commands will terminate the bot's operation.
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
    # print("Hello!")
    while True:
        user_input = input("Enter a command: ").lower().strip()

        if user_input in ["good bye", "close", "exit", "."]:
            break

        params = user_input.split(" ")
        
        if params[0] in commands:
            print(user_input)
            response = commands[params[0]](params[1:])
            print(response)
        else:
            print("Unknown command. Type 'help' to see available commands.")
    
    print("Good bye!")

    return None


if __name__ == "__main__":
    main()



