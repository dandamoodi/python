# single quotes
print('spam eggs')

# double quotes
print("spam eggs")

# to escape use \
print('doesn\'t') # doesn't

# here \n means newline!
print('C:\some\name')
''''C:\some
        ame'''

# note the r before the quote, for printing the raw strings
print(r'C:\some\name')

# Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
print('Py' 'thon') # 'Python'

# Above only works with two literals though, not with variables or expressions:
prefix = 'Py'
prefix 'thon'  # can't concatenate a variable and a string literal

# For long strings:
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

# Strings can be indexed
word = 'python'
# character in position 0
print(word[0]) # p
# character in position 5
print(word[5]) # n

#String slicing
# characters from position 0 (included) to 2 (excluded)
print(word[0:2]) # 'Py'
print(word[2:5]) # 'tho'

# s[:i] + s[i:] is always equal to s:
i=2
print(word[:i] + word[i:] == word) # True

# out of range slice indexes are handled gracefully when used for slicing:
print(word[4:42]) # 'on'


#Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error:
word[0] = 'J' # TypeError: 'str' object does not support item assignment

# length of string
print(len(word))

