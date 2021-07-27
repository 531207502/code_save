import re
phone='010-87663522'
result=re.match('(\d{3}|\d{4})-(\d{8})$',phone)
print(result)
print(result.group(1))
print(result.group(2))
test1="abcjhashduiqwdnjaksbneqwufccbqhewqqwedsahdhaskqwedhsajkdahoiqw3chasjkdhasjkqwe111"
result1=re.search('qw\w',test1)
print(result1)
print(result1.group())
print(result1.start())
print(result1.end())
result2=re.findall('qw\w',test1)
print(result2)
test2="92173128s\n\t13792ajdkashiqueqw"
result3=re.search('\\t\\w',test2)
print(result3.group())