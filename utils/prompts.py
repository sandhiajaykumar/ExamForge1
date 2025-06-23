# utils/prompts.py

def get_prompt(text, feature, num_items=None):
    # Set a default number of items if not provided or invalid
    # This default is used if the feature *requires* a number but none is given.
    default_num = 5
    num_items_val = default_num
    if num_items and num_items.isdigit():
        num_items_val = int(num_items)
        # Ensure it's within a reasonable range for the AI (e.g., 1-50 questions/items)
        if not (1 <= num_items_val <= 50): # Cap the request to avoid extremely long generations
            num_items_val = default_num

    if feature == 'mcq':
        return f"Generate {num_items_val} Multiple Choice Questions (MCQs) with 4 options each and clearly mark the 1 correct answer for each MCQ from the following text. Make sure the correct answer is clearly indicated, for example, by stating 'Correct Answer: [Option Letter]':\n\n{text}"
    elif feature == 'assignment':
        return f"Generate {num_items_val} detailed assignment-style long questions from the following content:\n\n{text}"
    elif feature == 'project_ideas':
        return f"Suggest {num_items_val} creative project ideas for students, along with a brief description for each, based on the following topic or content:\n\n{text}"
    elif feature == 'summary_flashcard':
        # For flashcards, num_items_val refers to the number of flashcards/quiz questions
        return f"Summarize the following content in a concise paragraph. Then, generate {num_items_val} flashcards or quiz questions based on the summarized content, with answers provided separately for each flashcard/quiz:\n\n{text}"
    elif feature == 'question_paper':
        # Question paper has a fixed structure (e.g., 5 MCQs, 3 Short, 2 Long)
        # Applying num_items directly here is tricky. For simplicity, we keep it fixed,
        # or you could interpret num_items as "total questions" and adjust proportions.
        # For now, keeping fixed as it's a "paper" format.
        return f"Generate a complete question paper from the following content. Include:\n- 5 Multiple Choice Questions (MCQs) with 4 options and 1 correct answer each.\n- 3 Short Answer Questions (2-3 sentences answers expected).\n- 2 Long Answer Questions (paragraph answers expected).\n\n{text}"
    elif feature == 'default_summary':
        return f"Summarize the following text concisely:\n\n{text}"
    else:
        return f"Summarize the following text:\n\n{text}"