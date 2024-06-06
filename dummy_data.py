import os ,django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
from products.models import Product, ProductImages, Brand, Review  
import random
from django.utils.text import slugify
from django.contrib.auth.models import User



fake=Faker()

def seed_brands(num_brands):
    imgs =['01.jpg','02.jpg','03.jpg','04.jpg','05.jpg','06.jpg', ]
    name = [fake.company() for _ in range(num_brands+20)] # Generate a fake company name
  
    for _ in range(num_brands):
        brand = Brand.objects.create(
            name=name[_],
            image=f'brand/{imgs[random.randint(0,5)]}',
        )
    
    print('brand addec successfully')



def seed_product(n):
    imgs =['01.jpg','02.jpg','03.jpg','04.jpg','05.jpg','06.jpg',
           '07.jpg','08.jpg','09.jpg','10.jpg','11.jpg','12.jpg',
           '13.jpg','14.jpg','15.jpg','16.jpg','17.jpg','18.jpg',
           '19.jpg','20.jpg',
        ]
    
    
    brand =Brand.objects.all()
    for _ in range(n):
        name = [fake.company() for _ in range(n+200)] # Generate a fake company name
       
        
        Product.objects.create(
            brand =brand[random.randint(0,len(brand)-1)] ,
            name = name[_],
            flag=fake.random_element(elements=('New', 'Sale', 'Feature')),
            image = f'product/{imgs[random.randint(0,19)]}',
            price = fake.random_number(digits=2),
            sku=fake.unique.random_number(digits=5),
            subtitle=fake.sentence(nb_words=60),
            description=fake.paragraph(nb_sentences = 80),
            quantity = random.randint(1, 100)
        )
    print('products added successfully')

def seed_review():
    users = list(User.objects.all())
    products = Product.objects.all()

    for product in products:
        for _ in range(3):
            Review.objects.create(
                user=random.choice(users),
                product=product,
                content=fake.sentence(nb_words=45),
                rate=fake.random_element(elements=[1, 2, 3, 4, 5]),
            )
    print('Added 3 reviews for each product successfully.')


def seed_product_img():
    imgs = [
        '01.jpg', '02.jpg', '03.jpg', '04.jpg', '05.jpg', '06.jpg',
        '07.jpg', '08.jpg', '09.jpg', '10.jpg', '11.jpg', '12.jpg',
        '13.jpg', '14.jpg', '15.jpg', '16.jpg', '17.jpg', '18.jpg',
        '19.jpg', '20.jpg'
    ]
    
    products = Product.objects.all()

    for product in products:
        for _ in range(4):
            ProductImages.objects.create(
                product=product,
                image=f'productimage/{random.choice(imgs)}',
            )
    print('4 images added for each product successfully.')

# seed_brands(30)
seed_product(100)
seed_review()
seed_product_img()