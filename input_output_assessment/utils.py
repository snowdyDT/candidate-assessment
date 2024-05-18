from typing import Optional

def get_answers(questions: dict) -> dict:
    answers = dict()
    for question, text in questions.items():
        if text == 'Если Вы сидите дома у окна с книгой в плохую погоду, то чем вы думаете?':
            answer = input(f"{text} (A) Как хорошо дома! / (B) Отличная книга!: ")
        else:
            answer = input(f"{text} (A) да / (B) нет: ")
        while answer not in ['A', 'B']:
            print("Пожалуйста, введите 'A' для ответа 'да' или 'B' для ответа 'нет'.")
            answer = input(f"{text} (A) да / (B) нет: ")
        answers[question] = answer
    return answers

def get_score(answers: dict, scores: dict) -> int:
    score = 0
    for question, answer in answers.items():
        if question in scores[answer]:
            score += 1
    return score


def get_level(score: int, levels: dict) -> Optional[str]:
    result = None
    for level, description in levels.items():
        if score >= level:
            result = description
            break
    return result
