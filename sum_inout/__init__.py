from pydantic import BaseModel


class SumModel(BaseModel):
    """
        Information that comes from user input to make addition of x and y
    """

    x: float
    y: float

    class Config:
        title = 'Sum Input Data'
