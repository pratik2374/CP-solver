import tiktoken

enc = tiktoken.get_encoding("cl100k_base")  # Adjust for your model

with open('code.c', 'r') as file:
    command = file.read()
token_count = len(enc.encode(command))

print(f"Token count: {token_count}")
