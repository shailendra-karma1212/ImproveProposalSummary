import os


BASE_DIR = os.path.dirname(__file__)

INPUT_DIR = os.path.join(
    BASE_DIR,
    "input_files"
)


def read_file(filename):

    file_path = os.path.join(
        INPUT_DIR,
        filename
    )

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()


constitution = read_file(
    "Constitution.md"
)

specification = read_file(
    "Specification.md"
)

user_prompt = read_file(
    "User_Prompt.md"
)


def get_summary_improvement_prompt(
    chunk_text: str,
    previous_summary: str,
    user_instruction: str
):

    return f"""
{constitution}

{specification}

{user_prompt}

---------------------------------

RAW CHUNK

{chunk_text}

---------------------------------

PREVIOUS SUMMARY

{previous_summary}

---------------------------------

USER INSTRUCTION

{user_instruction}

---------------------------------

Rules:

1. Use chunk as source of truth.
2. Do not hallucinate.
3. Do not invent facts.
4. Improve summary.
5. Return only final summary.
"""