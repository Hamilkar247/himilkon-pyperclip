from api.models import Organizacja
from django import forms
import datetime
from api.models import Organizacja, Pomiar

#class OrganizacjaForm(forms.ModelForm):


#class PomiarForm(forms.ModelForm):
#     #change the widget of the data field
#     dob = forms.DateField(
#         label='Jaka jest data pomiaru?',
#         widget=forms.SelectDataWidget() #dałem bez parametru - co się stanie?
#     )
#
#     def __init__(self, *args, **kwargs):
#         super(PomiarForm. self).__init__(*args,**kwargs)
#         ##
#         ##
#         for name in self.fields.keys():
#             self.fields[name].widget.attrs.update({
#                 'class': 'form-control', })
#
#     class Meta:
#         model = Pomiar
#         fields = ("__all__")