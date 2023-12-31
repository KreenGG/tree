from django.views.generic import ListView
from .models import Post, Category


class CategoryListView(ListView):
    model = Category
    template_name = "tree/category_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.tree.order_by("title")
        return context


class PostByCategoryView(ListView):
    context_object_name = "posts"
    template_name = "tree/post_list.html"

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs["slug"])
        queryset = Post.objects.filter(category=self.category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.category
        return context
