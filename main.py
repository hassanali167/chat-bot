import os
import chainlit as cl
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

# Your Groq API key
GROQ_API_KEY = "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"

# Class to interact with the Groq API using Langchain
class ChatBot:
    def __init__(self):
        # Initialize the Groq Llama model using Langchain's ChatGroq class
        self.llm = ChatGroq(
            temperature=0, 
            groq_api_key=GROQ_API_KEY,  # Use the Groq API key
            model_name="llama-3.1-70b-versatile"  # Llama 3.1 model
        )

    def get_response(self, user_message):
        """Send user input to the Llama model and return the response."""
        try:
            print(f"Sending message to Groq API: {user_message}")  # Debugging: print user message
            # Create the prompt template
            prompt_template = PromptTemplate.from_template(
                """
                You are a helpful assistant. Respond to the user's query clearly and concisely.
                User: {user_input}
                Bot Response:
                """
            )

            # Combine the prompt and the model for a conversation flow
            chain = prompt_template | self.llm

            # Get response from Groq model
            response = chain.invoke(input={"user_input": user_message})

            print(f"Raw response from API: {response.content}")  # Debugging: print raw response

            # Parse and return plain text response
            return response.content.strip()  # Ensure it's plain text response

        except OutputParserException as e:
            print(f"Error parsing response: {str(e)}")  # Debugging: print error
            return f"Error: Unable to parse the response. {str(e)}"
        except Exception as e:
            print(f"Error occurred: {str(e)}")  # Debugging: print exception
            return f"Error occurred while processing your request: {str(e)}"

# Chainlit Event Handlers

# When the chat starts
@cl.on_chat_start
async def start_chat():
    """Send a welcome message when the chat starts."""
    await cl.Message(content="Hello! How can I assist you today?").send()

# When a user sends a message
@cl.on_message
async def handle_message(message):
    """Send user input to the Groq model and display the response."""
    user_message = message.content  # Access the content of the message

    # Ensure the user input is not empty
    if not user_message.strip():
        await cl.Message(content="Please enter a valid query.").send()
        return
    
    # Create a chatbot instance and get the response from the Groq API
    chatbot = ChatBot()
    bot_response = chatbot.get_response(user_message)

    # Send the response back to the user
    await cl.Message(content=bot_response).send()

# Run the Chainlit app
if __name__ == "__main__":
    cl.run()

# ---------------------------------------------------------------------------------------------------
# import os
# import chainlit as cl
# from langchain_groq import ChatGroq
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import JsonOutputParser
# from langchain_core.exceptions import OutputParserException

# # Your Groq API key
# GROQ_API_KEY = "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"

# # Class to interact with the Groq API using Langchain
# class ChatBot:
#     def __init__(self):
#         # Initialize the Groq Llama model using Langchain's ChatGroq class
#         self.llm = ChatGroq(
#             temperature=0, 
#             groq_api_key=GROQ_API_KEY,  # Use the Groq API key
#             model_name="llama-3.1-70b-versatile"  # Llama 3.1 model
#         )

#     def get_response(self, user_message):
#         """Send user input to the Llama model and return the response."""
#         try:
#             print(f"Sending message to Groq API: {user_message}")  # Debugging: print user message
#             # Create the prompt template
#             prompt_template = PromptTemplate.from_template(
#                 """
#                 You are a helpful assistant. Respond to the user's query clearly and concisely.
#                 User: {user_input}
#                 Bot Response:
#                 """
#             )

#             # Combine the prompt and the model for a conversation flow
#             chain = prompt_template | self.llm

#             # Get response from Groq model
#             response = chain.invoke(input={"user_input": user_message})

#             print(f"Raw response from API: {response.content}")  # Debugging: print raw response

#             # Parse and return plain text response
#             return response.content.strip()  # Ensure it's plain text response

#         except OutputParserException as e:
#             print(f"Error parsing response: {str(e)}")  # Debugging: print error
#             return f"Error: Unable to parse the response. {str(e)}"
#         except Exception as e:
#             print(f"Error occurred: {str(e)}")  # Debugging: print exception
#             return f"Error occurred while processing your request: {str(e)}"

# # Chainlit Event Handlers

# # When the chat starts
# @cl.on_chat_start
# async def start_chat():
#     """Send a welcome message when the chat starts."""
#     await cl.Message(content="Hello! Welcome to ChatBot! How can I assist you today?").send()

# # When a user sends a message
# @cl.on_message
# async def handle_message(message):
#     """Send user input to the Groq model and display the response."""
#     user_message = message.content  # Access the content of the message

#     # Ensure the user input is not empty
#     if not user_message.strip():
#         await cl.Message(content="Please enter a valid query.").send()
#         return
    
#     # Create a chatbot instance and get the response from the Groq API
#     chatbot = ChatBot()
#     bot_response = chatbot.get_response(user_message)

#     # Send the response back to the user
#     await cl.Message(content=bot_response).send()

# # Run the Chainlit app
# if __name__ == "__main__":
#     # Configure Chainlit to hide branding and other UI customizations
#     cl.settings.update(
#         {
#             "title": "ChatBot",
#             "description": "A custom AI chatbot powered by Groq.",
#             "theme": "dark",
#             "hide_copyright": True,  # Remove footer copyright text
#             "hide_branding": True,  # Remove Chainlit logo from the interface
#         }
#     )
#     cl.run()



# ---------------------------------------------------------------------------------------------------





