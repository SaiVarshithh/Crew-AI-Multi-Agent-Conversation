# in-built
import re
from datetime import datetime
import pandas as pd

# custom
from crewai import Crew, Process
from src.agents import salesman_agent, user_agent, formatter_agent
from src.tasks import salesman_task, user_task


class CrewAI:

    def __init__(self) -> None:
        self.crew_1 = Crew(
            agents=[user_agent, formatter_agent],
            tasks=[user_task],
            verbose=True,
            process=Process.sequential,
        )

        self.crew_2 = Crew(
            agents=[salesman_agent, formatter_agent],
            tasks=[salesman_task],
            verbose=True,
            process=Process.sequential,
        )

    def conversation(self, product: str, n: int) -> dict:

        conversations = []

        user_input = {"product": product, "salesman_answer": None}
        question_1 = self.crew_1.kickoff(inputs=user_input)

        for _ in range(n):
            conversation = []

            salesman_input = {"product": product, "user_question": question_1}
            result = self.crew_2.kickoff(inputs=salesman_input)
            result = re.sub(r"\(.*?\)", "", result)
            salesman_answer = result.strip()

            conversation.append(
                {
                    "timestamp": datetime.now(),
                    "speaker": "Salesman",
                    "message": salesman_answer,
                }
            )

            user_input = {
                "product": product,
                "salesman_answer": salesman_answer,
            }
            result = self.crew_1.kickoff(inputs=user_input)
            result = re.sub(r"\(.*?\)", "", result)
            user_question = result.strip()
            conversation.append(
                {
                    "timestamp": datetime.now(),
                    "speaker": "User",
                    "message": user_question,
                }
            )

            conversations.extend(conversation)

        return conversations


def main():
    crew_ai = CrewAI()
    product = input(
        "Enter the name of product or service to start conversation: "
    )
    no_of_conv = int(
        input("Enter the number of conversations you want to build: ")
    )
    conversations = crew_ai.conversation(product=product, n=no_of_conv)

    conversation_df = pd.DataFrame(conversations)
    conversation_df.to_csv(f"{product}_conversations.csv", index=False)
    print(f"{no_of_conv} built and saved in csv succesfully!!!")


if __name__ == "__main__":
    main()
