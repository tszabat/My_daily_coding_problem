# Given a list of numbers and a number k, return True whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

def two_k_addable_items(k):
    given_list = [10, 15, 3, 7]
    for item_1 in given_list:
        for item_2 in given_list:
            if item_1 + item_2 == k:
                return True

print(two_k_addable_items(26))

