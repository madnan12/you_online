from django.db.models.query import RawQuerySet
from rest_framework.decorators import api_view
from django.shortcuts import redirect, render
from rest_framework import status
from django.shortcuts import  get_object_or_404
from rest_framework.response import Response
from .serializers import ApplySerializer, CompanySerializer, FavouriteSerializer, GetFavouriteSerializer, GetJobExperienceSerializer, GetJobProjectSerializer, GetJobSerializer, IndustrySerializer, JobExperienceSerializer, JobProjectSerializer, JobSerializer, EducationSerializer, CountrySerializer, SkillSerializer, StateSerializer, CitySerializer, CurrencySerializer, LanguageSerializer, UpdateCompanySerializer, UpdateJobSerializer
from .models import City, Company, Country, Currency, Education, Apply, FavouriteJob,Industry, Job, Job_Experience, Job_Project, Language, Skill, State
from django.db.models import Max, Min, manager
from django.db.models import Q
from .forms import Company_InfoForm, Job_InfoForm, Company_InfoUpdateForm, Job_InfoUpdateForm, ApplyForm
from django.views.decorators.csrf import csrf_exempt

from company_info import serializers
###############################  FETCHING API ########################################

@api_view(['GET'])
def get_jobs_api(request):
    jobs=Job.objects.filter(is_deleted=False)
    serializer=GetJobSerializer(jobs, many=True)
    return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_single_job_api(request):
    
    try:
        job=Job.objects.get(id=id, is_deleted=False)
        serializer=GetJobSerializer(job)
        return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)
    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_favourite_api(request):
    fav=FavouriteJob.objects.all()
    serializer=GetFavouriteSerializer(fav, many=True)
    return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_favourite_api(request):
    fav=FavouriteJob.objects.all()
    serializer=GetFavouriteSerializer(fav, many=True)
    return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_job_experience_api(request):
    experience=Job_Experience.objects.filter(is_deleted=False)
    serializer=GetJobExperienceSerializer(experience, many=True)
    return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_job_project_api(request):
    project=Job_Project.objects.filter(is_deleted=False)
    serializer=GetJobProjectSerializer(project, many=True)
    return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)


############################### CREATE API ###########################################
# add company api
@api_view(['POST'])
def add_company(request):
    serializer=CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)
    return Response({"success": False, 'response': {'message': serializer.errors}},
			status=status.HTTP_400_BAD_REQUEST)

# add job api
@api_view(['POST'])
def add_job(request):
    serializer=JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)
    return Response({"success": False, 'response': {'message': serializer.errors}},
			status=status.HTTP_400_BAD_REQUEST)

# add eductation api
@api_view(['POST'])
def add_education(request):
    serializer=EducationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)
    return Response({"success": False, 'response': {'message': serializer.errors}},
			status=status.HTTP_400_BAD_REQUEST)

# add country api
@api_view(['POST'])
def add_country(request):
    serializer=CountrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)
    return Response({"success": False, 'response': {'message': serializer.errors}},
			status=status.HTTP_400_BAD_REQUEST)

# add state api
@api_view(['POST'])
def add_state(request):
    serializer=StateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)
    return Response({"success": False, 'response': {'message': serializer.errors}},
			status=status.HTTP_400_BAD_REQUEST)

# add city api
@api_view(['POST'])
def add_city(request):
    serializer=CitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)
    return Response({"success": False, 'response': {'message': serializer.errors}},
			status=status.HTTP_400_BAD_REQUEST)

# add currency api
@api_view(['POST'])
def add_currency(request):
    serializer=CurrencySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)
    return Response({"success": False, 'response': {'message': serializer.errors}},
			status=status.HTTP_400_BAD_REQUEST)

# add language api
@api_view(['POST'])
def add_language(request):
    serializer=LanguageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)
    return Response({"success": False, 'response': {'message': serializer.errors}},
			status=status.HTTP_400_BAD_REQUEST)

# add industry api
@api_view(['POST'])
def add_industry(request):
    serializer=IndustrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)
    return Response({"success": False, 'response': {'message': serializer.errors}},
			status=status.HTTP_400_BAD_REQUEST)

