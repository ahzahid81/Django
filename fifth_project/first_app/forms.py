from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label='User Name:', required= True, initial= 'Abdul Hasib ', help_text= 'Enter your full name in English',
                           widget=forms.Textarea(attrs={'id' : 'text_area', 'placeholder' : 'Enter your name'}))
    file = forms.FileField()
    age = forms.CharField(widget=forms.NumberInput())
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    appointment = forms.DateTimeField(label='Appointment', widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices = CHOICES, widget=forms.RadioSelect)
    PizzaType = [('P', 'Pepperoni'), ('M', 'Mushroom'), ('B', 'Beff')]
    pizza = forms.MultipleChoiceField(choices=PizzaType, label='Pizza Type', widget=forms.CheckboxSelectMultiple)
    
    
    # email = forms.EmailField(label='User Email')
    # age = forms.IntegerField(label='Age')  
    # weight = forms.FloatField(label='Weight')
    # balance = forms.DecimalField(label = 'Balance')
    # birthDate = forms.DateField(label = 'Birth Date', required=False)
    # check = forms.BooleanField(label='All Provided Infromations are true')
    # appointment = forms.DateTimeField(label='Appointment')
    # CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    # size = forms.ChoiceField(choices = CHOICES)
    # PizzaType = [('P', 'Pepperoni'), ('M', 'Mushroom'), ('B', 'Beff')]
    # pizza = forms.MultipleChoiceField(choices=PizzaType, label='Pizza Type')
    
# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("Enter a name with at least 10 characters")
#     #     return valname
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
        
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("must added .com")

#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
        
#         if len(valname) < 10:
#                 raise forms.ValidationError("Enter a name with at least 10 characters")
        
#         if '.com' not in valemail:
#             raise forms.ValidationError("must added .com")

class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message='Enter a name at least 10 character')])
    email = forms.CharField(widget=forms.EmailInput)
    age = forms.CharField(widget= forms.NumberInput)
    
class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    Repassword = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_repass = self.cleaned_data['Repassword']
        
        if val_pass != val_repass:
            raise forms.ValidationError("Password doesn't match")
        