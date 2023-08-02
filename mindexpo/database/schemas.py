from datetime import date
from enum import Enum
from typing import List, Optional

from enum import Enum
from pydantic import BaseModel, EmailStr, Field, HttpUrl, ValidationError


class User(BaseModel):
    email: EmailStr
    website: HttpUrl


# Invalid email
try:
    user = User(email="jdoe@gmial.com", website="https://www.example.com")
    print(user)
except ValidationError as e:
    print(str(e))


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"


class Address(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str


class Person(BaseModel):
    first_name: str = Field(..., min_length=3)
    last_name: str = Field(..., min_length=3)
    gender: Gender
    age: Optional[int] = Field(None, ge=0, le=120)
    interests: List[str]
    address: Address


# class UserProfile(BaseModel):
#     username: Field(..., min_length=3)
#     location: Optional[str] = None
#     subscribed_newsletter: bool = True

# user = UserProfile(username="jdoe")
# print(user) # nickname='jdoe' location=None subscribed_newsletter=True

# # Valid
# person = Person(
#     first_name="John",
#     last_name="Doe",
#     gender=Gender.MALE,
#     birthdate="1991-01-01",
#     interests=["travel", "sports"],
# )
# # first_name='John' last_name='Doe' gender=<Gender.MALE: 'MALE'> birthdate=datetime.date(1991, 1, 1)
# interests=['travel', 'sports']
# print(person)

# Valid
person = Person(
    first_name="John",
    last_name="Doe",
    gender=Gender.MALE,
    age=27,
    interests=["travel", "sports"],
    address={
        "street_address": "12 Squirell Street",
        "postal_code": "424242",
        "city": "Woodtown",
        "country": "US",
    },
)
print(person)
