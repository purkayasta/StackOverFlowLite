import enum


class VotingOperation(enum.Enum):
    plus = 1
    minus = -1
    default = 0


class NegativeIntConverter:
    regex = r'-?\d+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%d' % value


def get_voting(element, operation):
    # if operation is 1
    # if vote is 1 nothing happened
    # if vote is 0/-1 , add 1

    # if operation is -1
    # if vote is 0/1, subtract 1
    # if vote is -1 , nothing happened

    if operation == VotingOperation.plus.value:
        if element <= 0:
            element = 1
    elif operation == VotingOperation.minus.value:
        if element >= 0:
            element = -1
    return element
    # pass
