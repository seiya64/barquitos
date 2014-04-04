# coding: utf-8
from django import forms
from crispy_forms.bootstrap import FormActions
from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, ButtonHolder, Submit, Button, Field

from servidor.models import Partida

class NuevaPartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        exclude = ['usuario','tablero1','tablero2','tablero1_ataque','tablero2_ataque','ultima_jugada1','ultima_jugada2','turno']
        
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_action = 'javascript:enviarpeticion(document.forms[0])'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                'Oponente',
                'oponente'
            ),
            FormActions(
                Submit('submit', 'Enviar Reto', css_class='btn btn-primary'),
            )
        )
        super(NuevaPartidaForm, self).__init__(*args, **kwargs)


login_helper = FormHelper()
login_helper.form_class = 'form-horizontal'
login_helper.layout = Layout(
    Fieldset(
        u'¿Quién eres?',
        "username",
        "password"
    ),
    FormActions(
        Submit('submit', 'Entrar', css_class='btn btn-primary')
    ),
)
