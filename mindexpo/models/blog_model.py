from pydantic import BaseModel, EmailStr, root_validator

class PostBase(BaseModel):
    title: str
    content: str

    def excerpt(self) -> str:
        return f"{self.content[:140]}..."

# a POST endpoint to create a new post.
class PostCreate(PostBase):
    pass

class PostPublic(PostBase):
    id: int

   
class PostDB(PostBase):
    id: int
    nb_views: int = 0


class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    password_confirmation: str

    @root_validator()
    def passwords_match(cls, values):
        password = values.get("password")
        password_confirmation = values.get("password_confirmation")
        if password_confirmation != password:
            raise ValueError("Passwords don't match")
        return values