from crewai import Agent
from langchain_groq import ChatGroq
from tools import yt_tool
import os 

from dotenv import load_dotenv

load_dotenv()

# os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not set. Please add it to your .env file.")
# Create a senior blog content researcher
blog_researcher = Agent(
    role='Blog Researcher from Youtube videos',
    goal='Get the relevant video content for the topic{topic} from youtube channel',
    verbose=True,
    backstory=(
        "Expert in understanding videos in AI Data Science, Machine Learning and GEN Ai and providing suggestions"
    ),
    tools=[
yt_tool
    ],
    allow_delegation=True,
    llm=ChatGroq(groq_api_key=api_key, model_name="mixtral-8x7b-32768")
) 

# Create a senior blog writer agent with Yotube tool
blog_writer=Agent(
    role='Writer',
    goal='Narrate compelling tech stories about the video {topic} from Youtube channel',
    verbose=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging stories that captivate and educate, bringing new"
        "discoveries ot light in an accessible manner"
    ),
    tools=[
        yt_tool
    ],
    allow_delegation=False,
       llm=ChatGroq(groq_api_key=api_key, model_name="mixtral-8x7b-32768")
)

