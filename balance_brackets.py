def balance(brackets):
    opening = 0
    closing = 0
    if brackets:
        for char in brackets:
            if char == "[":
                opening += 1
            elif char == "]":
                closing += 1
        if opening == closing:
            return True
    return False

test1 = "[][][]"
test2 = "[][]["
print(balance(test1))
print(balance(test2))


