from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='User Name:', required= True, initial= 'Abdul Hasib ', help_text= 'Enter your full name in English')
    file = forms.FileField()
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
    