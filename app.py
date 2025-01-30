import chainlit as cl
from ollama import Client

# Initialize Ollama client
client = Client(host="http://localhost:11434")  # Default Ollama API endpoint

@cl.on_message
async def on_message(message: cl.Message):
    # System prompt to guide the model's behavior
    system_prompt = "You are a helpful AI assistant. Answer concisely and clearly."

    # Combine the system prompt with the user's message
    full_prompt = f"{system_prompt}\n\nUser: {message.content}\nAssistant:"

    # Send the prompt to DeepSeek-R1 via Ollama
    response = client.generate(
        model="deepseek-r1:7b",
        prompt=full_prompt,
        stream=True,
        options={
            "temperature": 0.7,  # Adjust creativity
            "max_tokens": 150,   # Limit response length
        },
    )

    # Stream the response back to the Chainlit UI
    response_message = cl.Message(content="")
    await response_message.send()

    for chunk in response:
        await response_message.stream_token(chunk["response"])

    # Finalize the response
    await response_message.update()