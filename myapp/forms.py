from django import forms

class createNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200 )
    decripcion = forms.CharField(label="Descripcion de la tarea", 
    widget=forms.Textarea)