from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

# Research Task

research_task = Task(
    description=( 
        " Identify the video {topic}"
        "Get detailed information about the video from the youtube channel",
        ),
    expected_output=(
        "A comprehensive 3 paragraphs long report based on the {topic} of the video content"
    ),
    agent=[blog_researcher],
    tools=[yt_tool],
)

write_task = Task(
    description=(
        "Get the info from the youtube channel on the topic {topic}"
        "Write a blog post on the video content from the youtube channel"
    ),
    expected_output=(
        "Summarize the info from the youtube channel video on the topic {topic} and create the content for the blog"
    ),
    agent=[blog_writer],
    tools=[yt_tool],
    async_execution=False, # to make it run parallely
    output_file="blog_post.md",
)

