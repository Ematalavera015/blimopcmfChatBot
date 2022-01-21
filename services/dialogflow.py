from google.cloud import dialogflow_v2
import os

class DialogFlow:
    

    def __init__(self) -> None:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.dirname(os.path.abspath(__file__)) + "/keys/cmf2022.json"
        self.client = dialogflow_v2.SessionsClient()
        self.session = self.client.session_path(project = os.environ.get("PROJECT_ID"), session =os.environ.get("SESSION_ID", "me"))
    
    async def message(self, text: str) -> str:
        text_input = dialogflow_v2.TextInput(text=text, language_code="es")
        query_input = dialogflow_v2.QueryInput(text=text_input)
        response = self.client.detect_intent(query_input=query_input, session=self.session)
        return response.query_result.fulfillment_text

DialogFlowService = DialogFlow()