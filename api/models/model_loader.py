from . import models
from ..dependencies.database import engine

#Creating tables
def index():
    models.Base.metadata.create_all(engine)