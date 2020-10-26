import re
def my_atoi(s):
    if re.match('([ ]*[a-zA-Z.])', s):
        return 0
    s = re.sub('^[ ]*', '', s)
    print(s)
    result = re.match('([\+\-]?[0-9]+)', s)
    if result:
        print(result)
        result = int(result.group(0))
        if result < -(2**31):
            return -(2**31)
        if result > 2**31 - 1:
            return 2**31 - 1
        return result
    else:
        return 0

my_atoi("   +0 123")
