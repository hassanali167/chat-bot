


# ---------------------------------------------------------------------------------


# new code  for seprate file

import os
import chainlit as cl
from chain import ChatBot

@cl.on_chat_start
async def start_chat():
    """Send a welcome message when the chat starts."""
    await cl.Message(content="Hello! How can I assist you today?").send()


@cl.on_message
async def handle_message(message):
    """Send user input to the Groq model and display the response."""
    user_message = message.content
    if not user_message.strip():
        await cl.Message(content="Please enter a valid query.").send()
        return
         
    chatbot = ChatBot()
    bot_response = chatbot.get_response(user_message)
    await cl.Message(content=bot_response).send()


if __name__ == "__main__":
    cl.run()



















