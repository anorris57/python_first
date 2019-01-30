known_users = ["Alice","Bob", "Claire", "Dan","Emma","Fred", "Georgie","Harry"]


while True:
    print("Hi! My is Travis")
    name = input ("What is your name?: ").strip().capitalize()

    if name in known_users:
        #print("Hello{}!".format(name))
        string = "Hi {}"
        output = string.format(name)
        print(output)
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()
        if remove == "y":
            known_users.remove(name)#only removes first occurance and actually changes original list
            # can use del command to remove element at index and slices del example[0:2]
        elif remove == 'n':
            print("No problem, I didn't want you to leave anyway!")
    else:
        print("Hmmm I don't think  I have met you yet {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("No worries, see you around!")
