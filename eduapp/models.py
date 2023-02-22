from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_instructor = models.BooleanField()


class Category(models.Model):
    category_name = models.CharField(max_length=100)


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.CharField(max_length=300)
    instructor = models.ForeignKey('User',
                                   on_delete=models.CASCADE,
                                   max_length=100)
    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE,
                                 max_length=100)


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=100)
    lesson_description = models.CharField(max_length=300)
    course = models.ForeignKey('Course',
                               on_delete=models.CASCADE,
                               max_length=100)


class Enrollment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, max_length=100)
    course = models.ForeignKey('Course',
                               on_delete=models.CASCADE,
                               max_length=100)
    date_enrolled = models.DateTimeField()


class Review(models.Model):
    user = models.ForeignKey('user', on_delete=models.CASCADE, max_length=100)
    course = models.ForeignKey('Course',
                               on_delete=models.CASCADE,
                               max_length=100)
    review_text = models.CharField(max_length=300)
    review_date = models.DateTimeField()
    rating = models.IntegerField()


class Resource(models.Model):
    resource_name = models.CharField(max_length=100)
    resource_url = models.URLField(max_length=100)
    lesson = models.ForeignKey('Lesson',
                               on_delete=models.CASCADE,
                               max_length=100)
