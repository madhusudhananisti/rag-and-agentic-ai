import asyncio
import logging
from beeai_framework.agents.experimental import RequirementAgent
from beeai_framework.memory import UnconstrainedMemory
from beeai_framework.backend import ChatModel, ChatModelParameters

async def minimal_tracked_agent_example():
    print("Inside agent running")
    """
    Minimal RequirementAgent
    """
    
    llm = ChatModel.from_name("watsonx:meta-llama/llama-4-maverick-17b-128e-instruct-fp8", ChatModelParameters(temperature=0))
    # CONSISTENT SYSTEM PROMPT (used in all examples)
    SYSTEM_INSTRUCTIONS = """You are an expert cybersecurity analyst specializing in threat assessment and risk analysis.
    Your methodology:

    Analyze the threat landscape systematically

    Research authoritative sources when available

    Provide comprehensive risk assessment with actionable recommendations

    Focus on practical, implementable security measures"""
    #Minimal RequirementAgent
    minimal_agent = RequirementAgent(
        llm=llm,
        tools=[],  # No tools yet
        memory=UnconstrainedMemory(),
        instructions=SYSTEM_INSTRUCTIONS
    )
    #CONSISTENT QUERY (used in all examples)
    ANALYSIS_QUERY = """Analyze the cybersecurity risks of quantum computing for financial institutions. 
    What are the main threats, timeline for concern, and recommended preparation strategies?"""
    result = await minimal_agent.run(ANALYSIS_QUERY)
    print(f"\n💬 Pure LLM Analysis:\n{result.answer.text}")


async def main() -> None:
    print("Main called")
    #logging.getLogger('asyncio').setLevel(logging.DEBUG)
    await minimal_tracked_agent_example()

if __name__ == "__main__":
    asyncio.run(main())