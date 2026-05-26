# user = input("Enter a name:")
# print("good Afternoon, " + user + "!")
# #or
# print(f"good Afternoon, {user}!")

letter = '''Dear <|NAME|>,
You are selected!
Date: <|DATE|>'''

print(letter.replace("<|NAME|>", "Ayushi").replace("<|DATE|>", "20/06/2024"))