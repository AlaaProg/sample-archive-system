from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from category.models import Category
# Create your views here.

@login_required
@permission_required(['category.delete_category'])
def delete_category(request, id: int):
    """Delete Category"""
    
    obj = get_object_or_404(Category, pk=id)
    obj.delete()
    messages.success(request, "Successfuly delete category %s"%id)
    return redirect(reverse_lazy('category'))

class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Display all Category"""
    model = Category
    paginate_by = 10
    context_object_name = 'categories'
    template_name = "category.html"
    permission_required = ['category.view_category']

    def get_queryset(self):
        filter_name = self.request.GET.get('name', '')
        return Category.objects.order_by('id').filter(name__contains=filter_name)

class CreateCategoryView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Create Category View"""
    model = Category
    template_name = "forms/category.html"
    fields = "__all__"
    success_url = reverse_lazy('category')
    permission_required = ['category.create_category']

class UpdateCategoryView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Create Category View"""
    model = Category
    template_name = "forms/category.html"
    fields = "__all__"
    success_url = reverse_lazy('category')
    permission_required = ['category.change_category']
