from core.configs import settings
from pydantic import BaseModel as SCBaseModel

class AlunoSchema(SCBaseModel):
      #  __tablename__ = 'alunos'

        id: int 
        nome : str 
        email : str 

        class config():
            orm_mode = True