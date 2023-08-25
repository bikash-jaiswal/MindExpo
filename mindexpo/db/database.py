from sqlalchemy import create_engine, Column, Integer, String, DateTime,select
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
Base = declarative_base()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class BlogPost(Base):
    __tablename__ = "blogposts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.date)

    def __repr__(self):
        return "<BlogPost(id={self.id}, title={self.title}, content={self.content})>"


Base.metadata.create_all(bind=engine)


def add_blog(new_post: BlogPost):
    with SessionLocal(engine) as session:
        existing_blog = session.execute(select(BlogPost).filter(BlogPost.title == new_post.title, BlogPost.created_at == new_post.create_at)).scalar()
        if existing_blog:
            print("Book has already been added")
            return
        session.add(new_post)
        session.commit()
        session.refresh(new_post)  # Refresh the object to get the updated values
        print("Added new blog post:", new_post)
    

    
