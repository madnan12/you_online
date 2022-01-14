from os import read
from django.contrib.postgres import fields
from django.db import models
from django.http import request
from rest_framework import serializers
from rest_framework.views import set_rollback
from .models import AdminBlog, AdminJob, Apply, Blog, Company, FavouriteJob, Job, Education, Currency,Country, Job_Profile, Notification, Post,State,City, Language, Industry, Skill,Job_Experience,Job_Project, Job_Endoresements
from django.contrib.auth.models import User
from django.conf import settings

# default user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email']

# company serializer
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields="__all__"

# job serializer
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields="__all__"

# education serializer
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Education
        fields=['name']

# currency serializer
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model=Currency
        fields=['name','code']

# country serializer
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields=['name','code']

# state serializer
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model=State
        fields=['country' ,'name']

# city serializer
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields=['state','name']

# language serializer
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Language
        fields=['name', 'code']

# industry serializer
class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Industry
        fields=['name']

# skill serializer
class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model=Skill
        fields=['name']

# apply serializer
class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model=Apply
        fields='__all__'

# favourite job serializer
class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=FavouriteJob
        fields=['job','user']

# job experience serializer
class JobExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job_Experience
        fields='__all__'

# job project serializer
class JobProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job_Project
        fields='__all__'

# job profile serializer
class Job_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job_Profile
        fields=['user','logo','headline','first_name','last_name','about']

# job endoresements serializer
class Job_EndoresementsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job_Endoresements
        fields='__all__'

# Post serializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['content','normal_post','blog_post']

# blog serializer
class BlogSerializer(serializers.ModelSerializer):
    post=PostSerializer(read_only=True)
    class Meta:
        model=Blog
        fields=['title','category','description','body','post']

# admin jobs serializer
class AdminJobSerializer(serializers.ModelSerializer):
    job=serializers.StringRelatedField()
    user=serializers.StringRelatedField()
    class Meta:
        model=AdminJob
        fields=['job','user']

# admin blogs serializers
class AdminBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminBlog
        fields=['blog','user']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields='__all__'

#########################  UPDATE SERIALIZERS   ##################################

# company serializer
class UpdateCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=['name','email','mobile','address','description','logo']

# company serializer
class UpdateJobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields=['title','experience','minsalary','maxsalary','mobile','description','language','country','state','city','location','type','currency','education','industry','employeetype','duration','skill']

################################ GET API ######################

# get job serializer
class GetJobSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    company=serializers.StringRelatedField()
    country=serializers.StringRelatedField()
    state=serializers.StringRelatedField()
    city=serializers.StringRelatedField()
    currency=serializers.StringRelatedField()
    education=serializers.StringRelatedField()
    industry=serializers.StringRelatedField()
    skill=serializers.StringRelatedField()
    class Meta:
        model=Job
        fields=['id','user','company','title','experience','minsalary','maxsalary','mobile','description','language','country','state','city','location','type','currency','education','industry','employeetype','duration','skill','created_at']

# get apply serializer
class GetApplySerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Apply
        fields='__all__'

# get favourite serializer
class GetFavouriteSerializer(serializers.ModelSerializer):
    job=serializers.StringRelatedField()
    user=UserSerializer(read_only=True)
    class Meta:
        model=FavouriteJob
        fields=['id','job','created_at','user']

# get job experience serializers
class GetJobExperienceSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    industry=serializers.StringRelatedField()
    class Meta:
        model=Job_Experience
        fields=['user','title','empoyeetype','companyname','location','start_date','end_date','headline','industry','description']

# get job project serializer
class GetJobProjectSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    accociated_with=serializers.StringRelatedField()
    class Meta:
        model=Job_Project
        fields=['user','name','start_date','end_date','accociated_with','project_url','description']

# get job endoresemens serializer
class GetJob_EndoresementsSerializer(serializers.ModelSerializer):
    profile1=serializers.StringRelatedField()
    profile2=UserSerializer(read_only=True)
    skill=serializers.StringRelatedField()
    class Meta:
        model=Job_Endoresements
        fields=['profile2','profile1','skill','text']

# get job profile serializer
class GetJob_ProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    experience=serializers.SerializerMethodField()
    projects=serializers.SerializerMethodField()
    endoresement=serializers.SerializerMethodField()
    logo=serializers.SerializerMethodField()
    class Meta:
        model=Job_Profile
        fields=['user','logo','headline','first_name','last_name','about','experience','projects','endoresement']

    def get_experience(self, value):
        try:
            user=self.context.get('user')
            experience=Job_Experience.objects.filter(user=user, is_deleted=False)
        except Job_Experience.DoesNotExist:
            experience=None
        serializer=GetJobExperienceSerializer(experience, many=True)
        return serializer.data
    
    def get_projects(self, value):
        try:
            user=self.context.get('user')
            projects=Job_Project.objects.filter(user=user, is_deleted=False)
        except Job_Project.DoesNotExist:
            projects=None
        serializer=GetJobProjectSerializer(projects, many=True)
        return serializer.data
    
    def get_endoresement(self, value):
        try:
            user=self.context.get('user')
            projects=Job_Endoresements.objects.filter(profile2=user, is_deleted=False)
        except Job_Endoresements.DoesNotExist:
            pass
        serializer=GetJob_EndoresementsSerializer(projects, many=True)
        return serializer.data

    def get_logo(self, obj):
        request = self.context.get('request')
        logo_url = obj.logo.url
        return settings.YOU_ONLINE+(logo_url)

# get blog serializer
class GetBlogSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    post=PostSerializer(read_only=True)
    category=serializers.StringRelatedField()
    class Meta:
        model=Blog
        fields=['user','category','title','description','body','created_at','post']
