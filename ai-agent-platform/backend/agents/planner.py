from config.models import planner_llm
from schemas.planner_schema import PlannerOutput

planner_llm = planner_llm.with_structured_output(
    PlannerOutput
)

def planner_agent(state):

    task = state["user_task"]

    prompt = f"""
    Break this software task into
    implementation steps.

    Task:
    {task}
    """

    response = planner_llm.invoke(prompt)

    return {
        "plan": response.tasks
    }