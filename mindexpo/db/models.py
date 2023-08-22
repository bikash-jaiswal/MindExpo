# from typing import Optional, List
# from sqlmodel import SQLModel, Field, Session, create_engine
# from datetime import datetime


# class Post(SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     title: str = Field(..., nullable=False)
#     content: Optional[str] = Field(None, nullable=True)
#     published_date: datetime = Field(default_factory=datetime.now)

# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"

# engine = create_engine(sqlite_url, echo=True)


# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)


# def create_blog_post():
#     post1 = Post(
#         id=1,
#         title="First blog",
#         content="<h3> This is first blog</h3>",
#     )
#     post2 = Post(id=2, title="second blog", content="<h3> This is Second blog</h3>")
#     post3 = Post(id=3, title="third blog", content="<h3> This is Third blog</h3>")

#     with Session(engine) as session:
#         session.add(post1)
#         session.add(post2)
#         session.add(post3)
#         session.commit()
#         session.close()


# def run_db():
#     create_db_and_tables()
#     create_blog_post()


# if __name__ == "__main__":
#     run_db()
