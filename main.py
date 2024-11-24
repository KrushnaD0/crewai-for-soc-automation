import os
from crewai import Agent, Task, Crew, Process
import json
from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks
class CustomCrew:
    def __init__(self, var1):
        self.var1 = var1
        
    def run(self):
        agents = CustomAgents()
        tasks = CustomTasks()
        threat_intelligence_analyst = agents.threat_intelligence_analyst()
        
        red_team_operator = agents.red_team_operator()

        detection_engineer = agents.detection_engineer()

        extract_ttps = tasks.extract_ttps_task(
            threat_intelligence_analyst,
            var1=self.var1,
        )
        print("\n\nextracted ttps\n\n")
        var2=r"""
                 add your ttps here to generate abilities and rules
               """
        generate_abilities_task = tasks.generate_abilities_task(
            red_team_operator,
            var2,
        )
        print("\n\ngenerated abilities\n\n")

        generate_detection_rules_task = tasks.generate_detection_rules_task(
            detection_engineer,
            var2,
        )
        print("\n\n generated rules\n\n")

        crew = Crew(
            agents=[threat_intelligence_analyst,red_team_operator,detection_engineer],
            tasks=[extract_ttps, generate_abilities_task, generate_detection_rules_task],
            verbose=True,
            process=Process.sequential,
        )

        result = crew.kickoff()
        return result

if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    var1 = r"""
                add your report text here
            """
    print("**** Creating Crew ****")
    custom_crew = CustomCrew(var1)
    print("**** RUNNING CREW ****")
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
    