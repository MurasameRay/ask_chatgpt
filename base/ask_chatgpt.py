import os
import openai

# 完全免费使用以下勾选模型：
#  gpt-4o-mini（速度一般，若要体验极速回复，可购买付费API）
#  gpt-3.5-turbo-0125
#  gpt-3.5-turbo-1106
#  gpt-3.5-turbo
#  gpt-3.5-turbo-16k
#  net-gpt-3.5-turbo (可联网搜索模型-稳定性稍差)
#  whisper-1
#  dall-e-2
#  text-开头系列模型，例如：text-davinci（免费版已取消text系列模型）
#  gpt-4全系列（只定期限量开放）
#  付费版API支持OpenAI所有模型，包括（联网、绘画、聊天、向量、图片分析、文件分析、GPTs等）
#  付费版API支持Midjourney专业绘画、Suno音乐生成、PPT生成、（视频模型接入中）
# 标准的OpenAI接口请求格式。
# 支持流式响应输出。
# 完美兼容各类开源的GPT项目/应用/软件。

class OpenAI:
    def __init__(self):
        # optional; defaults to `os.environ['OPENAI_API_KEY']`
        openai.api_key = "sk-IVDR7MAkWixAiEco2f09F4D20eA240Ed9945A9CbC3AfB1B3"

        # all client options can be configured just like the `OpenAI` instantiation counterpart
        openai.base_url = "https://run.v36.cm/v1/"
        openai.default_headers = {"x-foo": "true"}

    @staticmethod
    def create_ask(text):
        completion = openai.chat.completions.create(
            # model="gpt-3.5-turbo",
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": text,
                },
            ],
        )
        # print(completion.choices[0].message.content)
        return completion.choices[0].message.content

if __name__ == "__main__":
    open_ai = OpenAI()
    while True:
        res = open_ai.create_ask("hello")
        print(res)