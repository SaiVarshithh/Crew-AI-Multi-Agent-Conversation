# in-built
import os

# 3rd party
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.7,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)


## Define Agents
salesman_agent = Agent(
    role="Salesman",
    goal="Sell or offer services to provided to you to potential customers by highlighting the features and benefits in an engaging and persuasive manner",
    verbose=True,
    memory=True,
    backstory=(
        "You're an experienced salesman, skilled at understanding"
        "customer needs and presenting products in the most appealing way."
        "Your goal is to showcase the features and benefits of the product you're selling while addressing any concerns or objections the customer may have."
    ),
    llm=llm,
    allow_delegation=False,
)


user_agent = Agent(
    role="User",
    goal="Explore the features and capabilities of products or services to find the best one for your needs",
    verbose=True,
    memory=True,
    backstory=(
        "You're a curious customer looking to find the best product for your needs."
    ),
    llm=llm,
    allow_delegation=False,
)

formatter_agent = Agent(
    role="formatter",
    goal="""Format the text as asked. Leave out actions from discussion members that happen between brackets, eg (smiling).""",
    backstory="You are an expert text formatter.",
    llm=llm,
    verbose=True,
    allow_delegation=False,
)
