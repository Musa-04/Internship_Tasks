# Lambda with map, filter, sort

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)

cubes = list(map(lambda x: x**3, numbers))
print(cubes)


nums = [10, 20, 30, 45, 55]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)


employees = [
    {"name": "joice", "salary": 50000},
    {"name": "lochitha", "salary": 70000},
    {"name": "Aliya", "salary": 40000}
]

employees.sort(key=lambda e: e["salary"], reverse=True)
print(employees)
