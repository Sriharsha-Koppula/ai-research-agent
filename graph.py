from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_core.messages import HumanMessage, BaseMessage, SystemMessage
from typing import TypedDict, Annotated
import operator
import os

load_dotenv()

system_prompt = """You are a helpful and honest research assistant with access to web search.

Follow these rules strictly:

1. ACCURACY: If you know the answer confidently, answer directly. If you are unsure, use the search tool to find reliable information before answering. Never guess or make up information.

2. HONESTY: If you cannot find reliable information even after searching, clearly say "I don't have reliable information on this topic" instead of hallucinating an answer.

3. MEDICAL & SENSITIVE TOPICS: When users ask about medical, health, or other sensitive topics, be extra careful. Only provide factual, well-sourced information. Always recommend consulting a qualified professional for personal medical advice.

4. SAFETY: If anyone asks for sexual, explicit, or 18+ content, politely respond with "I'm sorry, I'm not able to help with that kind of request" and nothing more.

5. TONE: Be concise, professional, and helpful at all times.
"""

llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-4o-mini"
)
search_tool = TavilySearch(api_key=os.getenv("TAVILY_API_KEY"))
tools = [search_tool]
llm_with_tools = llm.bind_tools(tools)

class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], operator.add]
tool_node = ToolNode(tools)

def llm_node(state: AgentState):
    messages = state["messages"]
    response = llm_with_tools.invoke([SystemMessage(content=system_prompt)] + messages)
    return {"messages": [response]}    
def should_continue(state: AgentState):
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools"
        return END
    
graph = StateGraph(AgentState)

graph.add_node("llm", llm_node)
graph.add_node("tools", tool_node)

graph.set_entry_point("llm")

graph.add_conditional_edges("llm", should_continue)
graph.add_edge("tools", "llm")

app = graph.compile()
if __name__ == "__main__":
    user_input = input("Ask Anything: ")
    result = app.invoke({"messages" : [HumanMessage(content=user_input)]})
    print(result["messages"][-1].content)