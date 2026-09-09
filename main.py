from agent import run_agent

print("AI Student Support Assistant")
print("Type 'exit' to stop.")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    answer = run_agent(question)

    print("\nAI:", answer)