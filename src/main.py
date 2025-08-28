# Description: The main entry point for the Arthakar application.

import sys
from agent import ArthakarAgent

def main():
    """
    Main function to run the Arthakar financial assistant.
    It takes a user query from the command line arguments.
    """
    # Check if a query was provided
    if len(sys.argv) < 2:
        print("Usage: python main.py \"<your financial query>\"")
        sys.exit(1)

    # Join all arguments after the script name to form the query
    user_query = " ".join(sys.argv[1:])
    
    print(f"🚀 Initializing Arthakar Agent for your query: \"{user_query}\"")
    
    # Initialize the agent
    arthakar_agent = ArthakarAgent()
    
    # Get the runnable graph from the agent
    app = arthakar_agent.get_graph()
    
    print("\n...Processing your request. This may take a moment...\n")
    
    # The input to the graph is a dictionary with a "messages" key
    inputs = {"messages": [("user", user_query)]}
    
    # Stream the output from the graph
    final_response = ""
    for output in app.stream(inputs):
        # The stream output is a dictionary where each key is a node name
        for key, value in output.items():
            if "messages" in value:
                # We extract the last message which is the agent's response
                agent_message = value["messages"][-1]
                final_response = agent_message.content
                # Print intermediate steps or thoughts from the agent
                print(f"--- Thought from {key} ---")
                print(agent_message.content)
                print("\n")

    print("✅ Final Response from Arthakar:\n")
    print(final_response)


if __name__ == "__main__":
    main()
