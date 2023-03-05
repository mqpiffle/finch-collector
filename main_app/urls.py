from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('finches/<int:finch_id>/assoc_bug/<int:bug_id>/', views.assoc_bug, name="assoc_bug"),
    path('finches/<int:finch_id>/unassoc_bug/<int:bug_id>/', views.unassoc_bug, name="unassoc_bug"),

    # BUGS routes
    path('bugs/', views.BugList.as_view(), name='bugs_index'),
    path('bugs/create/', views.BugCreate.as_view(), name='bugs_create'),
    path('bugs/<int:pk>/update/', views.BugUpdate.as_view(), name='bugs_update'),
    path('bugs/<int:pk>/delete/', views.BugDelete.as_view(), name='bugs_delete'),
    path('bugs/<int:pk>/', views.BugDetail.as_view(), name='bugs_detail'),
]