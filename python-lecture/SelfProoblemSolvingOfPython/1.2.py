# Q3. Student Marks (Lists, Tuples, List Comprehension)
# Store marks of 10 students in a list. Using list comprehension:

# Create a list of students who passed (≥ 40).
# Add 5 grace marks to students scoring between 35 and 39.
# Find the highest, lowest, and average marks.
# Store (name, marks) pairs as tuples and sort them by marks.

from random import randint

markse = [randint(0,100) for i in range(10)]

passesdList = [i for i in markse if i >=  40 ]

addGracelList = [m+5  if m >= 35 and m<= 49 else m for m  in markse]

print(markse)
print(passesdList)
print(addGracelList)
print("Mininum marks : " ,min(addGracelList) , " , Maximum Marks : ", max(addGracelList) , " ,average : " , sum(addGracelList) // len((addGracelList)))

records  = {}

count = 1
for i in addGracelList:
    name   = input(f"enter Student Name {count}: ")
    records[name] = i
    count +=1 


print(records)

