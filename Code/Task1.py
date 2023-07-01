"""
Реализовать функцию, которая работает так же, как и метод str.split
(без использования str.split).
Methods: for loop, if-else, append, join

Input: split_by_symbol("text text2 text1", " ")
Output: ['text', 'text2', 'text1']
"""


def split_by_symbol(text: str, separator: str) -> list:
    result = []
    word = []
    for t in text:
        if t != separator:
            word.append(t)
        else:
            result.append("".join(word).strip())
            word.clear()
    result.append("".join(word).strip())
    return result


string_ = input()
separator = ","
print(split_by_symbol(string_, separator=separator))

