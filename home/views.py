from django.shortcuts import render,redirect, get_object_or_404
from .models import Quiz, Question, Answer, QuizScore
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.timezone import timedelta
from django.contrib import messages

# Create your views here.

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
from django.utils.dateparse import parse_datetime



def start_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    return render(request, 'quiz/start_quiz.html', {'quiz': quiz, 'questions': questions})






@login_required
def submit_quiz(request, quiz_id):
    # Check if the user has already submitted the quiz
    if request.session.get(f'quiz_submitted_{quiz_id}', False):
        messages.error(request, "You have already submitted this quiz.")
        return redirect('quiz_list')  # Redirect to the quiz list or another page
    # Check if the start time is set and if the time limit has been exceeded
    start_time = request.session.get(f'quiz_start_time_{quiz_id}')
    if start_time:
        start_time = timezone.make_aware(start_time)  # Ensure the time is timezone-aware
        if timezone.now() > start_time + timedelta(minutes=2):
            messages.error(request, "Time limit exceeded. Quiz submission is not allowed.")
            return redirect('quiz_list')  # Redirect to the quiz list or another page

    if request.method == 'POST':
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        questions = Question.objects.filter(quiz=quiz)
        score = 0

        for question in questions:
            submitted_answer_id = request.POST.get(f'question_{question.id}')
            if submitted_answer_id:
                submitted_answer = get_object_or_404(Answer, pk=submitted_answer_id)
                if submitted_answer.is_correct:
                    score += 1

        # Calculate the percentage score
        total_questions = questions.count()
        percentage_score = (score / total_questions) * 100 if total_questions > 0 else 0

        # Save the quiz score to the database
        user = request.user
        quiz_score = QuizScore(user=user, quiz=quiz,total_question = total_questions, score=score, percentage_score=percentage_score)
        quiz_score.save()

        # Mark the quiz as submitted in the session
        request.session[f'quiz_submitted_{quiz_id}'] = True

        # Render the results page
        return render(request, 'quiz/quiz_result.html', {
            'quiz': quiz,
            'questions': questions,
            'score': score,
            'percentage_score': percentage_score,
            'start_time': timezone.now(),  # Pass the start time to the template

        })
    
    # If request method is not POST, redirect to quiz list
    return redirect('quiz_list')
