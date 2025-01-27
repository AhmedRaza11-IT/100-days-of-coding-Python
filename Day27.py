def kbc_game():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Madrid", "Berlin", "Paris", "Lisbon"],
            "answer": 3,
            "lifeline": ["", "", "Paris", ""]  # 50-50 lifeline options
        },
        {
            "question": "Which is the largest planet in our solar system?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "answer": 3,
            "lifeline": ["", "", "Jupiter", "Mars"]
        },
        {
            "question": "Who developed the theory of relativity?",
            "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Marie Curie"],
            "answer": 2,
            "lifeline": ["", "Albert Einstein", "", ""]
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["China", "Japan", "South Korea", "Vietnam"],
            "answer": 2,
            "lifeline": ["", "Japan", "", "China"]
        },
        {
            "question": "Which ocean is the largest by surface area?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": 4,
            "lifeline": ["", "", "", "Pacific Ocean"]
        },
        {
            "question": "Who painted the famous artwork 'Mona Lisa'?",
            "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
            "answer": 3,
            "lifeline": ["", "", "Leonardo da Vinci", ""]
        },
        {
            "question": "What is the smallest continent by land area?",
            "options": ["Europe", "Antarctica", "Australia", "South America"],
            "answer": 3,
            "lifeline": ["", "", "Australia", ""]
        },
    ]

    print("Welcome to KBC - Kaun Banega Crorepati!")
    prize_money = [1000, 2000, 5000, 10000, 20000, 50000, 100000]  # Prize for each question
    total_prize = 0
    lifeline_used = False

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for idx, option in enumerate(q["options"], start=1):
            print(f"{idx}. {option}")

        while True:
            choice = input("\nEnter your answer (1-4) or type 'lifeline' to use 50-50: ").strip().lower()

            if choice == "lifeline":
                if lifeline_used:
                    print("You have already used your lifeline!")
                else:
                    print("\n50-50 Lifeline Activated!")
                    lifeline_used = True
                    for idx, option in enumerate(q["lifeline"], start=1):
                        if option:  # Show only non-empty options
                            print(f"{idx}. {option}")
            else:
                try:
                    choice = int(choice)
                    if 1 <= choice <= 4:
                        if choice == q["answer"]:
                            total_prize += prize_money[i]
                            print(f"Correct! You've won ₹{prize_money[i]}!")
                            break
                        else:
                            print(f"Wrong answer! You won ₹{total_prize}. Better luck next time!")
                            return
                    else:
                        print("Invalid option. Please choose between 1 and 4.")
                except ValueError:
                    print("Invalid input. Please try again.")

    print(f"\nCongratulations! You've won a total of ₹{total_prize}!")

# Start the game
kbc_game()
