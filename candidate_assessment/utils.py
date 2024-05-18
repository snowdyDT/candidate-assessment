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
                text="Вы стремитесь к новым и оригинальным способам решения проблем?"
            ),
            models.Question(
                text="Вы находите способы достичь поставленных целей, даже если это требует нестандартного подхода?"
            ),
            models.Question(
                text="Вам нравится планировать свои действия?"
            ),
            models.Question(
                text="Вас мотивирует успех и достижение целей?"
            ),
            models.Question(
                text="Вы не боитесь рисковать, чтобы достичь своих целей?"
            ),
            models.Question(
                text="Вам нравится работать над сложными задачами?"
            ),
            models.Question(
                text="Вы стараетесь быть лучше в том, что делаете?"
            ),

            models.Question(
                text="Вы обычно следуете советам окружающих?"
            ),
            models.Question(
                text="Вам нравится быть необычным и выделяться из толпы?"
            ),
            models.Question(
                text="Вы стремитесь быть самостоятельным и принимать решения самостоятельно?"
            ),
            models.Question(
                text="Вам нравится работать в команде?"
            ),
            models.Question(
                text="Вы готовы принимать ответственность за свои решения и поступки?"
            ),
            models.Question(
                text="Вы склонны соглашаться с мнением большинства?"
            ),
            models.Question(
                text="Вас волнует, что другие люди думают о вас?"
            ),
            models.Question(
                text="Вы считаете, что внешние факторы влияют на ваш успех?"
            ),
            models.Question(
                text="Вы верите в свои способности достичь успеха?"
            ),
            models.Question(
                text="Если Вы сидите дома у окна с книгой в плохую погоду, то чем вы думаете?",
                options=["Как хорошо дома!", "Отличная книга!"]
            ),
        ]
        return questions
