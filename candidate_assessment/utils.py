from candidate_assessment import models

class Questions:
    @staticmethod
    def get_level_of_sufficiency():
        questions = [
            models.Question(
                text="Препятствия стимулируют Вас?"
            )
        ]
        return questions
