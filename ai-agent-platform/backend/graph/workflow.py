from langgraph.graph import StateGraph, END

from graph.state import AgentState

from agents.planner import planner_agent
from agents.researcher import research_agent
from agents.coder import coding_agent
from agents.writer import writer_agent
from agents.executor import executor_agent
from agents.debugger import debug_agent


# =========================
# Retry Logic
# =========================

def should_retry(state):

    execution_result = state["execution_result"]

    # Success
    if execution_result["success"]:
        print("\n[SYSTEM] Workflow completed successfully")
        return "success"

    # Stop after max retries
    if state["retries"] >= 3:
        print("\n[SYSTEM] Max retries reached")
        return "failed"

    print(
        f"\n[SYSTEM] Retrying... "
        f"Attempt {state['retries'] + 1}"
    )

    # Retry
    return "retry"


# =========================
# Workflow Graph
# =========================

workflow = StateGraph(AgentState)

# Nodes
workflow.add_node("planner", planner_agent)

workflow.add_node("researcher", research_agent)

workflow.add_node("coder", coding_agent)

workflow.add_node("writer", writer_agent)

workflow.add_node("executor", executor_agent)

workflow.add_node("debugger", debug_agent)

# Entry Point
workflow.set_entry_point("planner")

# Main Flow
workflow.add_edge("planner", "researcher")

workflow.add_edge("researcher", "coder")

workflow.add_edge("coder", "writer")

workflow.add_edge("writer", "executor")

# Retry Logic
workflow.add_conditional_edges(
    "executor",
    should_retry,
    {
        "success": END,
        "retry": "debugger",
        "failed": END
    }
)

# Retry Path
workflow.add_edge("debugger", "writer")

# Compile
graph = workflow.compile()



