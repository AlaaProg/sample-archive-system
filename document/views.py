from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from document.models import Document
from category.models import Category
# Create your views here.
# Create your views here.

@login_required
def home(request):
    """Home Page"""
    return render(request, "home.html")

@login_required
@permission_required(['document.delete_document'])
def delete_document(request, pk: int):
    """Delete document By Id"""
    
    obj = get_object_or_404(Document, pk=pk)
    obj.delete()
    messages.success(request, "Successfuly delete document %s"%pk)
    return redirect(reverse_lazy('document'))


class DocumentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):

    model = Document
    paginate_by = 10
    context_object_name = 'documents'
    template_name = "document.html"
    permission_required = ['document.view_document']

    def get_queryset(self):
        title = self.request.GET.get('title', '')
        str_date = self.request.GET.get('date')
        category = self.request.GET.get('category')
        
        # Order document by id field
        filter_obj = Document.objects.order_by('id')

        # filter by title 
        filter_obj = filter_obj.filter(title__contains=title)

        if str_date:
            _date = datetime.strptime(str_date, '%Y-%m-%d')

            # filter by date 
            filter_obj = filter_obj.filter(date__year=_date.year, date__month=_date.month)
            
        # filter by  category name
        if category :
            filter_obj = filter_obj.filter(category__name=category) 

        return filter_obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context[self.context_object_name] = self.get_queryset()
        context['categories'] = categories  # set categories to template 
        return context


class CreateDocumentView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Create Category View"""
    model = Document
    template_name = "forms/document.html"
    fields = ['title', "file", "note", "date", "category"]
    success_url = reverse_lazy('document')
    permission_required = ['document.add_document']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateDocumentView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Create Category View"""
    model = Document
    template_name = "forms/document.html"
    fields = ['title', "file", "note", "date", "category"]
    success_url = reverse_lazy('document')
    permission_required = ['document.change_document']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
