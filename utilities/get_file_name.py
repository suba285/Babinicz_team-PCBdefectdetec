

def get_file_name(path):
    revresult = ""
    result = ""
    for char in reversed(path):
        if char != "/":
            revresult += char
        else:
            break

    for char in reversed(revresult):
        if char != ".":
            result += char
        else:
            break

    return result
