import sys
from openai import OpenAI

# 1. Initialize client pointing to your LOCAL machine
# base_url: Default LM Studio port is 1234
# api_key: LM Studio ignores this, but the library requires it to be non-empty
client = OpenAI(
    base_url="http://localhost:1234/v1", 
    api_key="lm-studio" 
)
# 2. Get user input
#prompt = input("say something: ")
print("Paste your code here. Press Ctrl+D (Unix/Mac) or Ctrl+Z then Enter (Windows) to finish:")
prompt = sys.stdin.read()
print("You entered:")

try:
    # 3. Send request
    response = client.chat.completions.create(
        model="local-model", # LM Studio ignores this and uses the loaded model
        messages=[
            {"role": "system", "content": "You are a senior software engineer review the given code."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    print("\nAI Response:")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"Error: {e}")
    print("Tip: Make sure LM Studio server is running and a model is loaded!")