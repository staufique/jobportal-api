
from django.urls import path
from jobportal_api.views import *
urlpatterns = [
    path('register/',UserRegistrationView.as_view(), name='register'),
    path('login/',UserLoginView.as_view(), name='login'),
    path('profile/',UserProfileView.as_view(), name='profile'),
    path('changepswd/',UserChangePasswordView.as_view(), name='changepswd'),
    path('send-reset-pswd-email/',SendPasswordRequestEmailView.as_view(), name='SendPasswordRequestEmailView'),
    path('reset-pswd/<uid>/<token>/',UserPasswordResetView.as_view(), name='UserPasswordResetView'),
    path('personalinfo/',PersonalInfoView.as_view(), name='personal-info'),
    path('update-personalinfo/<int:pk>/',UpdatePersonalInfoView.as_view(), name='personal-info'),
    path('education/',EducationView.as_view(), name='personal-info'),
    path('update-eductaion/',UpdateEducationView.as_view(), name='personal-info'),
    path('experience/',ExperienceView.as_view(), name='personal-info'),
    path('update-experience/',UpdateExperienceView.as_view(), name='personal-info'),
    path('skills/',SkillsView.as_view(), name='personal-info'),
    path('update-skills/',UpdateSkillsView.as_view(), name='personal-info'),
]