from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import Company, Job, Country, State, City

class Company_InfoForm(forms.Form):
    name=forms.CharField(max_length=255)
    email=forms.EmailField()
    mobile=forms.CharField(max_length=255)
    address=forms.CharField()

# class Job_InfoForm(forms.Form):

#     experience_choices=[
#         ('Select Experience','Select Experience'),
#         ('Less 1 year','Less 1 year'),
#         ('More than 1 year','More than 1 year'),
#         ('2-5','2-4'),
#         ('5-7', '5-7'),
 
#     ]


#     country_choices=[
#         ('Select Country','Select Country'),
#         ('Afganistan','Afganistan'),
#         ('USA','USA'),
#         ('India','India'),
#         ('UK','UK'),
#         ('Pakistan','Pakistan'),
#         ('Canada','Canada'),
#         ('Bangladash','Bangladash'),
#         ('China','China'),
#         ('Austlia','Austlia'),
#         ('Norvay','Norvay'),
#         ('Singapur','Singapur'),
#         ('Suadia Arabia','Suadia Arabia'),
#         ('Kinia','Kinia'),
#         ('Zimbawe','Zimbawe'),
#     ]
#     state_choices=[
#         ('Select State','Select State'),
#         ('Punjab','Punjab'),
#         ('Sindh','Sindh'),
#         ('Balochistan', 'Balochistan'),
#         ('KPK','KPK'),
#         ('Gilgit Baltistan','Gilgit Baltistan'),
#     ]

#     city_choices=[
#         ('Select City', 'Select City'),
#         ('Lahore', 'Lahore'),
#         ('Karachi', 'Karachi'),
#         ('Multan', 'Multan'),
#         ('Islamabad', 'Islamabad'),
#         ('Faisalabad', 'Faisalabad'),
#         ('Murree', 'Murree'),
#         ('Rawalpindi', 'Rawalpindi'),
#         ('Sialkot', 'Sialkot'),
#     ]

#     language_choices=[
#         ('Select Language', 'Select Language'),
#         ('English', 'English'),
#         ('Arabic', 'Arabic'),
#         ('Urdu', 'Urdu'),
#     ]

#     job_choices=[
#         ('Select job type', 'Select job type'),
#         ('Web developer', 'Web developer'),
#         ('Web designer', 'Web designer'),
#         ('Project manager', 'Project manager'),
#     ]

#     currency_choices=[
#         ('Select currency', 'Select currency'),
#         ('Dollar', 'Dollar'),
#         ('INR', 'INR'),
#         ('PKR', 'PKR'),
#         ('LIRA', 'LIRA'),
#         ('RIYAL', 'RIYAL'),
#     ]

#     education_choices=[
#         ('Select education', 'Select education'),
#         ('Master', 'Master'),
#         ('Bachelor', 'Bachelor'),
#         ('Intermidiate', 'Intermidiate'),
#         ('Matric', 'Matric'),
#     ]

#     employee_choices=[
#         ('Select employee type', 'Select employee type'),
#         ('Fresh', 'Fresh'),
#         ('Intermediate', 'Intermediate'),
#         ('Senior', 'Senior'),
      
#     ]




#     j_title=forms.CharField(max_length=255)
#     j_experience=forms.ChoiceField(choices=experience_choices)
#     min_salary=forms.IntegerField()
#     max_salary=forms.IntegerField()
#     mobile=forms.CharField(max_length=200)
#     language=forms.ChoiceField(choices=language_choices)
#     country=forms.ChoiceField(choices=country_choices)
#     state=forms.ChoiceField(choices=state_choices)
#     city=forms.ChoiceField(choices=city_choices)
#     j_type=forms.ChoiceField(choices=job_choices)
#     currency=forms.ChoiceField(choices=currency_choices)
#     education=forms.ChoiceField(choices=education_choices)
#     employeetype=forms.ChoiceField(choices=employee_choices)
class Job_InfoForm(forms.ModelForm):
    experience_choices=[
        ('Select Experience','Select Experience'),
        ('Less 1 year','Less 1 year'),
        ('More than 1 year','More than 1 year'),
        ('2-5','2-4'),
        ('5-7', '5-7'),
 
    ]

    job_choices=[
        ('Select job type', 'Select job type'),
        ('Web developer', 'Web developer'),
        ('Web designer', 'Web designer'),
        ('Project manager', 'Project manager'),
    ]

    employee_choices=[
        ('Select employee type', 'Select employee type'),
        ('Fresh', 'Fresh'),
        ('Intermediate', 'Intermediate'),
        ('Senior', 'Senior'),

    ]
    experience=forms.ChoiceField(choices=experience_choices)
    type=forms.ChoiceField(choices=job_choices)
    employeetype=forms.ChoiceField(choices=employee_choices)
    class Meta:
        model=Job
        fields=['title','experience','minsalary','maxsalary','mobile','language','type','country','state','city','currency','education','employeetype']
    



class Company_InfoUpdateForm(forms.ModelForm):
    class Meta:
        model=Company
        fields=['name', 'email','mobile', 'address']
     
class Job_InfoUpdateForm(forms.ModelForm):
    class Meta:
        model=Job
        fields=['title','experience','minsalary','maxsalary','type']

class ApplyForm(forms.Form):
    documents=forms.FileField()
    experience=forms.IntegerField()
    expected=forms.IntegerField()

