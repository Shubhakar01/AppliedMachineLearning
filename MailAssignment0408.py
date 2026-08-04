def Quick_Sort_using_lambda(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = list(filter(lambda x: x < pivot, arr[1:]))
        greater_than_pivot = list(filter(lambda x: x >= pivot, arr[1:]))
        return Quick_Sort_using_lambda(less_than_pivot) + [pivot] + Quick_Sort_using_lambda(greater_than_pivot)

def square_using_lambda(n):
    return list(map(lambda x: x**2, n))

def square_using_list_comprehension(n):
    return [x**2 for x in n]

def square_of_even_numbers_using_list_comprehension(n):
    return [x**2 for x in n if x % 2 == 0]

def code_explanation():
    d={'person':2,'cat':4,'spider':8}
    for animal in d:
        legs=d[animal]
        print("A %s has %d legs" % (animal,legs)) 
        # Iterating through dictionary and printing the values using string formatting
        # %s for string and %d for integer values

def main():
    print(Quick_Sort_using_lambda([3, 6, 8, 10, 1, 2, 1]))
    print(square_using_lambda([1, 2, 3, 4, 5]))
    print(square_using_list_comprehension([1, 2, 3, 4, 5]))
    print(square_of_even_numbers_using_list_comprehension([1, 2, 3, 4, 5, 6]))
    code_explanation()
main()

