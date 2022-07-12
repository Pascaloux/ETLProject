from sqlalchemy import *
from sqlalchemy_utils import *
from sqlalchemy.orm import *
from base import Base


class DateValeursFoncieres(Base):
    __tablename__ = "DateValeursFoncieres"
    DateMAJ       = Column(String(20),primary_key=True)


class ValeursFoncieres(Base):
    __tablename__ = "ValeursFoncieres"
    IdValeurFonciere        = Column(Integer,primary_key=True)
    NoDisposition           = Column(Integer)
    DateMutation            = Column(Date)
    NatureMutation          = Column(String(40))
    ValeurFonciere          = Column(Float)
    NoVoie                  = Column(Integer)
    BTQ                     = Column(String(1))
    TypeVoie                = Column(String(4))
    CodeVoie                = Column(String(4))
    Voie                    = Column(String(100))
    CodePostal              = Column(Integer)
    Commune                 = Column(String(45))
    CodeDepartement         = Column(String(3))
    CodeCommune             = Column(Integer)
    PrefixeSection          = Column(Integer)
    Section                 = Column(String(2))
    NoPlan                  = Column(Integer)
    NoVolume                = Column(String(10))
    Lot1                    = Column(String(10))
    CarrezLot1              = Column(Float)
    Lot2                    = Column(String(10))
    CarrezLot2              = Column(Float)
    Lot3                    = Column(String(10))
    CarrezLot3              = Column(Float)
    Lot4                    = Column(String(10))
    CarrezLot4              = Column(Float)
    Lot5                    = Column(String(10))
    CarrezLot5              = Column(Float)
    NombreLots              = Column(Integer)
    CodeTypeLocal           = Column(Integer)
    TypeLocal               = Column(String(25))
    SurfaceReelleBati       = Column(Integer)
    NombrePiecesPrincipales = Column(Integer)
    NatureCulture           = Column(String(2))
    NatureCultureSpeciale   = Column(String(5))
    SurfaceTerrain          = Column(Integer)


class Bank_cap_temp(Base):
    __tablename__ = "Bank_capitalisation"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer,primary_key=True)
    Name = Column(String(500))
    Market_Cap = Column(Float)
    identifier = column_property(Name + " " + cast( Market_Cap,String))

class Bank_cap_final(Base):
    __tablename__ = "Bank_cap_final"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer,primary_key=True)
    Name = Column(String(500))
    Market_Cap = Column(Float)
    identifier = column_property(Name + " " +cast( Market_Cap,String))

class Taux(Base):
    __tablename__ = "taux"
    id = Column(Integer,primary_key=True)
    devise= Column(String(4))
    valeur = Column(Float)