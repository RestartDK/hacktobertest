users = [
    'Anna',
    'velocitatem',
    'laura',
    'velocitatem',
    'torkuno',
    'isabel',
    'zaid'
]

def greet(user):
    print(f'Hello {user}!')


if __name__ == "__main__":
    [greet(user) for user in users]
