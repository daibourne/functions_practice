def hello():
    print("Good Day, user!")

hello()

def pack(sandwhich, chips, drink):
    return print(sandwhich, chips, drink)

pack("Ham & Cheese", "Takis", "Sprite")

def eat_lunch(lunch_meal):
    if lunch_meal:
        print("My lunchbox is empty!")
    else:
        print("First I eat" + lunch_meal[0])
        for lunch in lunch_meal[1:]:
            print("Next I eat", lunch)
eat_lunch(["pear", "sandwhich", "yogurt"])