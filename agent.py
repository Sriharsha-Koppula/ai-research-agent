from langchain_tavily import TavilySearch
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
llm = ChatGroq(api_key = os.getenv("GROQ_API_KEY"), 
               model = "llama-3.3-70b-versatile")
search_tool = TavilySearch(api_key = os.getenv("TAVILY_API_KEY"))
tools = [search_tool]
llm_with_tools = llm.bind_tools(tools)
user_input = input("Ask anything: ")
response = llm_with_tools.invoke(user_input)
print(response)