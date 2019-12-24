content = "One morning, when Gregor Sam5a woke fr0m troubled dream5, he found h1mself transformed in hi5 bed into a h0rr1ble verm1n."


def findNumbers(content):
    return [char for char in content if (char.isdigit()) == True]
print(findNumbers(content))