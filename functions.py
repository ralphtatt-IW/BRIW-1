
from person import Person
import printer_aux
import texts
import file_functions


def ask_boolean(text):
    error = True
    res = False
    while error:
        try:
            inp = input(text)
            if inp.upper() == "Y":
                res = True
                error = False
            elif inp.upper() == "N" or len(inp) == 0:
                res = False
                error = False
            else:
                print(texts.ENTRY_BOOLEAN)
        except ValueError:
            print(texts.ENTRY_BOOLEAN)
    return res


def ask_input_string(text):
    # Auxiliary function to request a value(text) per command and check for errors.
    # +Parameters:
    #   - text: Message shown to request information
    #
    # Returns the value obtained

    error = True
    res = None
    while error:
        res = input(text)
        if not res:
            print(texts.NOT_EMPTY)
        else:
            error = False
    return res


def ask_number(text, mininum, maximum):
    # Auxiliary function to request a value(number) per command and check for errors.
    # +Parameters:
    #   - text: Message shown to request information
    #   - mininum: Minimum number allow
    #   - maximum: Maximum number allow
    #
    # Returns the value obtained

    error = True
    res = 0
    while error:
        try:
            res = input(text)
            if len(res) != 0:
                res = int(res)
                if res > maximum or res < mininum:
                    print(texts.INCORRECT_OPTION)
                else:
                    error = False
            else:
                res = 0
                error = False
        except ValueError:
            print(texts.ENTRY_INTEGER)
    return res


def add_drink(drinks, filepath):
    # Auxiliary function to ask and add a new drink, in cache and write in the file.

    drink = ask_input_string(texts.DRINK_NAME)
    drinks.append(drink)


def create_new_person(people, drinks, filepath):
    # Requests by console the necessary information to create a new person,
    # which are, name and favourite drink. Finaly save this new person in
    # cache and write in the people file.

    drink = None
    name = ask_input_string(texts.ENTER_NAME)
    add_drink = ask_boolean(texts.QUESTION_ADD_DRINK)
    if add_drink:
        printer_aux.print_list(texts.DRINKS, drinks)
        drink_id = ask_number(texts.ENTER_DRINK_ID, 0, len(drinks))
        if drink_id != 0:
            drink = drinks[drink_id-1]

    p = Person(name, drink)
    people.append(p)


def args_options(arg, people, drinks):
    # Manage the events available to add as arguments when launching the project.
    # +Parameters:
    #   - arg: The argument received

    if arg == 'get-people':
        # Print a list of people
        printer_aux.print_users(people)
    elif arg == 'get-drinks':
        # Print a list of drinks
        printer_aux.print_list(texts.DRINKS, drinks)
    else:
        # If the received argument is not among those available,
        # an error message is printed and you exit the program.
        print(texts.AVAILABLE_ARGUMENTS_OPTIONS)
    exit()


def check_args(args, people, drinks):
    # Manage the number of received arguments. Only one argument is allow.
    # +Parameters:
    #   - args: The arguments received
    #   - people: list of people
    #   - drinks: list of drinks

    len_args = len(args)
    # The arguments must have a length of 2 because
    # the first one is the name of the file when invoking it.
    if len_args > 2:
        # Help message and exit
        print(texts.AVAILABLE_ARGUMENTS_OPTIONS)
        exit()
    elif len_args == 2:
        args_options(args[1], people, drinks)


def set_favourite_drink(people, drinks):

    # Get Person ID
    printer_aux.print_users(people)
    person_id = ask_number(texts.ENTER_PERSON_ID, 0, len(drinks)+1)
    if person_id != 0:
        printer_aux.print_list(texts.DRINKS, drinks)
        drink_id = ask_number(texts.ENTER_DRINK_ID, 0, len(drinks))
        if drink_id != 0:
            drink = drinks[drink_id-1]
            people[person_id - 1].set_favourite_drink(drink)
            print(texts.FAVOURITE_DRINK_UPDATED)
    return people


def goodbye(people, drinks, people_path, drink_path):
    file_functions.write_drinks(drinks, drink_path)
    file_functions.write_people(people, people_path)
    print(texts.GOODBYE)
