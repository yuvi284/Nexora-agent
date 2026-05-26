from config.models import debug_llm

def debug_agent(state):

    code = state["generated_code"]
    logs = state["execution_logs"]

    prompt = f"""
    Fix this code based on logs.

    CODE:
    {code}

    LOGS:
    {logs}
    """

    response = debug_llm.invoke(prompt)

    return {
        "generated_code": response.content
    }