from django import forms
from .models import Visitor
from django.core.exceptions import ValidationError

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ('name', 'number', 'number2',)
        widgets = {'name': forms.TextInput(
                        attrs={
                            'placeholder': '홍길동',
                    }),
                    'number': forms.NumberInput(
                        attrs={
                            'placeholder': '01012345678',
                        }),
                    'number2': forms.NumberInput(
                        attrs={
                            'placeholder': '01012345678',
                        }),
        }
        labels = {
            'name': '이름',
            'number': '전화번호',
            'number2': '전화번호 확인',
        }
    
    def clean(self):
        number = self.cleaned_data.get('number')
        number2 = self.cleaned_data.get('number2')
        
        if number != number2:
            msg = '전화번호를 다시 확인해주세요'
            raise ValidationError(msg)
        
    
