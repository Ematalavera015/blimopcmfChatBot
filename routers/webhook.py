from fastapi import APIRouter, Response, Body
from schemas.model.telegram import TelegramMessageSchema
from services.dialogflow import DialogFlowService
from services.bot import BotService

api = APIRouter(prefix="", tags=["webhook"])

print("API ",api)

@api.post(path="/webhook", status_code=200)
async def webhook(request: TelegramMessageSchema = Body(..., example=TelegramMessageSchema.get_example())):
    text_response = await DialogFlowService.message(text=request.message.text)
    content, status_code = await BotService.reply_message(chat_id=request.message.chat.id, text=text_response)
    return Response(content="Message sent", status_code=status_code)

