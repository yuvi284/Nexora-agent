from tools.executor import execute_project


def executor_agent(state):

    generated_code = state["generated_code"]

    result = execute_project(
        generated_code["test_command"]
    )
    
    print("\n========= TEST OUTPUT =========")
    print(result["stderr"])
    print(result["stdout"])

    return {
        "execution_result": result
    }