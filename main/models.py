from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name    
SEMESTER_CHOICES = (
    ("1st Semester", "1st Semester"),
    ("2nd Semester", "2nd Semester"),
    ("3rd Semester", "3rd Semester"),
)

LEVEL_CHOICES = (
    ("ND1", "ND1"),
    ("ND2", "ND2"),
    ("HND1", "HND1"),
    ("HND2", "HND2"),
)
 
PROGRAM_CHOICES = (
    ("ND", "ND"),
    ("HND", "HND"),
)

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    semester = models.CharField(max_length=20,choices=SEMESTER_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.code}: {self.name}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    admission_no = models.CharField(max_length=100, unique=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.name + " : " + self.department

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)    
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    test_score = models.SmallIntegerField()
    exam_score = models.SmallIntegerField()
    def __str__(self):
        return self.student + " : " + self.course + " : " + self.score

    @property
    def total_score(self):
        return int(self.test_score) + int(self.exam_score)

class Material(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    file = models.FileField(upload_to="materials")
