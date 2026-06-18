# User Prompt – Summary Improvement Agent

## INPUTS
The AI agent will receive:
1. Constitution File
2. Specification File
3. Raw Text Chunk
4. Previous Summary Context
5. User Instruction

## TASK
Analyze the supplied Raw Text Chunk and the Previous Summary Context carefully.
Apply the exact modifications, additions, or structural updates requested in the User Instruction.
Generate the final updated, improved summary by strictly adhering to the Constitution and Specification guidelines.

## DATA PACKET
--- START OF DATA ---

[RAW TEXT CHUNK FROM DOCUMENT]
{chunk_text}

[PREVIOUS SUMMARY CONTEXT]
{previous_summary}

[USER INSTRUCTION]
{user_instruction}

--- END OF DATA ---

Return ONLY the final specification-compliant improved summary text.