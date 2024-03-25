def generate_hashtag(s: str):
    """The marketing team is spending way too much time typing in hashtags.
    Let's help them with our own Hashtag Generator!
    
    Here's the deal:
    
    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.
    Examples
    " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
    "    Hello     World   "                  =>  "#HelloWorld"
    ""
                                       =>  false"""
    if not s:
        return False

    s = '#' + ''.join(list(map(lambda txt: txt.title(), s.split(' '))))
    return s if len(s) <= 140 else False


def cakes(recipe: dict, avaible: dict):
    """Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths.
    Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns
the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of
flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})"""
    return min([avaible.get(ingredient, 0)//recipe[ingredient] for ingredient in recipe])


def pick_peaks(arr):

    if not arr:
        return

    pos_peaks = {'pos': [], 'peaks': []}
    centre = 1
    while centre != len(arr) - 1:
        left, right = centre - 1, centre + 1
        buffer = centre
        if arr[centre] == arr[right]:
            while arr[centre] == arr[right] and right != len(arr) - 1 :
                centre += 1
                right += 1

        if arr[left] < arr[centre] > arr[right]:
            pos_peaks['pos'].append(buffer)
            pos_peaks['peaks'].append(arr[centre])
        centre += 1
    return pos_peaks


def main():
    print(pick_peaks([2,1,3,1,2,2,2,2]))


if __name__ == '__main__':
    main()
