# # KBC Solution
#
# # question = ["which language was used to create facebook","python","javascript","c++",]
# questions = [
#         {
#             "question": "What is the capital of France?",
#             "options": ["Madrid", "Berlin", "Paris", "Lisbon"],
#             "answer": 3,
#             "lifeline": ["", "", "Paris", ""]  # 50-50 lifeline options
#         },
#         {
#             "question": "Which is the largest planet in our solar system?",
#             "options": ["Earth", "Mars", "Jupiter", "Venus"],
#             "answer": 3,
#             "lifeline": ["", "", "Jupiter", "Mars"]
#         },
#         {
#             "question": "Who developed the theory of relativity?",
#             "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Marie Curie"],
#             "answer": 2,
#             "lifeline": ["", "Albert Einstein", "", ""]
#         },
#         {
#             "question": "Which country is known as the Land of the Rising Sun?",
#             "options": ["China", "Japan", "South Korea", "Vietnam"],
#             "answer": 2,
#             "lifeline": ["", "Japan", "", "China"]
#         },
#         {
#             "question": "Which ocean is the largest by surface area?",
#             "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
#             "answer": 4,
#             "lifeline": ["", "", "", "Pacific Ocean"]
#         },
#         {
#             "question": "Who painted the famous artwork 'Mona Lisa'?",
#             "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
#             "answer": 3,
#             "lifeline": ["", "", "Leonardo da Vinci", ""]
#         },
#         {
#             "question": "What is the smallest continent by land area?",
#             "options": ["Europe", "Antarctica", "Australia", "South America"],
#             "answer": 3,
#             "lifeline": ["", "", "Australia", ""]
#         },
#     ]
# print("Welcome to KBC - Kaun Banega Crorepati!")
#     levels = [1000, 2000, 5000, 10000, 20000, 50000, 100000]  # Prize for each question
#     total_prize = 0
#     lifeline_used = False
#     for i in range(0,len(questions)):
#         questions = questions[i]
#         print(f"Question for Rs. {levels[i]}:")
#         print(f"{questions['question']}")
#     else:
#         print(f"Total Prize: Rs. {total_prize}")