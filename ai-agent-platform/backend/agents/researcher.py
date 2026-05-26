from config.models import research_llm

def research_agent(state):

    task = state["user_task"]

    prompt = f"""
    Research best technologies, libraries,
    and implementation strategy for:

    {task}
    """

    response = research_llm.invoke(prompt)

    return {
        "research_data": response.content
    }