from typing import Optional

def get_answers(questions: dict) -> dict:
    answers = dict()
    for question, text in questions.items():
        answer = input(f"{text} (А) да / (Б) нет: ")
        while answer not in ['А', 'Б']:
            print("Пожалуйста, введите 'А' для ответа 'да' или 'Б' для ответа 'нет'.")
            answer = input(f"{text} (А) да / (Б) нет: ")
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
