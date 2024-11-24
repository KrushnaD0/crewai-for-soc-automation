from crewai import Agent
from textwrap import dedent
import google.generativeai as genai
import os
from tasks import CustomTasks
from custom_tools import pdf_tool,web_search_tool, txt_tool, json_tool, mdx_tool, file_read_tool
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env", verbose=True, override=True)

os.environ['GEMINI_API_KEY'] = "YOUR_API_KEY"

class CustomAgents:
    def __init__(self):
        self.llm_google=genai.GenerativeModel('gemini/gemini-1.5-flash')
        print("\n\nLLM CONNECTED\n\n")

    def threat_intelligence_analyst(self):
        return Agent(
            role="Threat Intelligence Analyst",
            backstory=dedent(f""" You're a threat intelligence analyst at the best security services provider in the world.
      You're responsible for analyzing threat intelligence reports and extracting MITRE ATT&CK TTPs that can be used to build adversary emulation campaigns."""),
            goal=dedent(f"Extract MITRE ATT&CK TTPs from reports"),
            allow_delegation=False,
            tools=[txt_tool, web_search_tool],
            verbose=True,
            llm=self.llm_google,
        )
    


    def detection_engineer(self):
        return Agent(
            role="Detection Engineer",
            backstory=dedent(f"""You are a Detection Engineer responsible for creating detection rules based on MITRE ATT&CK TTPs.
      Your task is to translate the given TTPs into actionable detection logic, allowing security teams to detect and respond to potential adversary activities more effectively."""),
            goal=dedent(f"""Convert MITRE ATT&CK TTPs into detection rules in XML format for monitoring and alerting"""),
            tools=[txt_tool, web_search_tool,json_tool,file_read_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.llm_google,
        )
    
    def red_team_operator(self):
        return Agent(
            role="Red Team Operator",
            backstory=dedent(f"""You are a Red Team Operator tasked with designing and executing adversary emulation plans based on the MITRE ATT&CK framework.
      You create Caldera abilities that can be used to simulate specific TTPs, allowing security teams to test their detection and response capabilities."""),
            goal=dedent(f"""Convert MITRE ATT&CK TTPs into Caldera abilities for testing in YAML format"""),
            tools=[txt_tool, web_search_tool,json_tool,file_read_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.llm_google,
        )