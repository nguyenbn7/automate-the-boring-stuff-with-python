#! python3
"""random_quiz_generator.py - Creates quizzes with questions and answers in random order,
along with the answer key.

* Note: I use pathlib rather than os due to simplicity to use and argparse for handle argument.
"""
from pathlib import Path
import random

capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}


def generate_quizzes_and_answers(no_quizzes: int | None, out: str | None):
    current_path = (
        Path(out).resolve()
        if not out or (out and len(out))
        else Path(__file__).parent.resolve()
    )
    current_path.mkdir(parents=True, exist_ok=True)

    quiz_path = current_path / "quiz"
    quiz_path.mkdir(parents=True, exist_ok=True)

    quiz_answers_path = current_path / "quiz_answers"
    quiz_answers_path.mkdir(parents=True, exist_ok=True)

    for quiz_num in range(no_quizzes or 35):
        with open(quiz_path / f"capitals_quiz_{quiz_num + 1}.txt", "w") as quiz_file:
            with open(
                quiz_answers_path / f"capitals_quiz_answers_{quiz_num + 1}.txt",
                "w",
            ) as answer_key_file:
                # Write out the header for the quiz.
                quiz_file.write("Name:\n\nDate:\n\nPeriod:\n\n")
                quiz_file.write(
                    (" " * 20) + f"State Capitals Quiz (Form {quiz_num + 1})"
                )
                quiz_file.write("\n\n")

                # Shuffle the order of the states.
                states = list(capitals.keys())
                random.shuffle(states)

                for question_num in range(len(capitals)):
                    correct_answer = capitals[states[question_num]]
                    wrong_answers = list(capitals.values())

                    del wrong_answers[wrong_answers.index(correct_answer)]
                    wrong_answers = random.sample(wrong_answers, 3)
                    answer_options = wrong_answers + [correct_answer]
                    random.shuffle(answer_options)

                    quiz_file.write(
                        f"{question_num + 1}. What is the capital of {states[question_num]}?\n"
                    )
                    for i, answer in enumerate(answer_options):
                        quiz_file.write(f"    {'ABCD'[i]}. {answer}\n")
                    quiz_file.write("\n")

                    answer_key_file.write(
                        f"{question_num + 1}. {'ABCD'[answer_options.index(correct_answer)]}\n"
                    )


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument(
        "-nq",
        "--no-quiz",
        nargs="?",
        help="Total of quiz files generated. Default 35",
        type=int,
    )

    parser.add_argument(
        "-o",
        "--out",
        nargs="?",
        help="Destination folder. Default current folder of this file",
    )

    args = parser.parse_args()

    no_quiz, out = args.no_quiz, args.out

    generate_quizzes_and_answers(no_quiz, out)
