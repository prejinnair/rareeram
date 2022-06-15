from django.forms import ModelForm
from django import forms
from .models import Products

class ProductForm(ModelForm):
    class Meta:
        model=Products
        fields=['product_name','product_descriptions','product_image','category_id']
        labels = {
            "category_id": "Category name"
        
        }
        widgets = {

            'product_name': forms.TextInput(attrs={'class': 'form-control',
                                                     'aria-expanded': "false",
                                                     'tabindex': "0",
                                                     'aria-haspopup': "true",
                                                     'role': "combobox",
                                                     'data-plugin': "customselect",
                                                     
                                                     }),
            'product_descriptions': forms.TextInput(attrs={'class': 'form-control',
                                                     'aria-expanded': "false",
                                                     'tabindex': "0",
                                                     'aria-haspopup': "true",
                                                     'role': "combobox",
                                                     'data-plugin': "customselect",
                                                     
                                                     }),
            # 'product_attributes':forms.TextInput(attrs={'class': 'form-control',
            #                                          'aria-expanded': "false",
            #                                          'tabindex': "0",
            #                                          'aria-haspopup': "true",
            #                                          'role': "combobox",
            #                                          'data-plugin': "customselect",
                                                     
            #                                          }),
            # 'product_image': forms.FileInput(attrs={'class': 'form-control',
            #                                 'aria-expanded': "false",
            #                                 'tabindex': "0",
            #                                 'aria-haspopup': "true",
            #                                 'role': "combobox",
            #                                 'data-plugin': "customselect",
                                           
            #                                 }),
            'category_id':forms.Select(attrs={'class': 'form-control',
                                                 'aria-expanded': "false",
                                                 'tabindex': "0",
                                                 'aria-haspopup': "true",
                                                 'role': "combobox",
                                                 'data-plugin': "customselect"
                                                 }),
            
            
        }



            