
from django.urls import path
from category.views import CategoryListView, delete_category, UpdateCategoryView,  CreateCategoryView
urlpatterns = [
    
    path("", CategoryListView.as_view(), name="category"),
    path("create", CreateCategoryView.as_view(), name="create_category"),
    path("update/<pk>", UpdateCategoryView.as_view(), name="update_category"),
    path("delete/<id>/", delete_category, name="delete_category"),
]
