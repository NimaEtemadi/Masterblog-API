# def triple(value):
#     return 3 * value


# things = [2, 5, 9]

# things3 = map(triple, things)
# print(list(things3))


# //////////////////////////////////////////////////////////////////


# def double(value):
#     return 2*value


# lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

# greeting_doubled = map(double, lst)

# print(list(greeting_doubled))


# /////////////////////////////////////////////////////////////////////////

# def is_even(num):
#     return num % 2 == 0

# def keep_evens(nums):
#     new_seq = filter(is_even, nums)
#     return list(new_seq)

# print(keep_evens([3, 4, 6, 7, 0, 1]))



# ////////////////////////////////////////////////////////////////////////////


# things = [2, 5, 9]

# yourlist = [value * 2 for value in things]

# print(yourlist)

# ///////////////////////////////////////////////////////////////

# def keep_evens(nums):
#     new_list = [num for num in nums if num % 2 == 0]
#     return new_list

# print(keep_evens([3, 4, 6, 7, 0, 1]))


# ///////////////////////////////////////////////////////////////////


def is_even(num):
    return num % 2 == 0

def multiply(num):
    return num * 2

things = [3, 4, 6, 7, 0, 1]

# chaining together filter and map:
# first, filter to keep only the even numbers
# double each of them

print(list(map(multiply, filter(is_even, things))))

# equivalent version using list comprehension
print([x * 2 for x in things if x % 2 == 0])