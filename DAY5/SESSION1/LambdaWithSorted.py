students=[
    ("Aslaha",25),
    ("Dinix",26),
    ("Susanne",25),
]

sorted_students=sorted(
    students,
    key=lambda x:x[1]
)
print(sorted_students)