from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from bookshelf.models import Review, User

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ('author',)
        widgets = {
            'body': forms.Textarea()
        }