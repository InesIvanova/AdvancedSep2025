mapper = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "^": lambda a, b: a ** b,
}


def calculate(num1, num2, sign):
    function = mapper[sign]
    return function(num1, num2)