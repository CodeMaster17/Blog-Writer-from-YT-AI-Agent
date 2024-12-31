from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

# Research Task

research_task = Task(
    description="Identify the video {topic} and get detailed information about it from the YouTube channel.",
    expected_output="A comprehensive 3-paragraph report based on the {topic} of the video content.",
    agent=[blog_researcher],  # List
    tools=[yt_tool],
)
research_task = Task(
    description="Identify the video {topic} and get detailed information about it from the YouTube channel.",
    expected_output="A comprehensive 3-paragraph report based on the {topic} of the video content.",
    agent=blog_researcher,  # Single object
    tools=[yt_tool],
)

