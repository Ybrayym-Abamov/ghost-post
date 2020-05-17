from django import forms


RoastOrBoast = ((True, 'Boast'), (False, 'Roast'))


class GhostPost(forms.Form):
    boolean = forms.ChoiceField(choices=RoastOrBoast)
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Let the world know what's up"}))
