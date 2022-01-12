from django.contrib import admin
from django.contrib.admin.helpers import AdminField
from .models import AdminBlog, AdminJob, Blog, Blog_Category, Company, Job, Education, Currency,Country, Job_Category, Job_Endoresements, Job_Experience, Job_Profile, Job_Project,State,City, Language, Industry, Skill,FavouriteJob
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=['user', 'name','email','mobile','address','logo','is_deleted']
    
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display=['company', 'user','title','experience','minsalary','maxsalary', 'mobile', 'language','country','state','city','location','type','currency','education','industry','employeetype','duration','skill','is_deleted','created_at']

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

@admin.register(Job_Profile)
class JobProfileAdmin(admin.ModelAdmin):
    list_display=['headline','first_name','last_name','logo','about']

@admin.register(Job_Category)
class Job_CategoryAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(Job_Endoresements)
class Job_EndoresementsAdmin(admin.ModelAdmin):
    list_display=['profile1','profile2','skill','text']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['user','category','title','description','body','created_at','is_deleted']

@admin.register(Blog_Category)
class Blog_CategoryAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(AdminJob)
class AdminJobAdmin(admin.ModelAdmin):
    list_display=['job','user','created_at']

@admin.register(AdminBlog)
class AdminBlogAdmin(admin.ModelAdmin):
    list_display=['blog','user','created_at']
