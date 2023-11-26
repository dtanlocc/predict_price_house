import openai

gpt_key=["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",'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','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']

def process_using_gpt(value, key):
    openai.api_key = key
    input_text = f"Hãy dự đoán giúp tôi loại nội thất của '{value}'. Nó thuộc loại 'không có nội thất', 'nội thất cơ bản', hay 'đầy đủ nội thất'. Nếu nó thuộc loại 'không có nội thất' thì chỉ hiển thị 'không', nếu nó thuộc loại 'nội thất cơ bản' thì chỉ hiển thị 'cơ bản' nếu nó thuộc loại 'đầy đủ nội thất' thì hiển thị 'đầy đủ'. Chỉ chấp nhận câu trả lời nằm trong 3 loại sau ['không', 'cơ bản', 'đầy đủ'] không giải thích gì thêm và không chấp nhận việc bạn không dự đoán được."

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=input_text,
      temperature=0.1,
      # max_tokens=30,
    )
    print(response['choices'][0]['text'])

process_using_gpt('nội thất sang trọng và đẳng cấp.', gpt_key[0])