from config.models import coder_llm
from schemas.coder_schema import CodingOutput
from utils.logger import log_step


coder_llm = coder_llm.with_structured_output(
    CodingOutput
)

def coding_agent(state):

    log_step(
        "coder",
        "Generating project code..."
    )
    task = state["user_task"]
    plan = "\n".join(state["plan"])

    prompt = f"""
    You are an elite software engineer.

Generate a COMPLETE runnable project.

IMPORTANT RULES:
- Return ONLY structured output
- No explanations
- No markdown
- No tutorials
- Generate production-ready code
- ALWAYS include unit tests
- ALWAYS include a test command

Task:
{task}

Plan:
{plan}

Generate:
1. Project files
2. Runnable code
3. Unit tests
4. Run command
5. Test command
"""

    response = coder_llm.invoke(prompt)

    log_step(
        "coder",
        f"Generated {len(response.files)} files"
    )
    
    return {
        "generated_code": response.dict()
    }