import requests

from rag import search_notes
from memory import load_memory, add_topic, add_progress
from tools import generate_quiz, create_study_plan


def ask_ai(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


def run_agent(question):

    # Quiz tool
    if "quiz" in question.lower():
        topic = question.lower().replace("quiz", "").strip()
        prompt = generate_quiz(topic)
        return ask_ai(prompt)

    # Study plan tool
    if "study plan" in question.lower():
        topic = question.lower().replace("study plan", "").strip()
        prompt = create_study_plan(topic, 5)
        return ask_ai(prompt)

    # RAG
    notes = search_notes(question)

    # Memory
    memory = load_memory()

    prompt = f"""
You are an AI Student Support Assistant.

Answer the student's question using ONLY the information in the College documents below.

College documents:
{notes}

Student memory:
{memory}

Student question:
{question}

IMPORTANT RULES:
- Use the College documents as the main source of your answer.
- If the documents contain the exact answer, give that answer directly.
- Do not tell the student to check the syllabus if the answer is already in the documents.
- Do not make up information.
- If the answer is not found in the documents, say:
  "I don't have that information in my documents."
- Keep the answer short and clear.
"""

    answer = ask_ai(prompt)

    # Save learning topics
    if "learn" in question.lower():
        add_topic(question)

    # Save completed topics
    if "completed" in question.lower():
        add_progress(question)

    return answer