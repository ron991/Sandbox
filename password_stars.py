def main():
    get_password = input("Enter password : ")
    while len(get_password) < 5 or len(get_password) > 20:
        print("password not long enough")
        get_password = input("Enter password")
    else:
        print("*" * len(get_password))


main()
