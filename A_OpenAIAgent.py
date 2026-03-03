
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent

def main():
    model = ChatOllama(
        model="llama3.2:1b",
        temperature=0
    )

    tools = []
    agent_executor = create_react_agent(model, tools)

    print("🤏 Llama3.2 Ollama Assistant Ready")
    print("Type 'quit' to exit")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "quit":
            break

        print("\nAssistant: ", end="")

        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")

        print()

if __name__ == "__main__":
    main()
