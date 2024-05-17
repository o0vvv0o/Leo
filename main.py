from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

def chat_with_me():
    context = ""
    while True:
        user_input = input("You: ")
        context += "You: " + user_input + "\n"
        print("-----------------------------------------------------")  # Add a separator line
        completion = client.chat.completions.create(
            model="meta/llama3-70b-instruct",
            messages=[{"role": "user", "content": context}],
            temperature=0.5,
            top_p=1,
            max_tokens=1024,
            stream=True
        )
        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")
                context += chunk.choices[0].delta.content + "\n"
        print("\n------------------------------------------------------")  # Add a separator line

chat_with_me()
