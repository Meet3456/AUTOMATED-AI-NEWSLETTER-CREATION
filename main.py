from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from agents import AINewsLetterAgents
from tasks import AINewsLetterTasks
from file_io import save_output_as_markdwon

from dotenv import load_dotenv
load_dotenv()

# initialzing all agentss and tasks
agents = AINewsLetterAgents()
tasks = AINewsLetterTasks()

# initializing the llm:
OpenAIGPT35 = ChatOpenAI(
    model="gpt-3.5-turbo"
)

editor = agents.editor_agent()
news_fetcher = agents.news_fetcher_agent()
news_analyzer = agents.news_analyzer_agent()
newsletter_compiler = agents.newsletter_compiler_agent()

# takes news_fetcher agent
fetch_news_task = tasks.fetch_news_task(news_fetcher)

# takes news_analyzer agent along with context(previous task's output)
analyze_news_task = tasks.analyze_news_task(news_analyzer, [fetch_news_task])

# takes newsletter_compiler agent along with context(previous task's output) and a callback function
compile_newsletter_task = tasks.compile_newsletter_task(
    newsletter_compiler, [analyze_news_task], save_output_as_markdwon)

# Create the crew
crew = Crew(
    agents=[editor, news_fetcher, news_analyzer, newsletter_compiler],
    tasks=[fetch_news_task, analyze_news_task, compile_newsletter_task],
    process=Process.hierarchical,
    manager_llm=OpenAIGPT35,
    verbose=2
)

# Kick off the crew's work
results = crew.kickoff()

# Print the results
print("Crew Work Results:")
print(results)