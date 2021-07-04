from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from adminapp.forms import ShopUserRegisterForm, ProductCategoryEditForm, ProductEditForm
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class UserListView(LoginRequiredMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    context_object_name = 'objects'


# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'админка/пользователи'
#
#     users_list = ShopUser.objects.filter(is_delete=False).order_by('-is_active', '-is_superuser',\
#     '-is_staff', 'username')
#
#     context = {
#         'title': title,
#         'objects': users_list
#     }
#
#     return render(request, 'adminapp/users.html', context=context)


class UserCreateView(LoginRequiredMixin, CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin_staff:users')


# @user_passes_test(lambda u: u.is_superuser)
# def user_create(request):
#     title = 'пользователи/создание'
#
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:users'))
#     else:
#         user_form = ShopUserRegisterForm()
#
#     context = {
#         'title': title,
#         'update_form': user_form,
#     }
#
#     return render(request, 'adminapp/user_update.html', context=context)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin_staff:users')


# @user_passes_test(lambda u: u.is_superuser)
# def user_update(request, pk):
#     title = 'пользователи/редактерирование'
#
#     edit_user = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         edit_form = ShopUserRegisterForm(request.POST, request.FILES, instance=edit_user)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:user_update', args=[edit_user.pk]))
#     else:
#         edit_form = ShopUserRegisterForm(instance=edit_user)
#
#     context = {
#         'edit_user': edit_user,
#         'title': title,
#         'update_form': edit_form,
#     }
#
#     return render(request, 'adminapp/user_update.html', context=context)


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('admin_staff:users')
    context_object_name = 'user_to_delete'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_delete = True
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def user_delete(request, pk):
#     title = 'пользователи/удаление'
#
#     user = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         user.is_delete = True
#         user.save()
#         return HttpResponseRedirect(reverse('admin_staff:users'))
#
#     context = {
#         'title': title,
#         'user_to_delete': user,
#     }
#
#     return render(request, 'adminapp/user_delete.html', context=context)


class ProductCategoryListView(LoginRequiredMixin, ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'
    context_object_name = 'objects'


# @user_passes_test(lambda u: u.is_superuser)
# def categories(request):
#     title = 'админка/категории'
#
#     categories_list = ProductCategory.objects.all()
#
#     content = {
#         'title': title,
#         'objects': categories_list
#     }
#
#     return render(request, 'adminapp/categories.html', content)


class ProductCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ProductCategory
    form_class = ProductCategoryEditForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_staff:categories')


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = 'Категории/создание'

    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin_staff:categories'))
    else:
        category_form = ProductCategoryEditForm()

    context = {
        'title': title,
        'update_form': category_form,
    }

    return render(request, 'adminapp/category_update.html', context=context)


class ProductCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductCategory
    form_class = ProductCategoryEditForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_staff:categories')


# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#     title = 'пользователи/редактерирование'
#
#     edit_category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:category_update', args=[edit_category.pk]))
#     else:
#         edit_form = ProductCategoryEditForm(instance=edit_category)
#
#     context = {
#         'title': title,
#         'update_form': edit_form,
#     }
#
#     return render(request, 'adminapp/category_update.html', context=context)


class ProductCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin_staff:categories')
    context_object_name = 'category_to_delete'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_delete = True
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#     title = 'категория/удаление'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         category.is_delete = True
#         category.save()
#         return HttpResponseRedirect(reverse('admin_staff:categories'))
#
#     context = {
#         'title': title,
#         'category_to_delete': category,
#     }
#
#     return render(request, 'adminapp/category_delete.html', context=context)


class ProductsListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'adminapp/products.html'
    context_object_name = 'objects'

    def get_queryset(self):
        return Product.objects.filter(category__pk=self.kwargs.get('pk'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)

        category = get_object_or_404(ProductCategory, pk=self.kwargs.get('pk'))

        context.update({'category': category})

        return context

# @user_passes_test(lambda u: u.is_superuser)
# def products(request, pk):
#     title = 'админка/продукт'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#     products_list = Product.objects.filter(category__pk=pk).order_by('name')
#
#     context = {
#         'title': title,
#         'category': category,
#         'objects': products_list,
#     }
#
#     return render(request, 'adminapp/products.html', context=context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'adminapp/product_update.html'

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse_lazy('admin_staff:products', args=[pk])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)

        category = get_object_or_404(ProductCategory, pk=self.kwargs.get('pk'))

        context.update({'category': category})

        return context

    def get_initial(self):
        return {'category': get_object_or_404(ProductCategory, pk=self.kwargs.get('pk'))}


# def product_create(request, pk):
#     title = 'продукт/создание'
#     category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         product_form = ProductEditForm(request.POST, request.FILES)
#         if product_form.is_valid():
#             product_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:products', args=[pk]))
#     else:
#         product_form = ProductEditForm(initial={'category': category})
#
#     context = {'title': title,
#                'update_form': product_form,
#                'category': category
#                }
#
#     return render(request, 'adminapp/product_update.html', context=context)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'


# def product_read(request, pk):
#     title = 'продукт/подробнее'
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'title': title,
#         'object': product,
#     }
#
#     return render(request, 'adminapp/product_read.html', context=context)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'adminapp/product_update.html'

    # не совсем понимаю как эта функция работает - но оно работает, а без нее нет =)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        category = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        context.update({'category': category})

        return context

    def get_success_url(self):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))

        return reverse_lazy('admin_staff:products', args=[product.category.pk])


# @user_passes_test(lambda u: u.is_superuser)
# def product_update(request, pk):
#     title = 'продукт/редактирование'
#
#     edit_product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:product_update', args=[edit_product.pk]))
#     else:
#         edit_form = ProductEditForm(instance=edit_product)
#
#     context = {
#         'title': title,
#         'form': edit_form,
#         'category': edit_product.category,
#     }
#
#     return render(request, 'adminapp/product_update.html', context=context)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    context_object_name = 'product_to_delete'

    def get_success_url(self):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        return reverse_lazy('admin_staff:products', args=[product.category.pk])

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_delete = True
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request, pk):
#     title = 'продукт/удаление'
#
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         product.is_delete = True
#         product.save()
#         return HttpResponseRedirect(reverse('admin_staff:products', args=[product.category.pk]))
#
#     context = {
#         'title': title,
#         'product_to_delete': product,
#     }
#
#     return render(request, 'adminapp/product_delete.html', context=context)
