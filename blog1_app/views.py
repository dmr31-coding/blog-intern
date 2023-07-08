from django.shortcuts import render, redirect
from blog1_app.models import Post

from blog1_app.forms import PostForm

from django.utils import timezone

from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, View

from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

# Create your views here.

# class-based views

class PostListView(ListView):
    model = Post
    template_name = "post1_list.html"
    context_object_name = "posts1"
    queryset = Post.objects.filter(published_at__isnull=False).order_by("-published_at")

# def post1_list(request):
#     posts1 = Post.objects.filter(published_at__isnull=False).order_by("-published_at")
#     return render(request, "post1_list.html", {"posts1": posts1})



class DraftListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "post1_list.html"
    context_object_name = "posts1"
    queryset = Post.objects.filter(published_at__isnull=True).order_by("-published_at")
    
    
# # @login_required
# # def draft1_list(request):
# #     posts1 = Post.objects.filter(published_at__isnull=True).order_by("-published_at")
# #     return render(request, "post1_list.html", {"posts1": posts1})

class PostDetailView(DetailView):
    model = Post
    template_name = "post1_detail.html"
    context_object_name = "post2"

# # def post1_detail(request, pk):
# #     # ORM : object Relationship Mapping => converts python code to SQL
# #     # post2 = Post.objects.get(pk=pk) yaslai comment gareko kinavane security ko lagi about 404
    
# #     post2 =get_object_or_404(Post, pk=pk)
# #     return render(
# #         request,
# #         "post1_detail.html",
# #         {"post2": post2},
# #     )


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post1-list")
    
    def form1_valid(self, form1):
        messages.success(self.request, "Post is Successfully deleted.")
        return super().form1_valid(form1)
    
    
# # @login_required
# # def post1_delete(request, pk):
# #     # post3 = Post.objects.get(pk=pk)
    
# #     post3 =get_object_or_404(Post, pk=pk)
# #     post3.delete()
# #     messages.success(request, "Post is successfully deleted")
# #     return redirect("post1-list")


# # def post1_create(request):
# #     if request.method == "POST":
# #         form1 = PostForm(request.Post)
# #         if form1.is_valid():
# #             postu = form1.save(commit=False)
# #             postu.author = request.user
# #             postu.save()
# #             return redirect("post1-list")
# #         else:
# #             return render(
# #                 request,
# #                 "post1_create.html",
# #                 {"furm": form1},
# #             )
# #     else:
# #         form1 = PostForm()
# #         return render(request, "post1_create.html", {"furm": form1})

# # mathi ko comment gareko ra yo talako method eutai ho just code line ghatauxa talako le same function


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "post1_create.html"
    success_url = reverse_lazy("draft1-list")
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post is Successfully created.")
        return super().form_valid(form)
    
    # def form1_valid(self, furm):
    #     messages.success(self.request, "Post is Successfully deleted.")
    #     return super().form1_valid(furm)

# # @login_required
# # def post1_create(request):
# #     form1 = PostForm()
# #     if request.method == "POST":
# #         form1 = PostForm(request.POST)
# #         if form1.is_valid():
# #             postu = form1.save(commit=False)
# #             postu.author = request.user
# #             postu.save()
# #             messages.success(request, "Post is successfully created")
# #         else:
# #             messages.error(request, "Post can not be created")
            
# #         return redirect("post1-list")
# #     return render(
# #         request,
# #         "post1_create.html",
# #         {"furm": form1},
# #     )

class PostPublishView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post4 =get_object_or_404(Post, pk=pk)
        post4.published_at = timezone.now()
        post4.save()
        messages.success(request, "Post is successfully published")
        
        return redirect("post1-list")
    

# # @login_required
# # def post1_publish(request, pk):
# #     # post4 = Post.objects.get(pk=pk)
    
# #     post4 =get_object_or_404(Post, pk=pk)
# #     post4.published_at = timezone.now()
# #     post4.save()
# #     messages.success(request, "Post is successfully published")
    
# #     return redirect("post1-list")


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "post1_create.html"
    success_url = reverse_lazy("post1-list")
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post is Successfully updated.")
        return super().form_valid(form)
    
        

# # @login_required
# # def post1_update(request, pk):
# #     # poost = Post.objects.get(pk=pk)
    
# #     poost =get_object_or_404(Post, pk=pk)
# #     formm = PostForm(instance=poost)
# #     if request.method == "POST":
# #         formm = PostForm(request.POST, instance=poost)
# #         if formm.is_valid():
# #             formm.save()
# #             messages.success(request, "Post is successfully updated")
            
# #         else:
# #             messages.success(request, "Post can not be updated")
            
# #         return redirect("post1-list")
            
           
# #     return render(
# #         request,
# #         "post1_create.html",
# #         {"furm": formm},
# #     )
    

def handler404(request, exception, template_name='404.html'):
    return render(request, template_name,status=404)



