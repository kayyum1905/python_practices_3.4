from random import randint

objects = ('Rock', 'Paper', 'Scissor')
human_object = ''
ai_object = ''


def list_objects():
    print('Choose your object by typing the first letter of your choice: ')
    print(objects)


def ask_user_input():
    user_input = input('Type here please: ')
    process_user_choice(str(user_input))


def process_user_choice(user_input):
    user_input = user_input.lower()
    user_object = ''
    if user_input == 'r':
        user_object = objects[0]
    elif user_input == 'p':
        user_object = objects[1]
    elif user_input == 's':
        user_object = objects[2]
    else:
        print('Invalid input, try again')
        ask_user_input()

    if user_object in objects:
        global human_object
        human_object = user_object
        print('Your choice was: ', human_object)


def ai_choice():
    ai_input = objects[randint(0, 2)]
    print('Computer choice was: ', ai_input)
    global ai_object
    ai_object = ai_input


def compare_inputs():
    if human_object == 'Rock':
        if ai_object == 'Rock':
            print('TIE!')
        elif ai_object == 'Scissor':
            print('HUMAN WIN!')
        elif ai_object == 'Paper':
            print('AI WİN!!')
    elif human_object == 'Scissor':
        if ai_object == 'Rock':
            print('AI WİN!!')
        elif ai_object == 'Scissor':
            print('TIE!')
        elif ai_object == 'Paper':
            print('HUMAN WIN!')
    elif human_object == 'Paper':
        if ai_object == 'Rock':
            print('HUMAN WIN!')
        elif ai_object == 'Scissor':
            print('AI WİN!!')
        elif ai_object == 'Paper':
            print('TIE!')


def start_new_turn():
    print('type \'y\' for new turn or \'n\' to terminate: ')
    input_user = input(':')
    if input_user == 'y':
        process_game()
    elif input_user == 'n':
        return


def process_game():
    list_objects()
    ask_user_input()
    ai_choice()
    compare_inputs()
    start_new_turn()

process_game()
