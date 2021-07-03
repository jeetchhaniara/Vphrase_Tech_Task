from django.forms import ModelForm
from phone.models import PhoneModel

class PhoneForm(ModelForm):
    # phone_name = forms.CharField(label='Phone name', max_length=100)
    # phone_brand = forms.CharField(label='Phone brand', max_length=100)
    # phone_storage = forms.IntegerField(label='Phone Storage')
    # phone_ram = forms.IntegerField(label='Phone RAM')
    # phone_stock = forms.IntegerField(label='Phone stock')
    # phone_price = forms.IntegerField(label='Phone price')
    class Meta: 
        model = PhoneModel
        fields = ['name', 'brand', 'ram', 'storage', 'stock', 'price']