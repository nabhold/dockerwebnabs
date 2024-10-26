import factory
from factory.django import DjangoModelFactory
from faker import Faker
from django.contrib.auth import get_user_model
from .models import Profile

fake = Faker()
User = get_user_model()


class CustomUserFactory(DjangoModelFactory):
    """
    Factory for generating CustomUser instances.
    """

    class Meta:
        model = User

    email = factory.LazyAttribute(lambda _: fake.email())
    username = factory.LazyAttribute(lambda _: fake.user_name())
    first_name = factory.LazyAttribute(lambda _: fake.first_name())
    last_name = factory.LazyAttribute(lambda _: fake.last_name())
    date_of_birth = factory.LazyAttribute(lambda _: fake.date_of_birth())
    is_active = True
    is_admin = False


class ProfileFactory(DjangoModelFactory):
    """
    Factory for generating Profile instances.
    """

    class Meta:
        model = Profile

    user = factory.SubFactory(CustomUserFactory)
    profile_image = factory.django.ImageField(color="blue")
    bio = factory.LazyAttribute(lambda _: fake.paragraph(nb_sentences=3))
    phone_number = factory.LazyAttribute(lambda _: fake.phone_number())
    website = factory.LazyAttribute(lambda _: fake.url())
    address = factory.LazyAttribute(lambda _: fake.address())
    date_of_birth = factory.LazyAttribute(lambda _: fake.date_of_birth())
