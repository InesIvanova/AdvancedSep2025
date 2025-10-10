from collections import deque

strength = [int(el) for el in input().split()]
accuracy = deque([int(el) for el in input().split()])

goals = 0

while strength and accuracy:
    current_strength = strength[-1]
    current_accuracy = accuracy[0]

    result = current_strength + current_accuracy
    if result == 100:
        strength.pop()
        accuracy.popleft()
        goals += 1
    elif result < 100:
        if current_strength < current_accuracy:
            strength.pop()
        elif current_strength > current_accuracy:
            accuracy.popleft()
        else:
            strength[-1] += current_accuracy
            accuracy.popleft()
    else:
        strength[-1] -= 10
        temp = accuracy.popleft()
        accuracy.append(temp)
        # option 2
        # accuracy.append(accuracy.popleft())
        # option 3
        # accuracy.rotate(-1)


if goals == 3:
    print("Paul scored a hat-trick!")
elif goals == 0:
    print("Paul failed to score a single goal.")
elif goals > 3:
    print("Paul performed remarkably well!")
elif 0 < goals < 3:
    print("Paul failed to make a hat-trick.")


if goals > 0:
    print(f"Goals scored: {goals}")


if (not strength and accuracy) or (strength and not accuracy):
    if strength:
        print(f"Strength values left: {', '.join([str(el) for el in strength])}")
    if accuracy:
        print(f"Accuracy values left: {', '.join([str(el) for el in accuracy])}")

