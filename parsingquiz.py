def balanced(string):
    openers = "{[("
    closers = "}])"

    place = -1
    flag = False
    for c in string:
        if c in openers:
            place = openers.index(c)
            flag = False

        if c in closers:
            if closers.index(c) == place:
                flag = True
            else:
                break

    return flag
