import os
from pathlib import Path
from extractor_agent import ExtractorAgent
from analyzer_agent import AnalyzerAgent
from datetime import datetime
import asyncio


async def main():
    doc_path = "Ai_recruter_agency/agents/test_data/Resume.pdf"
    if os.path.exists(doc_path):
        extractor_agent =  ExtractorAgent()
        analyzer_agent  = AnalyzerAgent()

        resume_data = {
            "file_path": doc_path,
            "submission_timestamp": datetime.now().isoformat(),
        }
        workflow_context  =  {
            "resume_data": resume_data,
            "status": "initiated",
            "current_stage": "extraction",
        }
        extracted_results = await extractor_agent.run([{"role": "user", "content": str(resume_data)}])
        workflow_context.update(
             {"extracted_data": extracted_results, "current_stage": "analysis"}
        )
        analyzed_data = await analyzer_agent.run([{"role": "user", "content": str(extracted_results)}])
        print(analyzed_data)
        print('wait here !')

if __name__ == "__main__":
    asyncio.run(main())