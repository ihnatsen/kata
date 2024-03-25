def spin_words(sentence: str):
    """
    Write a function that takes in a string of one or more words, and returns the same string, but with all words that
    have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters
     and spaces. Spaces will be included only when more than one word is present.

    Examples:

    "Hey fellow warriors"  --> "Hey wollef sroirraw"
    "This is a test        --> "This is a test"
    "This is another test" --> "This is rehtona test
    """
    return ' '.join([(word[::-1] if len(word) >= 5 else word) for word in sentence.split(" ")])


def likes(names: list[str]):
    """
    You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other
    items. We want to create the text that should be displayed next to such an item.

    Implement the function which takes an array containing the names of people that like an item. It must return the
    display text as shown in the examples:

    []                                -->  "no one likes this"
    ["Peter"]                         -->  "Peter likes this"
    ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
    ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
    ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
    Note: For 4 or more names, the number in "and 2 others" simply increases."""


#     match names:
#         case []:
#             return 'no one likes this'
#         case [a]:
#             return f'{a} likes this'
#         case [a, b]:
#             return f'{a} and {b} like this'
#         case [a, b, c]:
#             return f'{a}, {b} and {c} like this'
#         case [a, b, *rest]:
#             return f'{a}, {b} and {len(rest)} others like this'

    match len(names):
        case 0:
            return f'no one like this'
        case 1:
            return f'{names[0]} like this'
        case 2:
            return f'{names[0]} and {names[1]} like this'
        case 3:
            return f'{names[0]}, {names[1]} and {names[2]} like this'
        case _:
            return f'{names[0]}, {names[1]} and {len(names) - 2} other like this'


def dig_pow(n: int, p: int):
    """
Some numbers have funny properties. For example:

89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the digits
of n raised to consecutive powers starting from p is equal to k * n.

In other words, writing the consecutive digits of n as a, b, c, d ..., is there an integer k such that :

If it is the case we will return k, if not return -1.

Note: n and p will always be strictly positive integers.

Examples:
n = 89; p = 1 ---> 1 since 8¹ + 9² = 89 = 89 * 1

n = 92; p = 1 ---> -1 since there is no k such that 9¹ + 2² equals 92 * k

n = 695; p = 2 ---> 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2

n = 46288; p = 3 ---> 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
"""

    # new foo enumerate()

    # The enumerate() function adds a counter to an iterable and returns it as an enumerate object
    # (iterator with index and the value).

    # Example
    # languages = ['Python', 'Java', 'JavaScript']
    #
    # # enumerate the list
    # enumerated_languages = enumerate(languages)
    #
    # # convert enumerate object to list
    # print(list(enumerated_languages))
    #
    # # Output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]
    places = [int(place) for place in list(str(n))]
    degree = [*range(p, len(places)+p)]
    sum_pow = sum([pow(place, i) for place, i in zip(places, degree)])
    return sum_pow/n if not sum_pow % n else -1


def nb_year(p0, percent, aug, p):
    year = 0
    while p0 < p:
        p0 += int(p0 + p0 * percent/100 + aug)
        year += 1
    return year


def order(sentence: str):
    """Your task is to sort a given string. Each word in the string will contain a single number. This number is the 
      position the word should have in the result.

    Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

    If the input string is empty, return an empty string. The words in the input String will only contain valid 
    consecutive numbers.

    Examples
    "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
    "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
    ""  -->  """""
    # def find_number(word):
    #     if not sentence:
    #         return ""
    #
    #     def find_number(word):
    #         index = 0
    #         while not word[index] in {str(i) for i in range(1, 10)}:
    #             index += 1
    #         return word[index]
    #
    #     words = sentence.split(' ')
    #     subsequence = {find_number(word): word for word in words}
    #     subsequence = dict(sorted(subsequence.items()))
    #     return ' '.join(subsequence.values())

    return ' '.join(sorted(sentence.split(), key=lambda w: sorted(w)))


def to_camel_case(text):
    """Complete the method/function so that it converts dash/underscore delimited
     words into camel casing. The first word within the output should be capitalized
     only if the original word was capitalized (known as Upper Camel Case, also often
     referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"""
    chars: list[str] = list(text)
    for index in range(1, len(text) - 1):
        if chars[index] in {'_', '-'}:
            chars[index+1] = chars[index+1].upper()
    return ''.join([char for char in chars if char not in {'_', '-'}])


def main():
    print(to_camel_case('The_Stealth-Warrior'))
    pass


if __name__ == '__main__':
    main()
