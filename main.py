from random import choice

ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
other_strings = 'abcdefghijklmnopqrstuvwxyz0123456789'

if __name__ == '__main__':
    str_count = int(input())
    if str_count >= 6:
        password = ""
        password += choice(other_strings + ascii_uppercase)

        if password.isupper():
            upper_index = 1
        else:
            upper_index = 0

        str_upper_count = choice(range(int(str_count * 0.2), int(str_count * 0.3) + 1))
        for i in range(str_count - 1):
            if password[i].islower() and upper_index < str_upper_count:
                password += choice(ascii_uppercase)
                upper_index += 1
            else:
                password += choice(other_strings)
        print(password)

    my_file = open("Пароль.txt", "w+")
    my_file.write(str(password))
    my_file.close()


