from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool
from mindexpo.db.models import Post

router = APIRouter(
    prefix="/blogs",
    tags=["blog"],
    responses={404: {"description": "Not found"}},
)

# # SQLite database setup
# sqlite_url = "sqlite:///./blog.db"
# engine = create_engine(
#     sqlite_url, connect_args={"check_same_thread": False}, poolclass=StaticPool
# )


# @router.on_event("startup")
# def on_startup():
#     SQLModel.metadata.create_all(engine)


# @router.on_event("shutdown")
# def on_shutdown():
#     SQLModel.metadata.drop_all(engine)


# # Dependency to get the database session
# def get_session() -> Session:
#     with Session(engine) as session:
#         yield session


# @router.post("/posts/", response_model=Post)
# def create_post(post: Post, session: Session = Depends(get_session)):
#     session.add(post)
#     session.commit()
#     session.refresh(post)
#     return post


# @app.get("/posts/{post_id}", response_model=Post)
# def read_post(post_id: int, session: Session = Depends(get_session)):
#     post = session.get(Post, post_id)
#     if not post:
#         raise HTTPException(status_code=404, detail="Post not found")
#     return post


# @app.put("/posts/{post_id}", response_model=Post)
# def update_post(post_id: int, post: Post, session: Session = Depends(get_session)):
#     existing_post = session.get(Post, post_id)
#     if not existing_post:
#         raise HTTPException(status_code=404, detail="Post not found")

#     for field, value in post.dict(exclude_unset=True).items():
#         setattr(existing_post, field, value)

#     session.commit()
#     session.refresh(existing_post)
#     return existing_post


# @app.delete("/posts/{post_id}", response_model=Post)
# def delete_post(post_id: int, session: Session = Depends(get_session)):
#     post = session.get(Post, post_id)
#     if not post:
#         raise HTTPException(status_code=404, detail="Post not found")
#     session.delete(post)
#     session.commit()
#     return post
