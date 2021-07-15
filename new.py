def convert(nums):

    digits = {"0":"zero", "1":"one", "2":"two", "3":"three",
             "4":"four", "5":"five", "6":"six", "7":"seven",
             "8":"eight", "9":"nine"}
    
    for num in nums:
        if num in digits:
            print(digits.get(num), end= ' ')

val = input("Enter your number: ")
convert(val)