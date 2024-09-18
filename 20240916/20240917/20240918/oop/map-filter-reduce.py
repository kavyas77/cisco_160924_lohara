nums = [2,3,4]
#map syntax
#map(<func>,iterable)
nums_sqr = list(map(lambda num: num**2,nums))
print(nums_sqr)

nums_even = list(filter(lambda num: num%2==0,nums))
print(nums_even)


from functools import reduce
nums = [10,20,30,41]
nums_sum = reduce((lambda s,num: s+num),nums,0)
print(nums_sum)
nums_product = reduce((lambda p,num: p*num),nums,1)
print(nums_product)

import sys
nums_min = reduce(lambda m,num: min(m,num), nums,sys.maxsize)
nums_max = reduce(lambda m,num: max(m,num), nums,-sys.maxsize)
print(nums_min,nums_max)

nums_min = reduce(min, nums)
nums_max = reduce(max, nums)
print(nums_min,nums_max)




