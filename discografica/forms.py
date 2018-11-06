from django import forms

from .models import Cancion, Vocalista, Genero, Artista, Album

class CancionForm(forms.ModelForm):
    #todos los campos de Cancion
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    num_pista = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    duracion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    fecha_creacion = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))

    class Meta:
        model = Cancion
        fields = ('titulo', 'Album', 'num_pista','duracion','fecha_creacion','Vocalista')

    def __init__ (self, *args, **kwargs):
        super(CancionForm, self).__init__(*args, **kwargs)
        #En este caso vamos a usar el widget checkbox multiseleccionable.
        self.fields["Vocalista"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["Vocalista"].help_text = "Ingrese los vocalistas que participaron en la Canción"
        self.fields["Vocalista"].queryset = Vocalista.objects.all()

class GeneroForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Genero
        fields = ('nombre',)

class ArtistaForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    fecha_inicio = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Artista
        fields = ('nombre', 'fecha_inicio',)

class AlbumForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    #Artista = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}))
    fecha_publicacion = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))
    duracion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Album
        fields = ('nombre',  'Artista','Genero', 'fecha_publicacion','duracion','portada',)

class VocalistaForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    fecha_nacimiento = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control'}))
    residencia = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Vocalista
        fields = ('nombre',  'apellido','fecha_nacimiento', 'residencia','email',)
