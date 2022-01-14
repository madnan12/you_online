from django.urls import path
from company_info import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ########### FETCING API URL #################
    path('', views.get_jobs_api),
    path('get_single_job_api/<int:id>', views.get_single_job_api),
    path('get_favourite_api', views.get_favourite_api),
    path('get_job_experience_api', views.get_job_experience_api),
    path('get_job_project_api', views.get_job_project_api),
    path('get_job_profile_api', views.get_job_profile_api),
    path('get_job_endoresements_api', views.get_job_endoresements_api),
    path('get_blog_api', views.get_blog_api),
    path('get_apply_api', views.get_apply_api),
    path('search_blog_api', views.search_blog_api),
    path('login_api/', views.login_api),
    path('logout_api', views.logout_api),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ########### CREATE API URL####################
    path('add_company',views.add_company ),
    path('add_job',views.add_job ),
    path('add_education',views.add_education ),
    path('add_country',views.add_country ),
    path('add_state',views.add_state ),
    path('add_city',views.add_city ),
    path('add_currency',views.add_currency ),
    path('add_language',views.add_language ),
    path('add_industry',views.add_industry ),
    path('add_skill',views.add_skill ),
    path('add_apply_api',views.add_apply_api ),
    path('add_favourite_api',views.add_favourite_api ),
    path('add_job_experience_api',views.add_job_experience_api ),
    path('add_job_project_api',views.add_job_project_api ),
    path('add_job_profile_api',views.add_job_profile_api ),
    path('add_job_endoresements_api',views.add_job_endoresements_api ),
    path('add_blog_api',views.add_blog_api ),
    path('add_admin_jobs_api',views.add_admin_jobs_api ),
    path('add_admin_blogs_api',views.add_admin_blogs_api ),

    ##################### DELETE API URL #####################
    path('delete_company_api',views.delete_company_api ),
    path('delete_job_api',views.delete_job_api ),
    path('delete_skill_api',views.delete_skill_api ),
    path('delete_education_api',views.delete_education_api ),
    path('delete_language_api',views.delete_language_api ),
    path('delete_country_api',views.delete_country_api ),
    path('delete_state_api',views.delete_state_api ),
    path('delete_city_api',views.delete_city_api ),
    path('delete_industry_api',views.delete_industry_api ),
    path('delete_favourite_api',views.delete_favourite_api ),
    path('delete_job_experience_api',views.delete_job_experience_api ),
    path('delete_job_project_api',views.delete_job_project_api ),
    path('delete_blog_api',views.delete_blog_api ),

    ##################### UPDATE API URL #######################
    path('update_company_api', views.update_company_api),
    path('update_job_api', views.update_job_api),
    path('search_job_api/', views.search_job_api),
    path('update_job_experience_api', views.update_job_experience_api),
    path('update_job_project_api', views.update_job_project_api),
    path('update_job_profile_api', views.update_job_profile_api),
    path('update_blog_api', views.update_blog_api),
    
    ######################## VIEWS URL #########################
    path('company_info', views.company, name='company_info'),
    path('search', views.search_job, name='search'),
    path('search_company', views.search_company, name='search_company'),
    path('add_company_info', views.add_company_info, name="add_company"),
    path('add_job_info/<int:id>', views.add_job_info, name="add_job"),
    path('update_job/<int:id>', views.update_job, name="update_job"),
    path('update_comapny/<int:id>', views.update_company, name="update_company"),
    path('delet_job/<int:id>', views.delete_job, name="delete_job"),
    path('delete_comapny/<int:id>', views.delete_company, name="delete_company"),
    path('apply/<int:id>', views.apply, name="apply"),
    path('all_applied/<int:id>', views.apply_data, name="all_applied"),
    ####################### Toke ##############################
]
