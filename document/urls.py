
from django.urls import path
from document.views import home, delete_document, DocumentListView, UpdateDocumentView, CreateDocumentView

urlpatterns = [
    
    path("", home, name="home_page"),
    path("document/", DocumentListView.as_view(), name="document"),
    path("create/", CreateDocumentView.as_view(), name="create_document"),
    path("update/<pk>/", UpdateDocumentView.as_view(), name="update_document"),
    path("delete/<pk>/", delete_document, name="delete_document"),
]
