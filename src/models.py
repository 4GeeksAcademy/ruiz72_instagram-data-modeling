import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    UsuarioID = Column(Integer, primary_key=True)
    NombreUsuario = Column(String(100))
    Email = Column(String(100))
    NombreCompleto = Column(String(100))
    Biografia = Column(String(250))
    ImagenPerfil = Column(String(250))
    publicaciones = relationship('Publicacion', back_populates='usuario')
    comentarios = relationship('Comentario', back_populates='usuario')
    seguidores = relationship('Seguir', foreign_keys='Seguir.SiguiendoID', back_populates='siguiendo')
    siguiendo = relationship('Seguir', foreign_keys='Seguir.SeguidorID', back_populates='seguidor')

class Publicacion(Base):
    __tablename__ = 'publicacion'
    PublicacionID = Column(Integer, primary_key=True)
    UsuarioID = Column(Integer, ForeignKey('usuario.UsuarioID'))
    Imagen = Column(String(250))
    Descripcion = Column(String(250))
    MeGusta = Column(Integer)
    Comentarios = Column(Integer)
    usuario = relationship('Usuario', back_populates='publicaciones')
    comentarios = relationship('Comentario', back_populates='publicacion')

class Comentario(Base):
    __tablename__ = 'comentario'
    ComentarioID = Column(Integer, primary_key=True)
    PublicacionID = Column(Integer, ForeignKey('publicacion.PublicacionID'))
    UsuarioID = Column(Integer, ForeignKey('usuario.UsuarioID'))
    Texto = Column(String(250))
    usuario = relationship('Usuario', back_populates='comentarios')
    publicacion = relationship('Publicacion', back_populates='comentarios')

class Seguir(Base):
    __tablename__ = 'seguir'
    SeguidorID = Column(Integer, primary_key=True)
    SiguiendoID = Column(Integer, ForeignKey('usuario.UsuarioID'))
    seguidor = relationship('Usuario', foreign_keys=[SeguidorID], back_populates='seguidores')
    siguiendo = relationship('Usuario', foreign_keys=[SiguiendoID], back_populates='siguiendo')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