# add skill api
@api_view(['POST'])
def add_skill(request):
    serializer=SkillSerializer(data=request.data)
    if serializer.is_valid():
        name=request.data['name']
        skill=Skill.objects.create(name=name)
        return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)
    return Response({"success": False, 'response': {'message': serializer.errors}},
			status=status.HTTP_400_BAD_REQUEST)

# add apply api
@api_view(['POST'])
def add_apply_api(request):
    user=request.user
    request.data['user'] = user.id
    serializer=ApplySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)
    return Response({"success": False, 'response': {'message': serializer.errors}},
			status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST',])
def add_favourite_api(request):
    job_id=request.data.get('job')
    try:
        job=Job.objects.get(id=job_id)
        print("adnan")
    except Job.DoesNotExist:
        pass
    try:
        fav=FavouriteJob.objects.get(user=request.user, job=job)
        fav.delete()
        return Response({"success": 'Remove from favourite'} ,status=status.HTTP_200_OK)
    except FavouriteJob.DoesNotExist:
        fav=FavouriteJob.objects.create(user=request.user, job=job)
        serializer=FavouriteSerializer(fav)
        return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)

# add job experience api
@api_view(['POST'])
def add_job_experience_api(request):
    serializer=JobExperienceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)
    return Response({"success": False, 'response': {'message': serializer.errors}},
			status=status.HTTP_400_BAD_REQUEST)

# add job project api
@api_view(['POST'])
def add_job_project_api(request):
    serializer=JobProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)
    return Response({"success": False, 'response': {'message': serializer.errors}},
			status=status.HTTP_400_BAD_REQUEST)


########################## DELETE API  ###############################

# delete company api
@api_view(['DELETE'])
def delete_company_api(request):
    id=request.query_params.get('id')
    company=Company.objects.get(id=id)
    company.is_deleted= True
    company.save()
    return Response('company deleted')

#delete job api
@api_view(['DELETE'])
def delete_job_api(request):
    id=request.query_params.get('id')
    job=Job.objects.get(id=id)
    job.is_deleted= True
    job.save()
    return Response('job deleted')

#delete education api
@api_view(['DELETE'])
def delete_education_api(request):
    id=request.query_params.get('id')
    education=Education.objects.get(id=id)
    education.is_deleted= True
    education.save()
    return Response('education deleted')

# delete currency api
@api_view(['DELETE'])
def delete_currency_api(request):
    id=request.query_params.get('id')
    currency=Currency.objects.get(id=id)
    currency.is_deleted= True
    currency.save()
    return Response('currency deleted')

#delete language api
@api_view(['DELETE'])
def delete_language_api(request):
    id=request.query_params.get('id')
    language=Language.objects.get(id=id)
    language.is_deleted= True
    language.save()
    return Response('language deleted')

# delete skill api
@api_view(['DELETE'])
def delete_skill_api(request):
    id=request.query_params.get('id')
    skill=Skill.objects.get(id=id)
    skill.is_deleted= True
    skill.save()
    return Response('skill deleted')

# delete industry api
@api_view(['DELETE'])
def delete_industry_api(request):
    id=request.query_params.get('id')
    industry=Industry.objects.get(id=id)
    industry.is_deleted= True
    industry.save()
    return Response('industry deleted')

# country api
@api_view(['DELETE'])
def delete_country_api(request):
    id=request.query_params.get('id')
    country=Country.objects.get(id=id)
    country.is_deleted= True
    country.save()
    return Response('country deleted')

# delete state api
@api_view(['DELETE'])
def delete_state_api(request):
    id=request.query_params.get('id')
    state=State.objects.get(id=id)
    state.is_deleted= True
    state.save()
    return Response('state deleted')

# delete city api
@api_view(['DELETE'])
def delete_city_api(request):
    id=request.query_params.get('id')
    city=City.objects.get(id=id)
    city.is_deleted= True
    city.save()
    return Response('city deleted')

@api_view(['DELETE'])
def delete_favourite_api(request):
    id=request.query_params.get('id')
    fav=FavouriteJob.objects.get(id=id)
    fav.delete()
    return Response('Job removed from favourite')

@api_view(['DELETE'])
def delete_job_experience_api(request):
    id=request.query_params.get('id')
    experience=Job_Experience.objects.get(id=id)
    experience.is_deleted=True
    experience.save()
    return Response('Job Experience Deleted Successfully')

