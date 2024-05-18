def process_answers(answers):
    motivation_questions = [1, 4, 5, 7, 8]
    conformity_questions = [11, 13, 16, 17, 20]
    motivation_score = 0
    conformity_score = 0

    for question, answer in answers.items():
        if question in motivation_questions:
            if answer == 'A':
                motivation_score += 1
        elif question in conformity_questions:
            if answer == 'B':
                conformity_score += 1

    return motivation_score, conformity_score

def interpret_results(motivation_score, conformity_score):
    motivation_levels = {
        10: "высокий уровень мотивации к успеху",
        7: "уровень выше среднего мотивации к успеху",
        5: "средний уровень мотивации к успеху",
        3: "уровень ниже среднего мотивации к успеху",
        0: "низкий уровень мотивации к успеху"
    }

    conformity_levels = {
        10: "самостоятельность, независимость суждений и поведения",
        7: "уровень выше среднего независимости суждений и поведения",
        5: "средний уровень конформизма",
        3: "уровень ниже среднего зависимости суждений и поведения от окружающих",
        0: "выраженный конформизм, зависимость от мнения других"
    }

    motivation_level = None
    conformity_level = None

    for level, description in motivation_levels.items():
        if motivation_score >= level:
            motivation_level = description
            break

    for level, description in conformity_levels.items():
        if conformity_score >= level:
            conformity_level = description
            break

    return motivation_level, conformity_level
