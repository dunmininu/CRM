from django.urls import reverse
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail

# from serializers import LeadCreateSerializer

from .models import Agent, Lead, User
from .forms import LeadModelForm, CustomeUserCreationForm
from agents.mixins import OrganiserAndLoginRequiredMixin


# Create your views here.

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomeUserCreationForm

    def get_success_url(self):
        return reverse('login')

class LandingPageView(TemplateView):
    template_name = "landing.html"

class LeadListView(LoginRequiredMixin, ListView):
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'
    
    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organiser:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            #filter for logged in agent
            queryset = queryset.filter(agent__user=user)
             
        return queryset

    def get_context_data(self, **kwargs):
        context= super(LeadListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organiser:
            queryset = Lead.objects.filter(organisation=user.userprofile)
            context.update({
                "unassigned_leads": 
            })
        return context

class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(OrganiserAndLoginRequiredMixin, CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')


    def form_valid(self, form):
        #TODO: send email
        send_mail(
            subject="a lead has been created",
            message="click to get link and send",
            from_email="djangomailtestmaster@gmail.com",
            recipient_list=["princekyle67@gmail.com"]
        )
        return super(LeadCreateView, self).form_valid(form)

class LeadUpdateView(OrganiserAndLoginRequiredMixin, UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        return Lead.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        return reverse('leads:lead-list')

class LeadDeleteView(OrganiserAndLoginRequiredMixin, DeleteView):
    template_name = 'leads/lead_delete.html'

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        return Lead.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        return reverse('leads:lead-list')