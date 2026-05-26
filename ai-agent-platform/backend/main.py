from pprint import pprint

from graph.workflow import graph
from tools.file_writer import write_files
from tools.executor import execute_project

result = graph.invoke({
    "user_task": "Build calculator app in Python",
    "retries": 0
})

generated_code = result["generated_code"]

write_files(generated_code)

execution_result = execute_project(
    generated_code["test_command"]
)

pprint(execution_result)