@api_view(['DELETE'])
def delete_job_project_api(request):
    id=request.query_params.get('id')
    project=Job_Project.objects.get(id=id)
    project.is_deleted=True
    project.save()
    return Response('Job Project Deleted Successfully')

############################### UPDATE API ###############################

# update company api
@api_view(['PUT'])
def update_company_api(request):
    id=request.query_params.get('id')
    try:
        company=Company.objects.get(id=id)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        serializer=UpdateCompanySerializer(company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()    
            return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)
        return Response({"success": False, 'response': {'message': serializer.errors}},
			status=status.HTTP_400_BAD_REQUEST)

# update job api
@api_view(['PUT'])
def update_job_api(request):
    id=request.query_params.get('id')
    try:
        job=Job.objects.get(id=id)
    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        serializer=UpdateJobSerializer(job, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()    
            return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)
        return Response({"success": False, 'response': {'message': serializer.errors}},
			status=status.HTTP_400_BAD_REQUEST)

# update job experience api
@api_view(['PUT'])
def update_job_experience_api(request):
    id=request.query_params.get('id')
    try:
        experience=Job_Experience.objects.get(id=id)
    except Job_Experience.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        serializer=GetJobExperienceSerializer(experience, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()    
            return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)
        return Response({"success": False, 'response': {'message': serializer.errors}},
			status=status.HTTP_400_BAD_REQUEST)

# update job experience api
@api_view(['PUT'])
def update_job_project_api(request):
    id=request.query_params.get('id')
    try:
        project=Job_Project.objects.get(id=id)
    except Job_Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        serializer=GetJobProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()    
            return Response({"success": True, 'response': {'message': serializer.data}},status=status.HTTP_200_OK)
        return Response({"success": False, 'response': {'message': serializer.errors}},
			status=status.HTTP_400_BAD_REQUEST)


##############################  FILTERING IN API  ########################

@api_view(['GET'])
def search_job_api(request):
    title=request.query_params.get('title')
    if not title:
        title = ''
    minsalary=request.query_params.get('minsalary')
    maxsalary=request.query_params.get('maxsalary')
    country=request.query_params.get('country')
    if not country:
        country=''
    state=request.query_params.get('state')
    if not state:
        state=''
    city=request.query_params.get('city')
    if not city:
        city=''
    employeetype=request.query_params.get('employeetype')
    if not employeetype:
        employeetype=''
    skill=request.query_params.get('skill')
    if not skill:
        skill=''
    education=request.query_params.get('education')
    if not education:
        education=''
    if minsalary and not maxsalary:
            job=Job.objects.filter(Q(title__icontains=title)&
                        Q(minsalary__gte=minsalary)& 
                        Q(country__name__icontains=country)& 
                        Q(state__name__icontains=state)& 
                        Q(city__name__icontains=city)& 
                        Q(employeetype__icontains=employeetype)&
                        Q(skill__name__icontains=skill)&
                        Q(education__name__icontains=education)
                        )
        
    if maxsalary and not minsalary:
            job=Job.objects.filter(Q(title__icontains=title)&
                        Q(maxsalary__lte=maxsalary)& 
                        Q(country__name__icontains=country)& 
                        Q(state__name__icontains=state)& 
                        Q(city__name__icontains=city)& 
                        Q(employeetype__icontains=employeetype)&
                        Q(skill__name__icontains=skill)&
                        Q(education__name__icontains=education)
                        )
    if minsalary and maxsalary:
                    job=Job.objects.filter(Q(title__icontains=title)&
                        Q(minsalary__gte=minsalary)& 
                        Q(maxsalary__lte=maxsalary)& 
                        Q(country__name__icontains=country)& 
                        Q(state__name__icontains=state)& 
                        Q(city__name__icontains=city)& 
                        Q(employeetype__icontains=employeetype)&
                        Q(skill__name__icontains=skill)&
                        Q(education__name__icontains=education)
                        )
    if not minsalary and not maxsalary:
                    job=Job.objects.filter(Q(title__icontains=title)&
                        Q(country__name__icontains=country)& 
                        Q(state__name__icontains=state)& 
                        Q(city__name__icontains=city)& 
                        Q(employeetype__icontains=employeetype)&
                        Q(skill__name__icontains=skill)&
                        Q(education__name__icontains=education)
                        )

    serializer=GetJobSerializer(job, many=True)
    return Response(serializer.data)
