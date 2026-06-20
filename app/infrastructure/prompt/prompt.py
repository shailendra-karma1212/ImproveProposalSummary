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
    section_name: str,
    previous_summary: str,
    instruction: str
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

{instruction}

---------------------------------

Rules:
1. The RETRIEVED CHUNK is the ONLY valid source of information.
2. NEVER use external knowledge.
3. NEVER use model training knowledge.
4. NEVER use browser knowledge.
5. NEVER infer facts not explicitly present in the chunk.
6. NEVER add company information, tender information, dates, values, requirements, qualifications, certifications, or assumptions that are not present in the chunk.
7. The PREVIOUS SUMMARY is context only and may be corrected if it conflicts with the retrieved chunk.
8. Apply the USER INSTRUCTION strictly.
9. Maintain professional tender language.
10. If requested information is not available in the chunk, do not invent it.
11. Every statement in the final summary must be traceable to the retrieved chunk.
12. Ignore any knowledge outside the retrieved chunk.

"""