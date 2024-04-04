import json
from logger import logger


class ChatRequest:
    def __init__(self, request_id, message, chatbot_id, summary, llm='zhipu', model='glm-4'):
        self.request_id = request_id
        self.message = message
        self.llm = llm
        self.model = model

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        try:
            data = json.loads(json_str)
            return cls(**data)
        except json.JSONDecodeError:
            logger.error("Error: Invalid JSON string: %s", json_str)
            return None
