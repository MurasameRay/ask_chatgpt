from flask import Flask, request

from base.ask_chatgpt import OpenAI

app = Flask(__name__)

open_ai = OpenAI()

@app.route('/ask_chatgpt', methods=['POST'])
def ask_chatgpt():
    data = request.get_json()  # 从请求体中获取 JSON 数据
    word = data.get('word') if data else None  # 获取 'word' 参数
    if word:
        # 在这里处理接收到的 word
        res = open_ai.create_ask(word)
        response = f"Received word: {res}"
    else:
        response = "No word provided."

    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=23333)
