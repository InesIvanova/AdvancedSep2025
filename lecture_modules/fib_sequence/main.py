from lecture_modules.fib_sequence.core import create_sequence, locate

command = input()
sequence = None

while command != "Stop":
    num = int(command.split()[-1])

    if command.startswith("Create"):
        sequence = create_sequence(num)
        print(*sequence)
    else:
        if sequence:
            print(locate(num, sequence))
        else:
            print(f"Please first initialize a sequence")

    command = input()
