word = input("Enter any word -->  ")
len(word)
nums = [0]
for unak in range(len(word)):
    num = int(input(f"Enter number {unak + 1} : "))
    nums += [num]
print(nums)
ave = num * len(word)
print("the length of words ", len(word))
print(f"The average of the numbers is {ave}")
print(f"The length of word '{word}'")