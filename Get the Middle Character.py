# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd,
# return the middle character. If the word's length is even, return the middle 2 characters.
#
# #Examples:
#
# Kata.getMiddle("test") should return "es"
#
# Kata.getMiddle("testing") should return "t"
#
# Kata.getMiddle("middle") should return "dd"
#
# Kata.getMiddle("A") should return "A"
# return a str

def get_middle(s):
    return s[(len(s) - 1) // 2:(len(s) + 2) // 2]






print(get_middle("testing"))
# ,"t")
print(get_middle("middle"))
      # ,"dd")