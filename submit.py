# 4. API: Update workout plan based on user feedback 
 @router.post("/update-plan/{user_id}", response_model=dict) 
def update_user_plan(user_id: int, data: FeedbackRequest): 
    original = get_original_plan(user_id) 
    if not original:

return {"error": "Original plan not found for this user."} 
updated = update_workout_plan(original, data.feedback) 
update_plan(user_id, updated)

return {"updated_plan": updated}

