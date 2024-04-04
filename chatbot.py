import time
from zhipuai import ZhipuAI
from logger import logger

# add your zhipuai api key here
ZHIPUAI_API_KEY = ''


class BaseChatbot:
    def __init__(self):
        self.round = 0
        self.max_retries = 5
        self.delay = 2
        self.client = self.client = ZhipuAI(
            api_key=ZHIPUAI_API_KEY,
        )
        self.llm = 'zhipu'
        self.model = 'glm-4'
        self.messages = []

    def chat(self, msg, request_id):
        self.round += 1
        logger.info("对话轮次:%d", self.round)
        self.messages.append({"role": "user", "content": msg})

        for attempt in range(self.max_retries):
            try:
                if request_id:
                    response = self.client.chat.completions.create(
                        model=self.model,  # 填写需要调用的模型名称
                        messages=self.messages,
                        request_id=request_id,
                    )
                    logger.info("response with request_id:%s", response)
                    return self.assemble_zhipu_result(response)
                else:
                    response = self.client.chat.completions.create(
                        model=self.model,  # 填写需要调用的模型名称
                        messages=self.messages,
                    )
                    logger.info("response without request_id:%s", response)
                    return self.assemble_zhipu_result(response)
            except Exception as e:
                print(f"尝试 {attempt + 1}/{self.max_retries} 失败: {e}")
                if attempt < self.max_retries - 1:  # 如果不是最后一次尝试，则延迟
                    time.sleep(self.delay)
                else:
                    return self.assemble_error_result(request_id)  # 如果达到最大尝试次数，则返回错误回复

    def assemble_zhipu_result(self, response):
        ai_content = response.choices[0].message.content
        self.messages.append({'role': 'assistant', 'content': ai_content})
        result = {
            "created": response.created,
            "model": response.model,
            "request_id": response.request_id,
            "message": response.choices[0].message.content,
            "round": self.round
        }
        return result

    def assemble_error_result(self, request_id):
        result = {
            "created": int(time.time()),
            "model": '',
            "request_id": request_id,
            "message": '系统错误，请稍后再试',
            "round": self.round
        }
        return result
