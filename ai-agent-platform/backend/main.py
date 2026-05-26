from pprint import pprint

from graph.workflow import graph

result = graph.invoke({
    "user_task": "Build calculator app in Python",
    "retries": 0
})

pprint(result["execution_result"])