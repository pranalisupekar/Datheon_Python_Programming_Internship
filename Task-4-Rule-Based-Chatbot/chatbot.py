import json
import re
import os

print("===================================")
print("   Customer Support Chatbot")
print("===================================")

try:
    path = os.path.join(os.path.dirname(__file__), "sample_faq.json")

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

except (FileNotFoundError, json.JSONDecodeError, OSError) as error:
    print("Error loading FAQ file:", error)
    raise SystemExit

greetings = data.get("greetings", [])
faqs = data.get("faqs", [])

state = "greeting"


def get_response(user_input):
    global state

    question = user_input.lower().strip()

    if not question:
        return "Please enter a question."

    if re.fullmatch(r"(bye|exit|quit)[.! ]*", question):
        state = "exit"
        return "Goodbye! Have a nice day!"

    responses = []

    for greeting in greetings:
        pattern = r"\b" + re.escape(greeting.lower()) + r"\b"

        if re.search(pattern, question):
            responses.append("Hello! Welcome! How can I help you?")
            break

    state = "intent_identification"

    for faq in faqs:
        faq_question = faq.get("question", "").lower()
        words = re.findall(r"\b[a-z]+\b", faq_question)

        ignored_words = [
            "what", "are", "your", "how", "do", "i",
            "when", "will", "the", "of", "my", "is",
            "a", "to", "and", "you", "we", "our"
        ]

        keywords = [
            word for word in words
            if word not in ignored_words and len(word) > 2
        ]

        matched_keywords = 0

        for word in keywords:
            pattern = r"\b" + re.escape(word) + r"s?\b"

            if re.search(pattern, question):
                matched_keywords += 1

        if keywords and matched_keywords / len(keywords) >= 0.5:
            answer = faq.get("answer", "Sorry, no answer is available.")

            if answer not in responses:
                responses.append(answer)

    if responses:
        state = "resolution"
        return "\n".join(responses)

    state = "fallback"

    return (
        "Sorry, I could not understand your question.\n"
        "Please ask about business hours, project submission, "
        "or your certificate."
    )


print("\nWelcome! Ask me a question.")
print("Type 'bye', 'exit', or 'quit' to stop.\n")

state = "greeting"

while state != "exit":
    try:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)

    except (EOFError, KeyboardInterrupt):
        print("\nBot: Goodbye!")
        state = "exit"