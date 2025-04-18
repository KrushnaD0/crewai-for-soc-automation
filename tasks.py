from crewai import Task
from textwrap import dedent

class CustomTasks:
    def extract_ttps_task(self, agent, var1):
        return Task(
            description=dedent(
                f"""
            Analyze the provided DFIR report and extract the relevant MITRE ATT&CK TTPs.
    Ensure that all identified tactics, techniques, and procedures are mapped correctly to the MITRE framework.
    REPORT: {var1}
        """
            ),
            agent=agent,
            expected_output=dedent(f"""
						  Generate a general cyber security report for the given documentation.
						  The report should include a list of MITRE TTPs.
                          Provide a JSON file containing a list of extracted TTPs with their corresponding techniques and descriptions.
						  """),
           
        )
    
    def generate_abilities_task(self, agent,var2):
        return Task(
            description=dedent(
                f"""
           Based on the extracted MITRE ATT&CK TTPs, generate corresponding Caldera abilities.
      The abilities should simulate specific adversary behavior for testing security controls, using Mitre TTPs.
      TTPs: {var2}
        """
            ),
            agent=agent,
            expected_output=dedent(f"""
						        A YAML file containing Caldera abilities for each TTP with the appropriate commands and settings.
						  """),
         
        )
    

    def generate_detection_rules_task(self, agent,var2):
        return Task(
            description=dedent(
                f"""
        Using the extracted MITRE ATT&CK TTPs, create detection rules that can be deployed in a SIEM (WAZUH) system.
        The detection rules should focus on identifying adversary techniques based on the provided TTPs.
        TTPs: {var2}
        """
            ),
            agent=agent,
            expected_output=dedent(f"""
						   A XML  file containing detection rules with descriptions, log sources, and necessary thresholds.
						  """),
   
        )
