from pydantic import BaseModel, Field
from typing import Annotated, Literal

class apiOutput(BaseModel):
    predicted_category: Annotated[Literal['High', 'Medium', 'Low'], Field(..., description='Predicted category of the user', example='High')]