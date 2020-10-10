def intersection(arrays):
    
    intersection = {}
    result = []
    
    for counter, arr in enumerate(arrays):
        
        for num in arr:
            if intersection.get(num) is not None and counter > 0:
                intersection[num] += 1
            
            elif intersection.get(num) is None and counter == 0:
                intersection[num] = 1

            else:
                continue

    for value in intersection:
        if intersection[value] == len(arrays):
            result.append(value)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
