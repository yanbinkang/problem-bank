"""
Finish the solution so that it takes an input 'n' (integer) and returns a string that is the decimal representation of the number grouped by commas after every 3 digits.

Assume: 0 <= n < 1000000000

       1  ->           "1"
      10  ->          "10"
     100  ->         "100"
    1000  ->       "1,000"
   10000  ->      "10,000"
  100000  ->     "100,000"
 1000000  ->   "1,000,000"
35235235  ->  "35,235,235"
"""

def group_by_commas(string):
    rev = string[::-1]
    if len(rev) <= 3:
        return rev[::-1]
    else:
        return group_by_commas(rev[3:][::-1]) + ","  + rev[:3][::-1]


print group_by_commas("1")
print group_by_commas("10")
print group_by_commas("100")
print group_by_commas("1000")
print group_by_commas("10000")
print group_by_commas("100000")
print group_by_commas("1000000")
print group_by_commas("35235235")
