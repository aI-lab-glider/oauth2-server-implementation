from django.urls import path
import identity_server.views as views

urlpatterns = [
    path('is_authenticated', views.is_authenticated),
    # GET
    path('login', views.login),
    # POST
    path('token', views.create_token),
    # POST
    path('revoke', views.revoke_token),
    # POST
    path('introspect', views.introspect_token),
    # GET
    path('contacts/<int:user_id>', views.get_contacts),
    # GET
    path('users/<int:user_id>', views.get_user),
    # GET
    path('users', views.get_users),
    # POST
    path('create_user', views.create_user),
    # GET
    path('worker_shifts/<int:user_id>', views.get_workers_shift),
    # POST
    path('create_worker_shift/<int:user_id>', views.create_shift),
]
