import tiktoken

enc = tiktoken.get_encoding()  # Adjust for your model

with open('/d:/CP solver/code.c', 'r') as file:
    command = file.read()
token_count = len(enc.encode(command))

print(f"Token count: {token_count}")
