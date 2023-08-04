"""
In this file we will have reusable functions to interact with the data in the database.

CRUD comes from: Create, Read, Update, and Delete.
"""

from sqlalchemy.orm import Session

from mindexpo.db import models


def get_single_post(db: Session, post_id: int):
    return db.query(models.Blog).filter(models.Blog.id == post_id).first()
