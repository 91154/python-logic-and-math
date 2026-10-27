def repeat(Letters, digit):

    return str(Letters).count(str(digit))
Letters = str(input("number : "))
digit = str(input("digit : "))
print(digit, "repeat ", repeat(Letters,digit), "dj")
