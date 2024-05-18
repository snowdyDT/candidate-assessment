from input_output_assessment import utils
from input_output_assessment import config

def main():
    motivation_answers = utils.get_answers(config.Questions.motivation_questions.value)
    conformity_answers = utils.get_answers(config.Questions.conformity.value)
    motivation_score = utils.get_score(answers=motivation_answers, scores=config.Scores.motivation.value)
    conformity_score = utils.get_score(answers=conformity_answers, scores=config.Scores.conformity.value)
    motivation_level = utils.get_level(score=motivation_score, levels=config.Level.motivation.value)
    conformity_level = utils.get_level(score=conformity_score, levels=config.Level.conformity.value)
    print("Результаты теста:")
    print("Уровень мотивации к успеху:", motivation_level)
    print("Уровень независимости суждений и поведения:", conformity_level)

if __name__ == '__main__':
    main()
