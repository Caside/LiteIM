import random

def oldmax(users):
    if len(users) == 0:
        return None
    else:
        m = users[0]['age']
        oldest_user = users[0]
        for user in users[1:]:
            if user['age'] > m:
                m = user['age']
                oldest_user = user
        return(oldest_user)

def generate_name():
    name_len = random.randint(1, 20)
    name = []
    for i in range(name_len):
        name.append(random.choice('йцукенгшщзхъэждлорпавыфячсмитьбю1234567890'))
    return ''.join(name)
