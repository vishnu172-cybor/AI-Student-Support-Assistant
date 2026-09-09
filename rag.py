import os

def load_notes():
    notes = ""

    for file in os.listdir("documents"):
        if file.endswith(".txt"):
            with open("documents/" + file, "r", encoding="utf-8") as f:
                notes += f.read() + "\n"

    return notes


def search_notes(question):
    notes = load_notes()
    words = question.lower().split()

    chunks = notes.split("\n\n")
    results = []

    for chunk in chunks:
        score = sum(
            1 for word in words
            if len(word) > 2 and word in chunk.lower()
        )

        if score > 0:
            results.append((score, chunk))

    results.sort(reverse=True)

    return "\n\n".join(chunk for score, chunk in results[:3])