from input_output_assessment import utils
from input_output_assessment import config

def main():
    answers = {}

    for question, text in config.questions.items():
        answer = input(f"{text} (А) да / (Б) нет: ")
        while answer not in ['А', 'Б']:
            print("Пожалуйста, введите 'А' для ответа 'да' или 'Б' для ответа 'нет'.")
            answer = input(f"{text} (А) да / (Б) нет: ")
        answers[question] = answer

    motivation_score, conformity_score = utils.process_answers(answers)
    motivation_level, conformity_level = utils.interpret_results(motivation_score, conformity_score)

    print("Результаты теста:")
    print("Уровень мотивации к успеху:", motivation_level)
    print("Уровень независимости суждений и поведения:", conformity_level)

if __name__ == '__main__':
    main()
