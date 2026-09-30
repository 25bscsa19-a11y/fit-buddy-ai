def generate_workout_plan_with_flash(user_details: str, user_feedback: str) -> str:
    """
    Use Gemini 1.5 Pro to refine the workout plan based on user feedback.
    """
    prompt = f"""
You are a professional fitness trainer assistant.

Here's the original 7-day workout plan:
{original_plan}

User feedback:
"{user_feedback}"

Based on the feedback, revise the relevant parts of the workout plan. Keep the format and rest of the plan unchanged if not needed.
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error updating plan: {e}"