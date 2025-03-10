from api.prompt import Prompt
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
class ChatGPT:
    def __init__(self, api_key, model="gpt-4"):
        """初始化 ChatGPT 物件"""
        self.api_key = api_key
        self.model = model

    def ask(self, prompt):
        """向 ChatGPT 發送請求並獲取回應"""
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            api_key=self.api_key
        )
        return response["choices"][0]["message"]["content"].strip()

# 測試
if __name__ == "__main__":
    API_KEY = "your_openai_api_key"
    chatbot = ChatGPT(API_KEY)
    
    question = "請問你是誰？"
    answer = chatbot.ask(question)
    
    print("ChatGPT 回應：", answer)
