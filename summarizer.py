def summarize_context(input_text, llm):
    """Summarize the given text to maintain a concise context."""
    try:
        prompt = f"Summarize the following conversation context: {input_text}"
        summary = llm.invoke(input={"user_input": prompt})
        return summary.content.strip()
    except Exception as e:
        return f"Unable to summarize the context: {str(e)}"





