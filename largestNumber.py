import itertools

# initializing the list
list_num = [34, 46, 11, 787, 777, 9]

num_combinations = []

# permutations
for permutation in itertools.permutations(str(number) for number in list_num):
   num_combinations.append(''.join(permutation))

#   print(result)

largest_num = max(num_combinations, key=int)

print(int(largest_num))