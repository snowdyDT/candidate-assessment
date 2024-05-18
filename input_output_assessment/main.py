from typing import Optional

from input_output_assessment import config
from input_output_assessment import utils


def print_result(answers: dict, score: int, level: Optional[str]) -> None:
    print(f"Ответы: {answers}\nВычисление: {score}\nУровень: {level}\n")

def main():
    motivation_answers = utils.get_answers(config.Questions.motivation_questions.value)
    conformity_answers = utils.get_answers(config.Questions.conformity.value)
    motivation_score = utils.get_score(answers=motivation_answers, scores=config.Scores.motivation.value)
    conformity_score = utils.get_score(answers=conformity_answers, scores=config.Scores.conformity.value)
    motivation_level = utils.get_level(score=motivation_score, levels=config.Level.motivation.value)
    conformity_level = utils.get_level(score=conformity_score, levels=config.Level.conformity.value)

    print("\nРезультаты теста:")
    print('Мотивации')
    print_result(answers=motivation_answers, score=motivation_score, level=motivation_level)
    print('Независимости суждений и поведения:')
    print_result(answers=conformity_answers, score=conformity_score, level=conformity_level)


if __name__ == '__main__':
    main()
