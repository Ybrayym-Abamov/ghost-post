from django import forms


RoastOrBoast = ((True, 'Boast'), (False, 'Roast'))


class GhostPost(forms.Form):
    boolean = forms.ChoiceField(choices=RoastOrBoast)
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Let the world know what's up"}))


# https://www.geeksforgeeks.org/choicefield-django-forms/
# http://www.learningaboutelectronics.com/Articles/How-to-add-a-placeholder-to-a-Django-form-field.php
