from configparser import SectionProxy
from sqlalchemy import *
from sqlalchemy_utils import *
from sqlalchemy.orm import *


def load(df):

    url = "mysql://root:password@localhost:3306/test"
    engine = create_engine(url)
    session = Session(engine)
    if not database_exists(url):
        create_database(url)

    Base = declarative_base()

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
        Commune                 = Column(String(50))
        CodeDepartement         = Column(String(2))
        CodeCommune             = Column(String)
        PrefixeSection          = Column(String)
        Section                 = Column(String)
        NoPlan                  = Column(Integer)
        NoVolume                = Column(String)
        Lot1                    = Column(String)
        CarrezLot1              = Column(Float)
        Lot2                    = Column(String)
        CarrezLot2              = Column(Float)
        Lot3                    = Column(String)
        CarrezLot3              = Column(Float)
        Lot4                    = Column(String)
        CarrezLot4              = Column(Float)
        Lot5                    = Column(String)
        CarrezLot5              = Column(Float)
        NombreLots              = Column(Integer)
        CodeTypeLocal           = Column(Integer)
        TypeLocal               = Column(String)
        SurfaceReelleBati       = Column(Integer)
        NombrePiecesPrincipales = Column(Integer)
        NatureCulture           = Column(String)
        NatureCultureSpeciale   = Column(String)
        SurfaceTerrain          = Column(Integer)

    Base.metadata.create_all(engine)