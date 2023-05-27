# Ex 1:

name = input("Enter name: ")
age = input("Enter age: ")
organization = input("Enter organization: ")
entrance_year = int(input("Enter entrance year: "))
current_year = int(input("Enter current year: "))

print("My name is", name)
print("I am", age, "year(s) old")
print("I entered", organization, "in", entrance_year)
print("I have spent", current_year - entrance_year, "year(s) in", organization)

# Ex 2:
Text = "My name is 26"
Text_list = Text.split()
Text_count = len(Text_list)
print(Text)
print("The text has", Text_count, "Word(s).")

New_Text = Text.replace("name", "current age")
Ntext_list = New_Text.split()
Ntext_count = len(Ntext_list)
print(New_Text)
print("The new text has", Ntext_count, "Word(s).")

