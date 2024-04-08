
class TooYoung(Exception):
    pass

class TooOld(Exception):
    pass


class Young(Exception):
    pass


age = 35
try:
    if age < 6:
        raise TooYoung
    elif age < 18:
        raise Young
    elif age > 100:
        raise TooOld
    else:
        print("You can cast your valuable vote....")
except TooYoung:
    print("Person is too very young to cast a vote....")
except Young:
    print("Person is young to cast the vote......")
except TooOld:
    print("Person is too old to cast a vote.....")

