import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o")
text = "Hey GPT!"

# Encode the token
token = encoder.encode(text)
print(f"token - {token}")

# Decode the token
decoded = encoder.decode(token)
print(f"decoded - {decoded}")