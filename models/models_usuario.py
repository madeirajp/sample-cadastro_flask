#coding: utf-8

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from database import Base

class Usuario(Base):
    __tablename__ = 'tbl_usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    login = Column(String(30))
    password = Column(String(20))

    colaborador_id = Column(Integer, ForeignKey('tbl_colaboradores.id'))
    colaborador = relationship("Colaborador", backref=backref('usuarios', order_by=id))

    def __init__(self, nome, login, password):
        self.nome = nome
        self.login = login
        self.password = password

    def __repr__(self):
       return "<Usuario('%s', '%s','%s', '%s')>" % (self.id, self.nome, self.login, self.password)
