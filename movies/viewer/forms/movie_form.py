from django.forms import (
    CharField,
    DateField,
    Form,
    IntegerField,
    ModelChoiceField,
    Textarea,
    ModelForm,
)

from viewer.models import Genre, Movie

# class MovieForm(Form):
#     title = CharField(max_length=128)
#     genre = ModelChoiceField(queryset=Genre.objects)
#     rating = IntegerField(min_value=1, max_value=10)
#     released = DateField()
#     description = CharField(widget=Textarea)


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
