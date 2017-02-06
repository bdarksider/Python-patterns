def parent():
    print("Printing from the parent()")

    def frist_child():
        return "First_child()"
    def second_child():
        return "Second_child()"

    print(first_child())
    print(second_child())
    print("pass")