################################ VIEWS  ####################################

def company(request):
    com=Company.objects.all()
    job=Job.objects.all()
    context={
        'com':com,
        'job':job
    }
    return render(request, 'company_info.html', context)


def add_company_info(request):
    form=Company_InfoForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            u=request.user
            n=form.cleaned_data['name']
            e=form.cleaned_data['email']
            m=form.cleaned_data['mobile']
            a=form.cleaned_data['address']
            com=Company.objects.create(user=u, name=n, email=e, mobile=m, address=a)
            return redirect('/company/company_info')
    return render(request, 'add_company.html', {'form':form})

def add_job_info(request, id):
    form=Job_InfoForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            u=request.user
            com=Company.objects.get(id=id)
            t=form.cleaned_data['title']
            e=form.cleaned_data['experience']
            min_s=form.cleaned_data['minsalary']
            max_s=form.cleaned_data['maxsalary']
            mobile=form.cleaned_data['mobile']
            language=form.cleaned_data['language']
            c=form.cleaned_data['country']
            s=form.cleaned_data['state']
            city=form.cleaned_data['city']
            ty=form.cleaned_data['type']
            currency=form.cleaned_data['currency']
            education=form.cleaned_data['education']
            employeetype=form.cleaned_data['employeetype']
            job=Job.objects.create(user=u, company=com, title=t, experience=e, minsalary=min_s, maxsalary=max_s,country=c, mobile=mobile,currency=currency,education=education,employeetype=employeetype ,state=s,city=city,type=ty)
            return redirect('/company_info')
    return render(request, 'add_job.html', {'form':form})
    

def delete_company(request, id):
    com=Company.objects.get(id=id)
    com.delete()
    return redirect('/company_info')

def delete_job(request, id):
    job=Job.objects.get(id=id)
    job.delete()
    return redirect('/company_info')

def update_company(request, id):
    com=Company.objects.get(id=id)
    form=Company_InfoUpdateForm(instance=com)
    if request.method=='POST':
        form=Company_InfoUpdateForm(request.POST or None, instance=com)
        if form.is_valid():
            com=form.save()
            return redirect('/company_info')

    return render(request, 'update_company.html',{'form':form})       

def update_job(request, id):
    job=Job.objects.get(id=id)
    form=Job_InfoUpdateForm(instance=job)
    if request.method=='POST':
        form=Job_InfoUpdateForm(request.POST or None, instance=job)
        if form.is_valid():
            com=form.save()
            return redirect('/company_info')

    return render(request, 'update_job.html',{'form':form})       

def apply(request, id):
    job=Job.objects.get(id=id)
    form=ApplyForm(request.POST, request.FILES)
    if request.method=='POST':
        if form.is_valid():
            u=request.user
            d=form.cleaned_data['documents']
            ex=form.cleaned_data['experience']
            e=form.cleaned_data['expected']
            apply=Apply.objects.create(job=job, user=u, documents=d, experience=ex, expected=e)
            return redirect('/company_info')

    return render(request, 'apply_form.html', {'form':form})

def apply_data(request, id):
    job=Job.objects.get(id=id)
    apply=job.apply_set.all()
    context={
        'apply':apply,
    }
    return render(request, 'all_applied_data.html', context)

def search_job(request):

    title=request.GET.get('title')
    country=request.GET.get('country')
    state=request.GET.get('state')
    city=request.GET.get('city')
    employeetype=request.GET.get('employeetype')
    job=Job.objects.filter(Q(title__icontains=title) & Q(country__name__icontains=country)& Q(state__name__icontains=state) & Q(city__name__icontains=city) & Q(employeetype__icontains=employeetype)) # &  Q & Q(employeetype__icontains=query5))
    # job=Job_info.objects.filter(state__name__icontains=query1)


    
    print(job)

    context={
        'job':job,

    }
    return render(request, 'search_job.html',context)

def search_company(request):
    query=request.GET.get('query')
    com=Company.objects.filter(name__icontains=query)
    context={
        'com':com
    }
    return render(request, 'search_company.html',context)
    
