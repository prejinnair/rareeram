
from django.forms import ModelForm
from django import forms
from manageorders.models import Orders

class OrderForm(ModelForm):
    class Meta:
        model=Orders
        fields=['order_name',"order_status","order_total","order_tracking_no","order_shipping_provider"]
        labels = {}


        widgets={

            'order_name':forms.TextInput(attrs={'class': 'form-control',
                                                    'aria-expanded': "false",
                                                    'tabindex': "0",
                                                    'aria-haspopup': "true",
                                                    'role': "combobox",
                                                    'data-plugin': "customselect"
                                                    }),
         
            'order_status':forms.Select(attrs={'class': 'form-control',
                                                    'aria-expanded': "false",
                                                    'tabindex': "0",
                                                    'aria-haspopup': "true",
                                                    'role': "combobox",
                                                    'data-plugin': "customselect"
                                                    }),
            'order_total':forms.TextInput(attrs={'class': 'form-control',
                                                    'aria-expanded': "false",
                                                    'tabindex': "0",
                                                    'aria-haspopup': "true",
                                                    'role': "combobox",
                                                    'data-plugin': "customselect"
                                                    }),
            'order_tracking_no':forms.TextInput(attrs={'class': 'form-control',
                                                    'aria-expanded': "false",
                                                    'tabindex': "0",
                                                    'aria-haspopup': "true",
                                                    'role': "combobox",
                                                    'data-plugin': "customselect"
                                                    }),
            'order_shipping_provider':forms.TextInput(attrs={'class': 'form-control',
                                                    'aria-expanded': "false",
                                                    'tabindex': "0",
                                                    'aria-haspopup': "true",
                                                    'role': "combobox",
                                                    'data-plugin': "customselect"
                                                    }),
            
          

                                           },