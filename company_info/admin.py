from django.contrib import admin
from .models import Company, Job, Education, Currency,Country, Job_Experience, Job_Project,State,City, Language, Industry, Skill,FavouriteJob
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=['user', 'name','email','mobile','address','logo','is_deleted']
    
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display=['company', 'user','title','experience','minsalary','maxsalary', 'mobile', 'language','country','state','city','location','type','currency','education','industry','employeetype','duration','skill','is_deleted']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display=['name','code']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display=['name','code']

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display=['country','name']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display=['state' ,'name']

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display=[ 'name','code']

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(FavouriteJob)
class FavouriteAdmin(admin.ModelAdmin):
    list_display=['job','user','created_at']

@admin.register(Job_Experience)
class JobExperienceAdmin(admin.ModelAdmin):
    list_display=['title','empoyeetype','companyname','location','start_date','headline','industry','description','is_deleted']

@admin.register(Job_Project)
class JobProjectAdmin(admin.ModelAdmin):
    list_display=['name','start_date','end_date','accociated_with','project_url','description','is_deleted']
