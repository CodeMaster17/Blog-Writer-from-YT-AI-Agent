from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY") 
print(f"GROQ_API_KEY loaded: {api_key}")

crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    memory = True,
    cache= True,
    max_rpm=100,
    share_crew=True,
)

# start task execution process with enhanced feedback
result = crew.kickoff(inputs={"topic": "AI VS ML VS DL VS Data Science"})
print(result)
