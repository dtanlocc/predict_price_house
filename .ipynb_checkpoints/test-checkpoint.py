import openai

openai.api_key="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"

input = "Hãy dự đoán kết quả giúp tôi từ 'đẹp' nó thuộc loại 'không có nội thất', 'nội thất cơ bản', hay 'đầy đủ nội thất'.Nếu nó thuộc lội 'không có nội thất' thì chỉ hiển thị 'không', nếu nó thuộc loại 'nội thất cơ bản' thì chỉ hiển thị 'cơ bản' nếu nó thuộc loại 'đầy đủ nội thất' thì hiển thị'đầy đủ'. Chỉ trả lời là thuộc loại 'không', 'cơ bản', hay 'đầy đủ' không giải thích gì thêm"

response = openai.Completion.create(
  engine="text-davinci-002",  # Sử dụng engine "text-davinci-002" thay vì "gpt-3.5-turbo"
  prompt=input,
  max_tokens=50
)

print(response.choices[0].text.strip())