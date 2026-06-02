import difflib


def generate_diff(old_content, new_content):
    return "\n".join(
        difflib.unified_diff(
            old_content.splitlines(),
            new_content.splitlines(),
            lineterm=""
        )
    )