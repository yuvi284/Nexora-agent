from langgraph.graph import StateGraph, END

from graph.state import AgentState

from agents.planner import planner_agent
from agents.researcher import research_agent
from agents.coder import coding_agent

workflow = StateGraph(AgentState)

workflow.add_node("planner", planner_agent)
workflow.add_node("researcher", research_agent)
workflow.add_node("coder", coding_agent)

workflow.set_entry_point("planner")

workflow.add_edge("planner", "researcher")
workflow.add_edge("researcher", "coder")
workflow.add_edge("coder", END)

graph = workflow.compile()