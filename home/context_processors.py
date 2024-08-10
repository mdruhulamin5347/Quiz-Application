from .models import Quiz
def QuizList(request):
    quizzes = Quiz.objects.all()
    return {'quizzes': quizzes}