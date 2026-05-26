from config.models import debug_llm

from schemas.coder_schema import CodingOutput
from utils.logger import log_step


debug_llm = debug_llm.with_structured_output(
    CodingOutput
)


def debug_agent(state):

    log_step(
        "debugger",
        "Debugging project..."
    )

    task = state["user_task"]

    current_code = state["generated_code"]

    execution_result = state["execution_result"]

    prompt = f"""
You are an elite debugging engineer.

The generated project failed.

TASK:
{task}

ERRORS:
{execution_result["stderr"]}

CURRENT CODE:
{current_code}

Fix the project.

IMPORTANT:
- Return ONLY structured output
- Fix ALL syntax issues
- Fix ALL failing tests
- No explanations
"""

    response = debug_llm.invoke(prompt)

    log_step(
        "debugger",
        f"Retry attempt: {state['retries'] + 1}"
    )

    return {
        "generated_code": response.dict(),
        "retries": state["retries"] + 1
    }