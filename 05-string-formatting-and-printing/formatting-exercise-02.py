header1 = "Name"
header2 = "Age"
header3 = "salary"
name = "John"
age = 22
salary = 15.15151515
print(f"| {header1:15} | {header2:5} | {header3:12} |")
print("-" * 42)
print(f"| {name:15} | {age:5} | {salary:12.2f} |")
print(f"| {name:15} | {age:5} | {salary:<12.2f} |")

person1 = {"name": "A", "age": 2, "salary": 100}
person2 = {"name": "B", "age": 4, "salary": 50}
person3 = {"name": "C", "age": 6, "salary": 50}
personList = [person1, person2, person3]
for person in personList:
    print(f"")

