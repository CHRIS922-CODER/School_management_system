from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'reg_no', 'course_name','unit_code']

class StudentMarksForm(forms.ModelForm):
    class Meta:
        model = StudentMarks
        fields = ['student', 'unit_code','cat1', 'cat2','cat3','exam_marks']
    def clean(self):
        cleaned_data = super().clean()
        cat1 = cleaned_data.get('cat1')
        cat2 = cleaned_data.get('cat2')
        cat3 = cleaned_data.get('cat3')
        exam_marks = cleaned_data.get('exam_marks')
        unit_filtered = cleaned_data.get('unit_code')
        unit = Unit.objects.get(unit_code=unit_filtered)


        if cat1 > unit.cat1:
            raise forms.ValidationError(f"CAT1 marks cannot exceed the maximum of {unit.cat1} marks.")
        if cat2 > unit.cat2:
            raise forms.ValidationError(f"CAT2 marks cannot exceed the maximum of {unit.cat2} marks.")
        if cat3 > unit.cat3:
            raise forms.ValidationError(f"CAT3 marks cannot exceed the maximum of {unit.cat3} marks.")       

        if exam_marks and unit and exam_marks > unit.final_exam:
            raise forms.ValidationError(f"Exam marks cannot exceed the maximum of {unit.exam_marks} marks.")

        return cleaned_data

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

