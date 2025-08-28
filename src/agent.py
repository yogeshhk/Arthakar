# Description: Defines the core agentic logic using LangGraph.
# It sets up the agent state, nodes, and the graph that dictates the workflow.

from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import Tool
from langgraph.prebuilt import ToolExecutor

from tools import get_live_stock_price, get_financial_news, parse_document_text
from config import get_groq_api_key

# 1. Define the state for our graph
#    This will be the shared memory between all nodes.
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], lambda x, y: x + y]

class ArthakarAgent:
    def __init__(self):
        """
        Initializes the ArthakarAgent, setting up the model, tools, and the graph.
        """
        # Initialize the LLM
        self.llm = ChatGroq(
            temperature=0,
            model_name="llama3-70b-8192",
            api_key=get_groq_api_key()
        )
        
        # Define the tools the agent can use
        self.tools = [get_live_stock_price, get_financial_news, parse_document_text]
        
        # Bind the tools to the LLM. This makes the LLM "tool-aware".
        self.llm_with_tools = self.llm.bind_tools(self.tools)
        
        # Create a ToolExecutor to actually run the tools
        self.tool_executor = ToolExecutor(self.tools)
        
        # Define the graph
        self.workflow = StateGraph(AgentState)
        
        # Add the nodes to the graph
        self.workflow.add_node("agent", self.call_model)
        self.workflow.add_node("action", self.call_tool)
        
        # Define the edges of the graph
        self.workflow.set_entry_point("agent")
        self.workflow.add_conditional_edges(
            "agent",
            self.should_continue,
            {
                "continue": "action",
                "end": END
            }
        )
        self.workflow.add_edge('action', 'agent')
        
        # Compile the graph into a runnable object
        self.app = self.workflow.compile()

    def get_graph(self):
        """Returns the compiled LangGraph app."""
        return self.app

    def should_continue(self, state: AgentState):
        """
        Decision node: Determines whether to continue with another tool call or end the process.
        """
        last_message = state['messages'][-1]
        # If the last message has no tool calls, then we are done.
        if not last_message.tool_calls:
            return "end"
        # Otherwise, we continue to call the tools.
        return "continue"

    def call_model(self, state: AgentState):
        """
        Agent node: This is where the LLM makes decisions.
        It can either respond to the user or decide to call a tool.
        """
        print("AGENT: Thinking...")
        response = self.llm_with_tools.invoke(state['messages'])
        # We return a dictionary with the messages to update the state
        return {"messages": [response]}

    def call_tool(self, state: AgentState):
        """
        Action node: This node executes the tools chosen by the agent.
        """
        print("ACTION: Executing tools...")
        last_message = state['messages'][-1]
        
        # We construct a list of ToolInvocation objects
        tool_invocations = []
        for tool_call in last_message.tool_calls:
            action = Tool(
                name=tool_call['name'],
                description="", # Description is not needed here
                func=self.tool_executor.functions[tool_call['name']]
            )
            # We invoke the tool with the provided arguments
            tool_invocations.append(
                (action.invoke(tool_call['args']), tool_call['id'])
            )
            
        # We get the tool outputs
        tool_outputs = self.tool_executor.batch(tool_invocations)
        
        # We format the outputs as ToolMessage objects
        tool_messages = [
            (output, tool_call_id)
            for (output, tool_call_id) in zip(tool_outputs, [tc['id'] for tc in last_message.tool_calls])
        ]
        
        # We return the tool messages to be added to the state
        return {"messages": tool_messages}
