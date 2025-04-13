from base_agent import BaseAgent
from typing import Dict, Any


class MatcherAgent(BaseAgent):
    def __init__(self, name, instructions):
        super().__init__(name="matcher",
                        instructions="""Match candidate profiles with job positions.
                        Consider: skills match, experience level, location preferences.
                        Provide detailed reasoning and compatibility scores.
                        Return matches in JSON format with title, match_score, and location fields.""")
        
    
    async def run(self, messages: list) -> Dict[str, Any]:
        """match condidate with available positions"""
        print(" Matcher: finding suitable job for condidate")

        # for testing i ll use a list of job descriptions --> TODO : integrate a databease !
        sample_jobs=[
            {
                "title": "Senior Software Engineer",
                "requirements": "python, java, Cloud, 5+ years experience",
                "location": "Remote",
            },
            {
                "title":"Data Scientist",
                "requirements":"Python, ML, Statistics, 3+ years experience ",
                "location":"Humberg",
            }
        ]
        # TODO: read content form message make sure it s a json and pass it in the prompt
        