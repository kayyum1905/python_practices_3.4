letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z')
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
punctuations = ('!', '+', '&', '?', '_', '#', '-', '*',
                '.', '\"', '\'', '^', '%', '/', '(', ')', '=', '@',
                '<', '>')


def ask_password():
    pw = input('Please set a password (at least one number, one letter and one punctuation):  \n')
    pw = list(pw)
    no_count = 0
    punc_no = 0
    let_no = 0
    for n in pw:
        if n in letters:
            let_no += 1
        elif n in str(numbers):
            no_count += 1
        elif n in punctuations:
            punc_no += 1
    print('Letter count:', let_no)
    print('Number count:', no_count)
    print('Punctionation count: ', punc_no)

    if let_no > 0 and punc_no > 0 and no_count > 0:
        print('Your password is confirmed')
    else:
        print('Password does not match standards please set new password \n')
        ask_password()

ask_password()
