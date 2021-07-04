from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='registration/password_change-form.html'), name='password_change' ),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password-change-done.html'),  name='password_change_done' ),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password_reset' ),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password-reset-done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password-reset-confirm.html"), name='password_reset_confirm' ),
    path('reset/done/', auth_views. PasswordResetCompleteView.as_view(template_name="registration/password-reset-complete.html"), name='password_reset_complete')


]
