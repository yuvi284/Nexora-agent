import os

WORKSPACE_DIR = "workspace"

def write_files(generated_code):

    files = generated_code["files"]

    for file in files:

        file_path = os.path.join(
            WORKSPACE_DIR,
            file["path"]
        )

        os.makedirs(
            os.path.dirname(file_path),
            exist_ok=True
        )

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(file["content"])

    return {
        "status": "success",
        "files_written": len(files)
    }