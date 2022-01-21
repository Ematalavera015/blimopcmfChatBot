from pydantic import BaseModel, Field, constr
from typing import Optional

class FromSchema(BaseModel):
    id: int = Field(..., title="ID del usuario")
    is_bot: bool = Field(..., title="Es bot o no")
    first_name: constr(strict=True) = Field(..., title="Nombre del usuario")
    username: constr(strict=True) = Field(..., title="Nombre de usuario")
    language_code: constr(strict=True) = Field(..., title="Idioma")


class ChatSchema(BaseModel):
    id: int = Field(..., title="ID del chat")
    first_name: constr(strict=True) = Field(..., title="Nombre del usuario")
    username: Optional[str] = Field(None , title="Nombre de usuario")
    type: constr(strict=True) = Field(..., title="Tipo de chat")


class MessageSchema(BaseModel):
    message_id: int = Field(..., title="ID del mensaje")
    _from: FromSchema = Field(..., title="Enviado por")
    chat: ChatSchema = Field(..., title="Chat")
    date: int = Field(..., title="Fecha numerica")
    text: constr(strict=True, max_length=4096) = Field(..., title="Texto del mensaje")


class TelegramMessageSchema(BaseModel):
    update_id: int = Field(..., title="Update ID")
    message: MessageSchema = Field(..., title="Mensaje")

    @classmethod
    def get_example(cls):
        return cls.Config.schema_extra["example"]

    class Config:
        schema_extra = {
            "example": {
                "update_id": 56918934,
                "message": {
                    "message_id": 86,
                    "from": {
                        "id": 1084783282,
                        "is_bot": False,
                        "first_name": "faqn2",
                        "username": "faQn2s",
                        "language_code": "es"
                    },
                    "chat": {
                        "id": 1084783282,
                        "first_name": "faqn2",
                        "username": "faQn2s",
                        "type": "private"
                    },
                    "date": 1641925988,
                    "text": "Mensaje"
                }
            }
        }
