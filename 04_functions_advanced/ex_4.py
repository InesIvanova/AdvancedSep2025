def rectangle(l, w):
    if not isinstance(l, int) or not isinstance(w, int):
        return "Enter valid values!"

    def area():
        return l * w

    def perimeter():
        return 2 * l + 2 * w

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"

print(rectangle(2, 10))
print(rectangle('2', 10))
