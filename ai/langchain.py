import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()
os.environ["OPENAI_API_KEY"] =  os.getenv("OPENAI_API_KEY")


model = ChatOpenAI(model="gpt-3.5-turbo")

def response(prompt, question):
    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=question),
    ]

    return model.invoke(messages)