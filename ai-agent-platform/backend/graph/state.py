from typing import TypedDict, List, Dict

class AgentState(TypedDict):

    user_task: str

    plan: List[str]

    research_data: str

    generated_code: Dict

    write_result: dict
    
    execution_result: Dict

    retries: int