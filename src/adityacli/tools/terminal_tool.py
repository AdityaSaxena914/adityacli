import subprocess


def run_command(command: str):
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        shell=True
    )

    return {
        "success": result.returncode == 0,
        "stdout": result.stdout,
        "stderr": result.stderr
    }