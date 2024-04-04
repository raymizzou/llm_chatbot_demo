from flask import Flask, request
from chatbot import BaseChatbot
from entity import ChatRequest
from logger import logger
import json

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    logger.info("====chat start, request param: %s", request.get_json())
    chat_request = ChatRequest.from_json(request.data)
    logger.info("chat_request %s", chat_request.to_json())

    # validate param
    if chat_request is None:
        logger.error("====chat end: invalid request")
        return "{\"code\": -2, \"message\":\"empty user input\"}"

    bot = BaseChatbot()
    result = bot.chat(chat_request.message, '')
    chat_result = json.dumps(result)
    logger.info("====chat end, chat result: %s", chat_result)
    return chat_result


if __name__ == '__main__':
    app.run(port=9000, debug=True, host='0.0.0.0')
