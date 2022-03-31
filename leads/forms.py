from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

from leads.models import Lead, Agent

User = get_user_model()

class LeadModelForm(forms.ModelForm):
    # loggedIn_organisation = forms.formsets
    class Meta:
        model = Lead
        fields = (
            "first_name",
            "last_name",
            "age",
            'notes',
            "agent",
            # "loggedIn_organisation"
        )


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class CustomeUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {"username": UsernameField}

class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    #Pop out the request because django form 
    # isn't expecting it: all args coming from request e.g the user
    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        agents = Agent.objects.filter(organisation=request.user.userprofile)

        #for every time the form is rendered, 
        # this is to dynamically update the field based on the user logged in
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents