from crewai import Agent
from tools.search_tools import SearchTools


class AINewsLetterAgents():
    def editor_agent(self):
        return Agent(
            role='Editor',
            goal='Oversee the Creation of AI newsletter',
            backstory=""" 
          With a keen eye for detail and a passion for storytelling, you ensure that the newsletter
          not only informs but also engages and inspires the readers. 
        """,
            # Allow agent to delegate the work to other agents``
            allow_delegation=True,
            # priint out the thinking process
            verbose=True,
            # So that the agent cannot get stuck in the infinite loop:
            max_iter=15
        )

    def news_fetcher_agent(self):
        return Agent(
            role='NewsFetcher',
            goal='Fetch the top AI news stories for the day',
            backstory="""
              As a digital sleuth, you scour the internet for the latest and most impactful developments in the world of AI, ensuring that our readers are always upto the date with latest developement in AI.
            """,
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True,
        )

    def news_analyzer_agent(self):
        return Agent(
            role='NewsAnalyzer',
            goal='Analyze each news story and generate a detailed markdown summary',
            backstory="""
              With a critical eye and a knack for distilling complex information, you provide insightful and rightul analyses of AI news stories, making them accessible and engaging for our audience.
            """,
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True,
        )

    def newsletter_compiler_agent(self):
        return Agent(
            role='NewsletterCompiler',
            goal='Compile the analyzed news stories into a final newsletter format',
            backstory="""
              As the final architect of the newsletter, you meticulously arrange and format the content,ensuring a coherent and visually appealing presentation that captivates our readers. Make sure to follow newsletter format guidelines and maintain consistency throughout.
            """,
            verbose=True,
        )
