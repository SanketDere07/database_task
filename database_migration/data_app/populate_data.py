from .models import User, Address, Item

def populate_data():
    user1 = User.objects.create(name='John')
    user2 = User.objects.create(name='Alice')

    Address.objects.create(email_address='john@example.com', user=user1)
    Address.objects.create(email_address='alice@example.com', user=user2)

    Item.objects.create(name='Book', description='A good book', user=user1)
    Item.objects.create(name='Laptop', description='A powerful laptop', user=user2)

if __name__ == '__main__':
    populate_data()
