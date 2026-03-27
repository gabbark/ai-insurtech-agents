from openai import OpenAI

client = OpenAI(api_key="your_api_key")

def call_llm(system_prompt, user_input, context=None):
    messages = [
        {"role": "system", "content": system_prompt}
    ]

    if context:
        messages.append({"role": "assistant", "content": context})

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        temperature=0.3
    )

    return response.choices[0].message.content
