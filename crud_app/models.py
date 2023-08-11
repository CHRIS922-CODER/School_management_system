from django.db import models


class Course(models.Model):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    course_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course_name}"

class Unit(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)  
    unit_code = models.CharField(max_length=20,unique=True)
    title = models.CharField(max_length=100)
    cat1 = models.DecimalField(max_digits=5, decimal_places=2)
    cat2 = models.DecimalField(max_digits=5, decimal_places=2)
    cat3 = models.DecimalField(max_digits=5, decimal_places=2)
    final_exam = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.unit_code}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=20, unique=True)
    course_name = models.ForeignKey(Course,on_delete=models.CASCADE)
    unit_code = models.ForeignKey(Unit, on_delete=models.CASCADE,null=True)
    enrolled = models.BooleanField(default=False)
    graded = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.reg_no}"

class StudentMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    unit_code = models.ForeignKey(Unit, on_delete=models.CASCADE)
    cat1 = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, null=True)
    cat2 = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, null=True)
    cat3 = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, null=True)
    exam_marks = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, null=True)
    grade = models.CharField(max_length=1, default=None, null=True)

    def calculate_grade(self):
        average_grade = self.cat1 + self.cat2 + self.cat3 + self.exam_marks
        if average_grade >= 70:
            self.grade = 'A'
        elif average_grade >= 60:
            self.grade = 'B'
        elif average_grade >= 50:
            self.grade = 'C'
        elif average_grade >= 40:
            self.grade = 'D'
        else:
            self.grade = 'F'

    def save(self, *args, **kwargs):
        self.calculate_grade()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"student: {self.student} Grade: {self.grade}"







