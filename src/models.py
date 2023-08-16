import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    UserID = Column(Integer, primary_key=True)
    Username = Column(String(50))
    Email = Column(String(100))
    FullName = Column(String(100))
    Bio = Column(String(250))
    ProfileImage = Column(String(250))

class Post(Base):
    __tablename__ = 'post'
    PostID = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey('user.UserID'))
    Image = Column(String(250))
    Caption = Column(String(250))
    Likes = Column(Integer)
    Comments = Column(Integer)

class Comment(Base):
    __tablename__ = 'comment'
    CommentID = Column(Integer, primary_key=True)
    PostID = Column(Integer, ForeignKey('post.PostID'))
    UserID = Column(Integer, ForeignKey('user.UserID'))
    Text = Column(String(250))

class Follow(Base):
    __tablename__ = 'follow'
    FollowerID = Column(Integer, primary_key=True)
    FollowingID = Column(Integer, ForeignKey('user.UserID'))

class Like(Base):
    __tablename__ = 'like'
    LikeID = Column(Integer, primary_key=True)
    PostID = Column(Integer, ForeignKey('post.PostID'))
    UserID = Column(Integer, ForeignKey('user.UserID'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
