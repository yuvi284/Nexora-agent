from typing import TypedDict, List, Dict

class AgentState(TypedDict):
    user_task: str
    plan: List[str]
    research_data: str
    generated_code: Dict
    execution_logs: str
    errors: str
    status: str
    retries: int