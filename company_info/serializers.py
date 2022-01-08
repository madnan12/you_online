from django.contrib.postgres import fields
from rest_framework import serializers
from .models import Apply, Company, FavouriteJob, Job, Education, Currency,Country, Job_Profile,State,City, Language, Industry, Skill,Job_Experience,Job_Project, Job_Endoresements

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

class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=FavouriteJob
        fields=['job','user']

class JobExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job_Experience
        fields='__all__'

class JobProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job_Project
        fields='__all__'

class Job_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job_Profile
        fields='__all__'

class Job_EndoresementsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job_Endoresements
        fields='__all__'

#####################################  UPDATE SERIALIZERS   ##################################

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
class GetJobSerializer(serializers.ModelSerializer):
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
        fields=['id','company','title','experience','minsalary','maxsalary','mobile','description','language','country','state','city','location','type','currency','education','industry','employeetype','duration','skill','is_deleted']
    
class GetFavouriteSerializer(serializers.ModelSerializer):
    job=serializers.StringRelatedField()
    user=serializers.StringRelatedField()
    class Meta:
        model=FavouriteJob
        fields=['id','job','user','created_at']


class GetJobExperienceSerializer(serializers.ModelSerializer):
    industry=serializers.StringRelatedField()
    class Meta:
        model=Job_Experience
        fields=['title','empoyeetype','companyname','location','start_date','end_date','headline','industry','description']

class GetJobProjectSerializer(serializers.ModelSerializer):
    accociated_with=serializers.StringRelatedField()
    class Meta:
        model=Job_Project
        fields=['name','start_date','end_date','accociated_with','project_url','description']

class GetJob_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job_Profile
        fields="__all__"
