import re

import openai

KEY = "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"
openai.api_key = KEY


def Ans_ChatGPT(question):
    completion = completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": question
        }]
    )
    response = completion.choices[0].message.content
    return response


sentence = "好きです。付き合ってください。お願いします"
question = "「"+sentence+"」\n"+"この文章のロマンティック度を100点満点で評価して数字だけを教えてください"
answer = Ans_ChatGPT(question)
print(sentence)
print(re.findall(r'\d+', answer)[0])
