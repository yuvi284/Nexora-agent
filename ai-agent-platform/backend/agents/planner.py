from config.models import planner_llm
from schemas.planner_schema import PlannerOutput
from utils.logger import log_step

planner_llm = planner_llm.with_structured_output(
    PlannerOutput
)

def planner_agent(state):

    log_step("planner", "Planning task...")

    task = state["user_task"]

    prompt = f"""
    Break this software task into
    implementation steps.

    Task:
    {task}
    """

    response = planner_llm.invoke(prompt)

    log_step(
        "planner",
        f"Generated {len(response.tasks)} steps"
    )

    return {
        "plan": response.tasks
    }