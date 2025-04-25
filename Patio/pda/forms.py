from django import forms
from .models import Patio,Trabajador, Paquete,AlbaranDevolucion,LineaArticulo,Trabajador,Articulo,TipoTarea

class TrabajadorForm(forms.ModelForm):
    nombre=forms.CharField(label='Trabajador')
    class Meta:
        model=Trabajador
        fields=['nombre']



class PatioForm(forms.ModelForm):
    idOper1 = forms.IntegerField(required=True, min_value=0, label='Trab.1')
    idTipTarea = forms.IntegerField(required=True, min_value=0, label='Tip.Tarea')
    idOper2 = forms.IntegerField(required=False, min_value=0, label='Trab.2')

    class Meta:
        model = Patio
        fields = ['idTipTarea', 'idOper1', 'idOper2'] 

    def clean(self):
        cleaned_data = super().clean()
        oper1 = cleaned_data.get('idOper1')
        oper2 = cleaned_data.get('idOper2')
        tip_tarea = cleaned_data.get('idTipTarea')

        if oper1 and oper2 and oper1 == oper2:
            raise forms.ValidationError("El trabajador y el trabajador 2 no pueden ser el mismo")

        if not Trabajador.objects.filter(id=oper1).exists():
            raise forms.ValidationError('El ID del trabajador 1 no es valido')
        
        if oper2 and not Trabajador.objects.filter(id=oper2).exists():
            raise forms.ValidationError('El ID del trabajador 2 no es valido')
        
        if not TipoTarea.objects.filter(id=tip_tarea).exists():
            raise forms.ValidationError('El ID del tipo de tarea no es valido')
        return cleaned_data

class PaqueteForm(forms.ModelForm):
    codBarrasPaquete = forms.IntegerField(required=True,min_value=0,label='Cod.Barras.Paquete')
    idTipArticulo = forms.IntegerField(required=True,min_value=0,label='Tip.Articulo')
    cantidad_paquete = forms.IntegerField(min_value=0,label='Cantidad.Paquete')
    class Meta:
        model = Paquete
        fields = ['codBarrasPaquete','idTipArticulo', 'cantidad_paquete']
    
    def clean(self):
        cleaned_data = super().clean()
        idTipArticulo=cleaned_data.get('idTipArticulo')
        if not Articulo.objects.filter(id=idTipArticulo).exists():
            raise forms.ValidationError('El ID del articulo no es valido')
        
        return cleaned_data

class AlbaranForm(forms.ModelForm):
    numero=forms.IntegerField(required=True,min_value=0,label='Num.Albaran')
    class Meta:
        model=AlbaranDevolucion
        fields=['numero']


class LineaArticuloForm(forms.ModelForm):
    idArticulo = forms.IntegerField(required=True,label='Id.Articulo')
    cantidad_buena=forms.IntegerField(min_value=0)
    cantidad_mala=forms.IntegerField(min_value=0)
    chatarra=forms.IntegerField(min_value=0)

    def clean(self):
        cleaned_data=super().clean()
        idArticulo=cleaned_data.get('idArticulo')
        if not Articulo.objects.filter(id=idArticulo).exists():
            raise forms.ValidationError('El Id del articulo es invalido')
        return cleaned_data
    
    class Meta:
        model = LineaArticulo
        fields = ['idArticulo', 'cantidad_buena', 'cantidad_mala','chatarra']

        


