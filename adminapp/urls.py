from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.projecthomepage,name='projecthomepage'),
    path('printpagecall/',views.printpagecall,name='printpagecall'),
    path('printpagelogic/',views.printpagelogic,name='printpagelogic'),
    path('exceptionpagecall/',views.exceptionpagecall,name='exceptionpagecall'),
    path('exceptionpagelogic/',views.exceptionpagelogic,name='exceptionpagelogic'),
    path('randompagecall/',views.randompagecall,name='randompagecall'),
    path('randomlogic/',views.randomlogic,name='randomlogic'),
    path('calculatorlogic/',views.calculatorlogic,name='calculatorlogic'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),

    # path('login_view/',views.login_view,name='login_view'),
    # path('register_view/',views.register_view,name='register_view'),
    # path('log_out_view/', views.log_out_view, name='log_out_view'),

    path('UserRegisterLogic',views.UserRegisterLogic, name='UserRegisterLogic'),
    path('UserRegisterPageCall',views.UserRegisterLogic,name='UserRegisterPageCall'),
    path('UserLoginPageCall',views.UserLoginPageCall,name='UserLoginPageCall'),
    path('UserLoginLogic',views.UserLoginLogic,name='UserLoginLogic'),
    path('logout',views.logout,name='logout'),

    path('datetime_view/',views.datetime_view,name='datetime_view'),

    path('add_student/',views.add_student,name='add_student'),
    path('student_list/',views.student_list,name='student_list'),
    path('upload_file/',views.upload_file,name='upload_file'),

    path('feedback/', views.submit_feedback, name='submit_feedback'),
    path('feedback/success/', views.feedback_success, name='feedback_success'),  # Define this view for success page
    path('contact_list/', views.contact_list, name='contact_list'),
    path('add/', views.contact_add, name='contact_add'),
    path('delete/<int:pk>/', views.contact_delete, name='contact_delete'),

]
