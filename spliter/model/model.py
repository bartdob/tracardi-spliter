from pydantic.main import BaseModel


class Spliter(BaseModel):
    message: str
    dot: str

