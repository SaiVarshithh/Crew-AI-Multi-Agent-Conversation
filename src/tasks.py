# custom
from crewai import Task
from src.agents import salesman_agent, user_agent


user_task = Task(
    description=(
        "Ask a relevant question about the {product} based on the previous response: {salesman_answer} from the salesman. If this is the first question, ask a general question about the product to start the conversation."
        "Focus on grammar and tense of the questions."
        "That question will be given to the salesman for generating a response"
    ),
    expected_output="A clear and relevant question about the product",
    agent=user_agent,
    memory=True,
)

salesman_task = Task(
    description=(
        "Provide a detailed and persuasive response to the customer's question about the {product}."
        "Highlight the features, benefits, and unique selling points of the product in an engaging manner."
        "Address any potential concerns or objections the customer may have."
    ),
    expected_output="A descriptive and persuasive answer of 75-80 words that is easily understandable to the customer",
    agent=salesman_agent,
)
