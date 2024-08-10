from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()
    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return self.answer_text


class QuizScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    total_question = models.IntegerField(null=True,blank=True)
    score = models.IntegerField()
    percentage_score=models.FloatField(null=True)
    create_at = models.DateTimeField(default=now,blank=True)

    def __str__(self):
        return f"{self.user.username}'s score in {self.quiz.title}: {self.percentage_score}%"
