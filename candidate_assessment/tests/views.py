from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Test, Question, AnswerChoice, UserResponse
from .forms import AnswerForm


@login_required
def take_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = Question.objects.filter(test=test)

    if request.method == 'POST':
        form = AnswerForm(request.POST, questions=questions)
        if form.is_valid():
            for question in questions:
                answer_id = form.cleaned_data[f'question_{question.id}']
                answer = AnswerChoice.objects.get(id=answer_id)
                UserResponse.objects.create(user=request.user, question=question, answer=answer)
            return redirect('test_result', test_id=test.id)
    else:
        form = AnswerForm(questions=questions)

    return render(request, 'tests/take_test.html', {'test': test, 'form': form})


@login_required
def test_result(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    user_responses = UserResponse.objects.filter(user=request.user, question__test=test)

    motivation_score = 0
    independence_score = 0

    motivation_questions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    independence_questions = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for response in user_responses:
        question_number = response.question.id
        answer_text = response.answer.text

        if question_number in motivation_questions:
            if (question_number in [1, 4, 5, 7, 8] and answer_text == 'А') or (
                    question_number in [2, 3, 6, 9, 10] and answer_text == 'Б'):
                motivation_score += 1

        if question_number in independence_questions:
            if (question_number in [12, 14, 15, 18, 19] and answer_text == 'А') or (
                    question_number in [11, 13, 16, 17, 20] and answer_text == 'Б'):
                independence_score += 1

    return render(request, 'tests/test_result.html', {
        'test': test,
        'motivation_score': motivation_score,
        'independence_score': independence_score,
    })
