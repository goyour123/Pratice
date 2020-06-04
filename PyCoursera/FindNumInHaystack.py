import re

haystack = open("target/regex_sum_261104.txt")

sum = 0
for line in haystack:
    line = line.rstrip()
    nums = re.findall('[0-9]+', line)
    if len(nums) == 0:
        continue
    else:
        for index in nums:
            sum += int(index)

print sum