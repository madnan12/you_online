from typing import Tuple
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
# company model
class Company(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    mobile=models.CharField(max_length=25)
    address=models.TextField()
    description=models.TextField()
    logo=models.ImageField(upload_to='company_logo')
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Company'

    def __str__(self):
        return self.name

# country model
class Country(models.Model):
    name = models.CharField(max_length=40)
    code=models.CharField(max_length=255)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Country'

    def __str__(self):
        return self.code

#state model
class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='State'
        

    def __str__(self):
        return self.name

# city model
class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='City'
        

    def __str__(self):
        return self.name

#language model
class Language(models.Model):
    name=models.CharField(max_length=255)
    code=models.CharField(max_length=255)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Language'
        
    def __str__(self):
        return self.code

# currency model
class Currency(models.Model):
    name=models.CharField(max_length=255)
    code=models.CharField(max_length=255)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Currency'
        
    def __str__(self):
        return self.code

# education model
class Education(models.Model):
    name=models.CharField(max_length=255)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Education'

    def __str__(self):
        return self.name



# industry model
class Industry(models.Model):
    name=models.CharField(max_length=255)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Industry'

    def __str__(self):
        return self.name

# skill model
class Skill(models.Model):
    name = models.CharField(max_length=200)
    is_deleted=models.BooleanField(default=False)

    class Meta:
        db_table='Skill'

    def __str__(self):
        return self.name

# job model
class Job(models.Model):

    experience_choices=[
        ('Select Experience','Select Experience'),
        ('Less 1 year','Less 1 year'),
        ('More than 1 year','More than 1 year'),
        ('2-5','2-4'),
        ('5-7', '5-7'),
 
    ]


    job_choices=[
        ('Web developer', 'Web developer'),
        ('Web designer', 'Web designer'),
        ('Project manager', 'Project manager'),
    ]

    employee_choices=[
        ('Fresh', 'Fresh'),
        ('Intermediate', 'Intermediate'),
        ('Senior', 'Senior'),
      
    ]

    duration_choices=[
        ('7 days', '7 days'),
        ('14 days', '14 days'),
        ('30 days', '30 days'),
      
    ]

    company=models.ForeignKey(Company, on_delete=models.CASCADE, related_name='job_company')
    user=models.ForeignKey(User, on_delete=models.CASCADE,  related_name='job_user')
    title=models.CharField(max_length=255, null=True, blank=True)
    experience=models.CharField(max_length=200, choices=experience_choices ,null=True, blank=True)
    minsalary=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    maxsalary=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    mobile=models.CharField(max_length=200, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    language=models.ForeignKey(Language, null=True, blank=True, on_delete=models.SET_NULL,related_name='job_language')
    country=models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL, related_name='job_country')
    state=models.ForeignKey(State, null=True, blank=True, on_delete=models.SET_NULL, related_name='job_state')
    city=models.ForeignKey(City ,null=True, blank=True, on_delete=models.SET_NULL, related_name='job_city')
    location=models.TextField(null=True, blank=True)
    type=models.CharField(max_length=255, choices=job_choices ,null=True, blank=True)
    currency=models.ForeignKey(Currency ,on_delete=models.SET_NULL,null=True, blank=True, related_name='job_currency')
    education=models.ForeignKey(Education ,on_delete=models.SET_NULL,null=True, blank=True, related_name='job_education')
    industry=models.ForeignKey(Industry ,on_delete=models.SET_NULL,null=True, blank=True, related_name='job_industry')
    employeetype=models.CharField(max_length=255, choices=employee_choices ,null=True, blank=True)
    duration=models.CharField(max_length=255, choices=duration_choices ,null=True, blank=True)
    skill=models.ForeignKey(Skill ,null=True, blank=True, on_delete=models.SET_NULL, related_name='job_skill')
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Job'
    

    def __str__(self):
        return self.title

class Apply(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    job=models.ForeignKey(Job, on_delete=models.CASCADE)
    documents=models.FileField(upload_to='doc/')
    experience=models.IntegerField()
    expected=models.IntegerField()
    class Meta:
        db_table='Apply'

    def __str__(self):
        return str(self.experience)+" "+str(self.expected) 

class FavouriteJob(models.Model):
    job=models.ForeignKey(Job, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='FavouriteJob'
    
    def __str__(self):
        return str(self.job.title)

class Job_Experience(models.Model):
    employee_choices=[
        ('Full Time','Full Time'),
        ('Self Employed','Self Employed'),
        ('Freelance','Freelance'),
        ('Contract','Contract'),
        ('Internship','Internship'),
        ('Apprenticehip','Apprenticehip'),
        ('Seasonal','Seasonal'),
    ]

    title=models.CharField(max_length=255)
    empoyeetype=models.CharField(max_length=255, choices=employee_choices)
    companyname=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateTimeField(auto_now_add=True)
    headline=models.CharField(max_length=255)
    industry=models.ForeignKey(Industry,  on_delete=models.SET_NULL, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Job_Experience'
    
    def __str__(self):
        return self.headline

class Job_Project(models.Model):
    name=models.CharField(max_length=255)
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateTimeField(auto_now_add=True)
    accociated_with=models.ForeignKey(Job_Experience, on_delete=models.SET_NULL, null=True, blank=True)
    project_url=models.CharField(max_length=255)
    description=models.TextField(null=True, blank=True)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table='Job_Project'

    def __str__(self):
        return (self.name)

