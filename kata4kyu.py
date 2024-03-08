# 08.03.2024
def move_zeros(lst):
    def one():

        if len(set(lst)) == 1 or not lst:
            return lst

        # [1, 0, 1, 2, 0, 1, 3]
        pointer_i, pointer_j = 0, len(lst) - 1
        while pointer_i != pointer_j:
            if lst[pointer_i]:
                pointer_i += 1
            else:
                for i in range(pointer_i, pointer_j):
                    lst[i], lst[i+1] = lst[i+1], lst[i]
                pointer_j -= 1
        return lst

    def two():
        return [item for item in lst if item]

    return two()





def main():
    pass


if __name__ == '__main__':
    main()
