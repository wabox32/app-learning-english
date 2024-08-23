import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chains import LLMChain, ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from langchain_openai import ChatOpenAI
from langchain_core.prompts.prompt import PromptTemplate
from langchain.memory import ConversationBufferMemory


load_dotenv()
os.environ["OPENAI_API_KEY"] =  os.getenv("OPENAI_API_KEY")
memory = ConversationBufferMemory(ai_prefix="AI Assistant"),
model = ChatOpenAI(model="gpt-3.5-turbo")

def response(prompt, question):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    template = """Eres un profesor de ingles me ayudaras aprender ingles me realizaras preguntas con tematica de pasado simpre y yo las contestare luego de que me las contestes me corregiras y me daras otra pregunta diferente el nivel del ingles es A1.

Current conversation:
{history}
Human: {input}
AI Assistant:"""

    PROMPT = PromptTemplate(input_variables=["history", "input"], template=template)

    chat_chain = ConversationChain(
        prompt=PROMPT,
        llm=llm,
        verbose=True,
        memory=ConversationBufferMemory(ai_prefix="AI Assistant")
    )
    return  chat_chain.predict(input=question)