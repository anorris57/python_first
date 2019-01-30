known_users = ["Alice", "Bob", "Claire",
               "Dan", "Emma", "Fred", "Georgie", "Harry"]
print(len(known_users))
while True:
    print("Hi! My is Travis")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        string = "Hi {}"
        output = string.format(name)
        print(output)
    else:
        print("name NOT recognised")
