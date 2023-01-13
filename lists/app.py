import math
from typing import List


## https://leetcode.com/problems/palindrome-number/submissions/877133152/

def isPalindrome(x: int) -> bool:
    aux = [i for i in str(x)]
    aux.reverse()
    return str(x) == ''.join(aux)


# https://leetcode.com/problems/roman-to-integer/submissions/877230592/
def romanToInteger(s: str) -> int:
    chaveValue = { "I": 1,"V": 5,  "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    dupla = {"IV": 4, "IX": 9, "XL": 40, "XC":90, "CD": 400, "CM": 900}
    gatilhos = [ "I", "X", "C"]

    valor = 0
    value = 0
    while value < len(s):
            try:
                if s[value] in gatilhos:
                    par = f'{s[value]}{s[value+1]}'
                    valor += dupla[par]
                    value += 2
                    continue
                else:
                    valor += chaveValue[s[value]]
                value += 1
            except:
                valor += chaveValue[s[value]]
                value += 1
                continue
    return valor


#  https://leetcode.com/problems/happy-number/submissions/877251395/
def isHappy(self, n: int) -> bool:
    numberString = str(n)
    taxa = 4 if len(numberString) < 3 else len(numberString) + 2
    for i in range(taxa + 1):
        numberString = [x for x in str(numberString)]
        numberString = sum([int(i) ** 2 for i in numberString])
    return numberString == 1

# https://leetcode.com/problems/reverse-integer/submissions/877433104/
def reverse(x: int) -> int:
    numberString = str(x)
    numberString = numberString[::-1]
    if numberString[-1] == "-":
        numberString = numberString[0:-1]
        numberString = f'-{numberString}'
    if not ((-2 ** 31) <= int(numberString) <= (2 ** 31 - 1)):
        return 0
    if numberString[0] == 0:
        return int(numberString[1::])
    return int(numberString)
# https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/877627326/
def findMedianSortedArrays( nums1: List[int], nums2: List[int]) -> float:
    merglist = nums1 + nums2
    merglist.sort()
    length = len(merglist)
    id = math.floor(length / 2)
    if length == 1:
        return merglist[0]
    if length % 2 == 0:
        return math.trunc(merglist[id] + merglist[id - 1]) / 2
    return merglist[id]

# https://leetcode.com/problems/maximum-gap/submissions/877683060/
def maximumGap(nums: List[int]) -> int:
    gap = 0
    nums.sort()
    for key, value in enumerate(nums):
        aux = key + 1
        try:
            if (nums[aux] - value) > gap:
                gap = nums[aux] - value
        except:
            continue
    return gap
if __name__ == '__main__':
    print(findMedianSortedArrays([1, 3], [2]))
    print(reverse(-123))
    print(isPalindrome(121))
    print(maximumGap([3,6,9,1]))
    print(romanToInteger("MCMXCIV"))
    print(isHappy(19))