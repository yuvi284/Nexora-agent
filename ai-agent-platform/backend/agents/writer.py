from tools.file_writer import write_files
from utils.logger import log_step

def writer_agent(state):

    log_step(
        "writer",
        "Writing project files..."
    )

    generated_code = state["generated_code"]

    result = write_files(generated_code)

    log_step(
        "writer",
        f"Written {result['files_written']} files"
    )

    return {
        "write_result": result
    }