from crewai import Agent


# Create a senior blog content researcher
blog_researcher = Agent(
    role='Blog Researcher from Youtube videos',
    goal='Get the relevant video content for the topic{topic} from youtube channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science, Machine Learning and GEN Ai and providing suggestions"
    ),
    tool=[

    ],
    allow_delegation=True,
) 

# Create a senior blog writer agent with Yotube tool
blog_writer=Agent(
    role='Writer',
    goal='Narrate compelling tech stories about the video {topic} from Youtube channel',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging stories that captivate and educate, bringing new"
        "discoveries ot light in an accessible manner"
    ),
    tools=[
        
    ],
    allow_delegation=False,
)
