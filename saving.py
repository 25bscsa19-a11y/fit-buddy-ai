# 3. API: Save user info & generate plan 
@router.post("/generate-plan")
def generate_plan(user_data: UserInput):

try:

save_user(

user_id=user_data.user_id, 
namezuser_data.username, 
age=user_data.age, 
weight=user_data.weight, 
goal=user_data.goal, 
intensity=user_data.intensity

plan = = generate_workout_gemini({ 
                                  "goal": user_data.goal, 
                                  "intensity": user_data.intensity
})

save plan(user data.user id, plan)

return{
"message": "Workout plan generated and saved successfully!",

"workout_plan": plan
}

except Exception as e:

raise HTTPException(status_code=500, detail=f"Something went wrong:{str(e)}")