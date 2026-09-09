def generate_quiz(topic):
    return f"""
Create a 5-question multiple-choice quiz about {topic}.

Give:
1. Question
2. Four options
3. Correct answer

Keep the questions suitable for a beginner.
"""

def create_study_plan(topic, days):
    return f"""
Create a {days}-day study plan for learning {topic}.

For each day give:
- Topic
- What to learn
- Small practice task

Keep it realistic for a student.
"""