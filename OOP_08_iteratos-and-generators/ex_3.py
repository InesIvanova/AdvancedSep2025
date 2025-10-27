class vowels:
    vowels_list = ['a', 'e', 'i', 'o', 'u', 'y']

    def __init__(self, text):
        self.text = text
        self.current = -1
        self.vowels = [el for el in self.text if el.lower() in self.vowels_list]

    def __iter__(self):
        return self

    # def __next__(self):
    #     self.current += 1
    #     if self.current >= len(self.text):
    #         raise StopIteration
    #     if self.text[self.current].lower() in self.vowels_list:
    #         return self.text[self.current]
    #     else:
    #         return self.__next__()
    def __next__(self):
        self.current += 1
        if self.current >= len(self.vowels):
            raise StopIteration
        else:
            return self.vowels[self.current]

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
