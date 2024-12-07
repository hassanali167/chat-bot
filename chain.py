import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from summarizer import summarize_context

# Load API key from the .env file
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Developer details
DEVELOPER_DETAILS = """
The chatbot was developed by Hassan Ali, a Software Engineering student at 
Pak Austria Fachhochschule Institute of Applied Sciences and Technology, Mang Haripur, 
and a Software Developer at Technik Nest.

Education:
Hassan Ali is currently studying in his 5th semester.

Professional Work:
Hassan Ali works as a software developer at Technik Nest.

Portfolio and Social Profiles:
- Portfolio: https://hassanali202.vercel.app/
- LinkedIn: https://www.linkedin.com/in/hassanali202/
- GitHub: https://github.com/hassanali167

Expertise:
Python, C++, Django, AI/ML, Docker, IoT, High-Performance Computing, LLM, Proxmox Administration.
"""

class ChatBot:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=GROQ_API_KEY,
            model_name="llama-3.1-70b-versatile",
        )
        self.context = {"var1": None, "var2": None, "var3": None}

    def get_response(self, user_message):
        """Generate a contextual response for user input."""
        try:
            # Update the conversational context
            self.context["var1"] = user_message
            if self.context["var2"]:
                summarized_context = f"{self.context['var2']} {user_message}"
                self.context["var3"] = summarize_context(summarized_context, self.llm)

            # Prepare the prompt
            prompt_template = PromptTemplate.from_template(
                """
                You are a helpful assistant. Always respond to the user's query concisely and clearly.
                Here are the developer details: 
                {developer_details}
                
                If the user asks about the developer, provide the relevant details based on their question. 
                If not, focus solely on the user's query.

                Current Context:
                {context}
                here is my previous chat with you so which is summarized and their have also my new chat and 
                see this summarized previous chat and give me the next reponce by seeing this context and 
                also if it is relavent to previous 
                give me the best responce by using previous chat and the next query also 



                User: {user_input}
                here is my new question do this also use previous chat if thay are related to each other 
                
                Bot Response:
                """
            )
            chain = prompt_template | self.llm

            # Get the response from the Groq model
            response = chain.invoke(
                input={
                    "developer_details": DEVELOPER_DETAILS,
                    "context": self.context["var3"] or "No prior context available.",
                    "user_input": user_message,
                }
            )

            # Update context with the bot response
            self.context["var2"] = response.content.strip()

            return response.content.strip()

        except OutputParserException as e:
            return f"Error: Unable to parse the response. {str(e)}"
        except Exception as e:
            return f"Error occurred while processing your request: {str(e)}"




