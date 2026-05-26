from config.models import research_llm
from utils.logger import log_step

def research_agent(state):

    log_step(
        "researcher",
        "Researching technologies..."
    )

    task = state["user_task"]

    response = research_llm.invoke(
        f"Research best implementation for: {task}"
    )

    log_step(
        "researcher",
        "Research completed"
    )

    return {
        "research_data": response.content
    }