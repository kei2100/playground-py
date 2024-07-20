# 色々な in を使って、ある文字が母音かどうかを判定する

letter = "o"
vowel_set = {"a", "i", "u", "e", "o"}
print(letter in vowel_set)
# True

vowel_list = ["a", "i", "u", "e", "o"]
print(letter in vowel_list)
# True

vowel_tuple = ("a", "i", "u", "e", "o")
print(letter in vowel_tuple)
# True

vowel_dict = {"a": "apple", "i": "ink", "u": "umbrella", "e": "elephant", "o": "orange"}
print(letter in vowel_dict)
# True

vowel_str = "aiueo"
print(letter in vowel_str)
# True
