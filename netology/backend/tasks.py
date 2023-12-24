from django.core.mail import EmailMultiAlternatives
from django.core.validators import URLValidator
from requests import get
from yaml import Loader
from yaml import load as load_yaml

from netology.celery import application as celery
from netology.models import (
    Category,
    Parameter,
    Product,
    ProductInfo,
    ProductParameter,
    Shop,
)


@celery.task
def send_email(subject, body, from_email, to):
    print(f"Send email to {to}")
    email = EmailMultiAlternatives(subject, body, from_email, to)
    email.send()


@celery.task
def do_import(url, user_id):
    print("Import in process")
    validate_url = URLValidator()
    validate_url(url)
    stream = get(url).content

    data = load_yaml(stream, Loader=Loader)

    shop, _ = Shop.objects.get_or_create(name=data["shop"], user_id=user_id)
    for category in data["categories"]:
        category_object, _ = Category.objects.get_or_create(
            id=category["id"], name=category["name"]
        )
        category_object.shops.add(shop.id)
        category_object.save()
    ProductInfo.objects.filter(shop_id=shop.id).delete()
    for item in data["goods"]:
        product, _ = Product.objects.get_or_create(
            name=item["name"], category_id=item["category"]
        )

        product_info = ProductInfo.objects.create(
            product_id=product.id,
            external_id=item["id"],
            model=item["model"],
            price=item["price"],
            price_rrc=item["price_rrc"],
            quantity=item["quantity"],
            shop_id=shop.id,
        )
        for name, value in item["parameters"].items():
            parameter_object, _ = Parameter.objects.get_or_create(name=name)
            ProductParameter.objects.create(
                product_info_id=product_info.id,
                parameter_id=parameter_object.id,
                value=value,
            )
        print("Finished")
