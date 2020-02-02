import oldmax
from random import randint
users = [
    {
        'name': 'Jack',
        'password': '123',
        'age':  10
    },
    {
        'name': 'Suka',
        'password': '222',
        'age': 18
    },
    {
        'name': 'Pring',
        'password': '#3FzxV)',
        'age': 22
    }
]

for i in range(100):
    users.append(
        {
            'name': oldmax.generate_name(),
            'password': oldmax.generate_name(),
            'age': randint(1, 200)
        }
    )
for user in users:
    print(user)
print("Oldfag is", oldmax.oldmax(users)['name'], "hi is", oldmax.oldmax(users)['age'], "years old!")
