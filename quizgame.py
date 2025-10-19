# quiz_game.py
# Interactive Quiz Game with Single, Multi-select, and Fill-in-the-Blank questions

def run_quiz(questions):
    score = 0

    for q in questions:
        print("\n--------------------------------------")
        print(f"Question: {q['question']}")
        q_type = q['type']

        if q_type == "single":
            # Single choice
            for i, option in enumerate(q['options'], 1):
                print(f"{i}. {option}")
            try:
                answer = int(input("Enter your choice (1-4): "))
                if q['options'][answer - 1].lower() == q['answer'].lower():
                    print("✅ Correct!")
                    score += 1
                else:
                    print(f"❌ Wrong! Correct answer: {q['answer']}")
            except (ValueError, IndexError):
                print("⚠️ Invalid input. Moving to next question.")

        elif q_type == "multi":
            # Multi-select
            print("Choose all correct options (comma-separated, e.g., 1,3):")
            for i, option in enumerate(q['options'], 1):
                print(f"{i}. {option}")
            user_input = input("Your answers: ")
            try:
                selected = [q['options'][int(i.strip()) - 1].lower() for i in user_input.split(",")]
                correct_answers = [ans.lower() for ans in q['answers']]
                if set(selected) == set(correct_answers):
                    print("✅ Correct (all selected right)!")
                    score += 1
                else:
                    print(f"❌ Wrong! Correct answers: {', '.join(q['answers'])}")
            except Exception:
                print("⚠️ Invalid input. Moving to next question.")

        elif q_type == "fill":
            # Fill in the blank
            user_ans = input("Your answer: ").strip().lower()
            if user_ans == q['answer'].lower():
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}")

    print("\n======================================")
    print(f"🎯 Final Score: {score}/{len(questions)}")
    print("======================================")

# --------------------------------------
# Questions list
quiz_questions = [
    {
        "type": "single",
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Mars"
    },
    {
        "type": "multi",
        "question": "Which of the following are programming languages?",
        "options": ["Python", "HTML", "C++", "CSS"],
        "answers": ["Python", "C++"]
    },
    {
        "type": "fill",
        "question": "Fill in the blank: The capital of Japan is ____.",
        "answer": "Tokyo"
    },
    {
        "type": "fill",
        "question": "Fill in the blank: The chemical symbol for water is ____.",
        "answer": "H2O"
    }
]

# Run the quiz
run_quiz(quiz_questions)
