known_users = ["Alice","Bob", "Claire", "Dan","Emma","Fred", "Georgie","Harry"]


while True:
    print("Hi! My is Travis")
    name = input ("What is your name?: ").strip().capitalize()

    if name in known_users:
        #print("Hello{}!".format(name)) instructor solution
        string = "Hi {}"
        output = string.format(name)
        print(output)
        remove = input("Would you like to be removed from the system (y/n)?: ").lower()
        if remove == "y":
            print(known_users)
            known_users.remove(name)#only removes first occurance and actually changes original list
            print(known_users)
    else:
        print("name NOT recognised")
