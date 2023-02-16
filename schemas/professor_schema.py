from typing import Optional
from core.configs import settings
#from typing import Optional
from pydantic import BaseModel as SCBaseModel

class ProfessorSchema(SCBaseModel):
        
        id: Optional[int] 
        nome : str 
        email : str 

        class Config():
            orm_mode = True