# 08.03.2024
def move_zeros(lst):
    def one():

        if len(set(lst)) == 1 or not lst:
            return lst

        pointer_i, pointer_j = 0, len(lst) - 1

        while not lst[pointer_j]:
            pointer_j -= 1

        while pointer_i != pointer_j:
            if lst[pointer_i]:
                pointer_i += 1
            else:
                for i in range(pointer_i, pointer_j):
                    lst[i], lst[i+1] = lst[i+1], lst[i]
                pointer_j -= 1

    def two():
        return [item for item in lst if item] + [0] * lst.count(0)

    return two()


class RomanNumerals:

    arab_roman = {1: 'I', 10: 'X', 100: 'C',
                  5: 'V', 50: 'L', 500: 'D',
                  1000: 'M'}

    ranks = [{1: 'M'},
             {1: 'C', 5: 'D', 9: 'CM', 10: 'M'},
             {1: 'X', 5: 'L', 9: 'XC', 10: 'C'},
             {1: 'I', 5: 'V', 9: 'IX', 10: 'X'}]

    roman_arab = {arab: roman for roman, arab in arab_roman.items()}

    @staticmethod
    def to_roman(val: int) -> str:
        def foo(rank_zero, value_rank):

            number = ''
            if value < 4:
                for n in range(value_rank):
                    number += rank_zero[1]
            elif value_rank == 4:
                number += rank_zero[1] + rank_zero[5]

            elif value_rank == 5:
                number += rank_zero[5]

            elif value_rank <= 8:
                number += rank_zero[5]
                for n in range(9 - value_rank):
                    number += rank_zero[1]

            elif value_rank == 9:
                number += rank_zero[9]

            return number

        value_ranks = [int(i) for i in list(str(val))]
        value_ranks = [0] * (4-len(value_ranks)) + value_ranks

        number = ''
        for rank, value in zip(RomanNumerals.ranks, value_ranks):
            number += foo(rank, value)

        return number

    @staticmethod
    def from_roman(roman_num: str) -> int:
        value_symbols = [RomanNumerals.roman_arab[sym] for sym in list(roman_num)]

        for i in range(len(value_symbols)-1):
            if value_symbols[i] < value_symbols[i+1]:
                value_symbols[i+1] -= value_symbols[i]
                value_symbols[i] = 0

        return sum(value_symbols)


def solution(n):
    ranks = [{1: 'M'},
             {1: 'C', 5: 'D', 9: 'CM', 10: 'M'},
             {1: 'X', 5: 'L', 9: 'XC', 10: 'C'},
             {1: 'I', 5: 'V', 9: 'IX', 10: 'X'}]

    def foo(rank_zero, value_rank):

        number = ''
        if value < 4:
            for n in range(value_rank):
                number += rank_zero[1]
        elif value_rank == 4:
            number += rank_zero[1] + rank_zero[5]

        elif value_rank == 5:
            number += rank_zero[5]

        elif value_rank <= 8:
            number += rank_zero[5]
            for _ in range(value_rank-5):
                number += rank_zero[1]

        elif value_rank == 9:
            number += rank_zero[9]

        return number

    value_ranks = [int(i) for i in list(str(n))]
    value_ranks = [0] * (4 - len(value_ranks)) + value_ranks

    number = ''
    for rank, value in zip(ranks, value_ranks):
        number += foo(rank, value)

    return number


def next_bigger(n):
    ranks = sorted([int(i) for i in list(str(n))], reverse=True)
    ranks = [int(i)*10**pow for pow, i in enumerate(ranks[::-1])]
    res = sum(ranks) if sum(ranks) != n else None
    return res


if __name__ == '__main__':
    print(next_bigger(2017))
