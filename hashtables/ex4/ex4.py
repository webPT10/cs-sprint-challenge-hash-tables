def has_negatives(a):
    
    digits = {}
    result = []

    for num in a:

        if ( num * -1 ) in digits:

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
