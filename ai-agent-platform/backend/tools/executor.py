import subprocess
import os

WORKSPACE_DIR = "workspace"

def execute_project(run_command):

    try:

        result = subprocess.run(
            run_command,
            shell=True,
            cwd=WORKSPACE_DIR,
            capture_output=True,
            text=True,
            timeout=30
        )

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }

    except Exception as e:

        return {
            "success": False,
            "stderr": str(e)
        }