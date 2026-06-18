# Summary Improvement Specification File

Version: 1.0

## OBJECTIVE
Controls ONLY the output format of the generated improved summary.

## OUTPUT FORMAT RULES
1. **Direct Output**: Start directly with the improved summary text content.
2. **No Explanations**: Do not explain why changes were made, what was added, or how the instruction was applied.
3. **No Conversational Filler**: Absolutely no introductory or outro commentary.
4. **Formatting Alignment**: Use clean markdown structure (such as bullet points or bold headers) ONLY if explicitly requested by the user instruction or if it perfectly matches the previous summary's existing format. Otherwise, return structured paragraph text.
5. **No Markdown Wrappers**: Do not wrap the final output inside code blocks like ```markdown or ```text. Return the raw textual summary directly.