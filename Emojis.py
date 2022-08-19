# Python program to print Emojis.
'''
There are multiple ways we can print the Emojis in Python. Let’s see how to print Emojis with Unicodes,
CLDR names and emoji module.
'''
# Using Unicodes:

# grinning face
print("\U0001f600")
# grinning squinting face
print("\U0001F606")
# rolling on the floor laughing
print("\U0001F923")

# Using CLDR short name:

# grinning face
print("\N{grinning face}")
# slightly smiling face
print("\N{slightly smiling face}")
# winking face
print("\N{winking face}")

# Using emoji module:

# import emoji module
# import emoji

# print(emoji.emojize(":grinning_face_with_big_eyes:"))
# print(emoji.emojize(":winking_face_with_tongue:"))
# print(emoji.emojize(":zipper-mouth_face:"))