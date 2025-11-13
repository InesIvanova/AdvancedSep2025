def vowel_filter(function):
    def wrapper(*args, **kwargs):
        for el in args:
            if isinstance(el, str) and  'w' in el:
                raise ValueError("Forbidden letter appears")

        result = function(*args, **kwargs)
        return [el for el in result if el.lower() in 'aeiouy']
    return wrapper


@vowel_filter
def get_letters(letters_list):
    return letters_list


@vowel_filter
def say_something(name, age):
    return f"I am {name} and I am {age} years old w"

print(get_letters(['a', 'b', 'c']))
print(say_something('John', 22))
