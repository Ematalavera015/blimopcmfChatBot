from fastapi import APIRouter, Body, Response, HTTPException, status
from schemas.model.webhook import SetWebhookSchema
from services.bot import BotService

api = APIRouter(prefix="", tags=["setters"])


@api.post(path="/", status_code=status.HTTP_200_OK)
async def set_webhook(sw: SetWebhookSchema = Body(...)) -> Response:
    content, status_code = await BotService.setWebhook(webhook_url=sw.url)
    if status_code == 200:
        return content
    else:
        raise HTTPException(status_code=status_code, detail=content)
