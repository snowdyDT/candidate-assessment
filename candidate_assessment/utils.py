from candidate_assessment import models

class Questions:
    @staticmethod
    def get_level_of_sufficiency():
        questions = [
            models.Question(
                text="Препятствия стимулируют Вас?"
            ),
            models.Question(
                text="Когда Вы работаете без вдохновения, это обычно заметно?"
            ),
            models.Question(
                text="Иногда Вы откладываете то, что нужно сделать сейчас?"
            ),
            models.Question(
                text="В жизни нужно полагаться только на самого себя?"
            ),
            models.Question(
                text="В жизни мало вещей более важных, чем деньги?"
            ),
        ]
        return questions
