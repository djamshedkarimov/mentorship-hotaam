first = input("what is ur first name: ")
last = input("what is ur last name: ")

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "you didnt provide valid inputs"
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"

print(format_name(first, last))

print("""\nThis
is
a
docstring :D""")
