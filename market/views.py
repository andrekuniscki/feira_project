from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Sum, F, DecimalField, Count, Q
from django.utils import timezone
from datetime import timedelta
from .models import Item, Category, ShoppingHistory, UserProfile
from .forms import ItemForm

class HomeView(TemplateView):
    template_name = 'market/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            items = Item.objects.filter(owner=self.request.user)
            pending_items = items.filter(bought=False)
            bought_items = items.filter(bought=True)
            
            today = timezone.now().date()
            month_start = today.replace(day=1)
            month_items = items.filter(created_at__date__gte=month_start)
            
            total_pending = pending_items.count()
            total_bought = bought_items.count()
            total_price = month_items.aggregate(
                total=Sum(F('quantity') * F('price'), output_field=DecimalField())
            )['total'] or 0
            
            top_items = items.values('name').annotate(
                count=Count('id')
            ).order_by('-count')[:3]
            
            history = ShoppingHistory.objects.filter(owner=self.request.user)
            avg_spending = history.aggregate(avg=Sum('total_price'))['avg'] or 0
            if history.count() > 0:
                avg_spending = avg_spending / history.count()
            
            context.update({
                'total_pending': total_pending,
                'total_bought': total_bought,
                'total_price': total_price,
                'avg_spending': avg_spending,
                'top_items': top_items,
            })
        
        return context

class AboutView(TemplateView):
    template_name = 'market/about.html'

class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'market/item_list.html'
    paginate_by = None 

    def get_queryset(self):
        queryset = Item.objects.filter(owner=self.request.user).order_by('-created_at')
        
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        
        status = self.request.GET.get('status')
        if status == 'bought':
            queryset = queryset.filter(bought=True)
        elif status == 'pending':
            queryset = queryset.filter(bought=False)
        
        if self.request.GET.get('favorites'):
            queryset = queryset.filter(is_favorite=True)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['categories'] = Category.objects.all()
        
        all_items = Item.objects.filter(owner=self.request.user)
        context['pending_items'] = all_items.filter(bought=False).order_by('-created_at')
        context['bought_items'] = all_items.filter(bought=True).order_by('-created_at')
        
        total_pending = all_items.filter(bought=False).aggregate(
            total=Sum(F('quantity') * F('price'), output_field=DecimalField())
        )['total'] or 0
        total_bought = all_items.filter(bought=True).aggregate(
            total=Sum(F('quantity') * F('price'), output_field=DecimalField())
        )['total'] or 0
        total_all = total_pending + total_bought
        
        context['total_pending'] = total_pending
        context['total_bought'] = total_bought
        context['total_all'] = total_all
        
        context['pending_count'] = all_items.filter(bought=False).count()
        context['bought_count'] = all_items.filter(bought=True).count()
        
        context['selected_category'] = self.request.GET.get('category')
        context['selected_status'] = self.request.GET.get('status')
        
        return context

class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = 'market/item_detail.html'

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'market/item_form.html'
    success_url = reverse_lazy('market:item_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'market/item_form.html'
    success_url = reverse_lazy('market:item_list')