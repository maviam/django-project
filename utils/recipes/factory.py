from random import randint
from faker import Faker

def rand_ratio():
    return randint(840, 900), randint(473, 573)

def number_words(text):
    new_text = text[0:175] + " ..."
    return new_text 

fake = Faker('pt_BR')
# print(signature(fake.random_number))

def make_recipe():
    return {
        'title': fake.sentence(nb_words=3),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
        'preparation_steps': number_words(fake.text(300)),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % (640,360),
        }
    }
if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())