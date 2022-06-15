# # from re import A
# from django.forms import ModelForm
# from django import forms
# from .models import Dealers,Address


# class DealerForm(ModelForm):
#     class Meta:
#         model=Dealers
#         fields=['reg_dealer_id','dealer_first_name','dealer_last_name',"dealer_mobile_number","dealer_gender","dealer_status"]
#         labels = {}


#         widgets={

#             'reg_dealer_id': forms.TextInput(attrs={'class': 'form-control',
#                                                     'aria-expanded': "false",
#                                                     'tabindex': "0",
#                                                     'aria-haspopup': "true",
#                                                     'role': "combobox",
#                                                     'data-plugin': "customselect"
#                                                     }),

#             'dealer_first_name':forms.TextInput(attrs={'class': 'form-control',
#                                                     'aria-expanded': "false",
#                                                     'tabindex': "0",
#                                                     'aria-haspopup': "true",
#                                                     'role': "combobox",
#                                                     'data-plugin': "customselect"
#                                                     }),
#             'dealer_last_name':forms.TextInput(attrs={'class': 'form-control',
#                                                     'aria-expanded': "false",
#                                                     'tabindex': "0",
#                                                     'aria-haspopup': "true",
#                                                     'role': "combobox",
#                                                     'data-plugin': "customselect"
#                                                     }),
#             'caretaker_email':forms.TextInput(attrs={'class': 'form-control',
#                                                     'aria-expanded': "false",
#                                                     'tabindex': "0",
#                                                     'aria-haspopup': "true",
#                                                     'role': "combobox",
#                                                     'data-plugin': "customselect"
#                                                     }),
            
#             'dealer_gender':forms.Select(attrs={'class': 'form-control',
#                                                     'aria-expanded': "false",
#                                                     'tabindex': "0",
#                                                     'aria-haspopup': "true",
#                                                     'role': "combobox",
#                                                     'data-plugin': "customselect"
#                                                     }),
#             'dealer_mobile_number':forms.TextInput(attrs={'class': 'form-control',
#                                                     'aria-expanded': "false",
#                                                     'tabindex': "0",
#                                                     'aria-haspopup': "true",
#                                                     'role': "combobox",
#                                                     'data-plugin': "customselect"
#                                                     }),
#             'dealer_status':forms.Select(attrs={'class': 'form-control',
#                                                     'aria-expanded': "false",
#                                                     'tabindex': "0",
#                                                     'aria-haspopup': "true",
#                                                     'role': "combobox",
#                                                     'data-plugin': "customselect"
#                                                     }),

#         }

# class AddressForm(ModelForm):
#     class Meta:
#         model=Address
#         fields=['address_id','city','area',"country","postalcode"]
#         labels = {}


#         widgets={

#             'address_id': forms.TextInput(attrs={'class': 'form-control',
#                                                     'aria-expanded': "false",
#                                                     'tabindex': "0",
#                                                     'aria-haspopup': "true",
#                                                     'role': "combobox",
#                                                     'data-plugin': "customselect"
#                                                     }),

#             'city':forms.TextInput(attrs={'class': 'form-control',
#                                                     'aria-expanded': "false",
#                                                     'tabindex': "0",
#                                                     'aria-haspopup': "true",
#                                                     'role': "combobox",
#                                                     'data-plugin': "customselect"
#                                                     }),
#             'area':forms.TextInput(attrs={'class': 'form-control',
#                                                     'aria-expanded': "false",
#                                                     'tabindex': "0",
#                                                     'aria-haspopup': "true",
#                                                     'role': "combobox",
#                                                     'data-plugin': "customselect"
#                                                     }),
#             'country':forms.TextInput(attrs={'class': 'form-control',
#                                                     'aria-expanded': "false",
#                                                     'tabindex': "0",
#                                                     'aria-haspopup': "true",
#                                                     'role': "combobox",
#                                                     'data-plugin': "customselect"
#                                                     }),

#             'postalcode':forms.TextInput(attrs={'class': 'form-control',
#                                                     'aria-expanded': "false",
#                                                     'tabindex': "0",
#                                                     'aria-haspopup': "true",
#                                                     'role': "combobox",
#                                                     'data-plugin': "customselect"
#                                                     }),

#         }


# # class SaleAgentForm(ModelForm):
# #     class Meta:
# #         model=SalesAgent
# #         fields=['reg_salesagent_id','salesagent_first_name','salesagent_last_name',"salesagent_mobile_number","salesagent_gender","salesagent_status"]
# #         labels = {}


# #         widgets={

# #             'reg_salesagent_id': forms.TextInput(attrs={'class': 'form-control',
# #                                                     'aria-expanded': "false",
# #                                                     'tabindex': "0",
# #                                                     'aria-haspopup': "true",
# #                                                     'role': "combobox",
# #                                                     'data-plugin': "customselect"
# #                                                     }),

# #             'salesagent_first_name':forms.TextInput(attrs={'class': 'form-control',
# #                                                     'aria-expanded': "false",
# #                                                     'tabindex': "0",
# #                                                     'aria-haspopup': "true",
# #                                                     'role': "combobox",
# #                                                     'data-plugin': "customselect"
# #                                                     }),
# #             'salesagent_last_name':forms.TextInput(attrs={'class': 'form-control',
# #                                                     'aria-expanded': "false",
# #                                                     'tabindex': "0",
# #                                                     'aria-haspopup': "true",
# #                                                     'role': "combobox",
# #                                                     'data-plugin': "customselect"
# #                                                     }),
# #             'salesagent_mobile_number':forms.TextInput(attrs={'class': 'form-control',
# #                                                     'aria-expanded': "false",
# #                                                     'tabindex': "0",
# #                                                     'aria-haspopup': "true",
# #                                                     'role': "combobox",
# #                                                     'data-plugin': "customselect"
# #                                                     }),
            
# #             'salesagent_gender':forms.Select(attrs={'class': 'form-control',
# #                                                     'aria-expanded': "false",
# #                                                     'tabindex': "0",
# #                                                     'aria-haspopup': "true",
# #                                                     'role': "combobox",
# #                                                     'data-plugin': "customselect"
# #                                                     }),
            
# #             'salesagent_status':forms.Select(attrs={'class': 'form-control',
# #                                                     'aria-expanded': "false",
# #                                                     'tabindex': "0",
# #                                                     'aria-haspopup': "true",
# #                                                     'role': "combobox",
# #                                                     'data-plugin': "customselect"
# #                                                     }),

# #         }



        
# # class AgentAddressForm(ModelForm):
# #     class Meta:
# #         model=SalesAddress
# #         fields=['salesagent_address_id','salesagent_city','salesagent_area',"salesagent_country","salesagent_postalcode"]
# #         labels = {}


# #         widgets={

# #             'salesagent_address_id': forms.TextInput(attrs={'class': 'form-control',
# #                                                     'aria-expanded': "false",
# #                                                     'tabindex': "0",
# #                                                     'aria-haspopup': "true",
# #                                                     'role': "combobox",
# #                                                     'data-plugin': "customselect"
# #                                                     }),

# #             'salesagent_city':forms.TextInput(attrs={'class': 'form-control',
# #                                                     'aria-expanded': "false",
# #                                                     'tabindex': "0",
# #                                                     'aria-haspopup': "true",
# #                                                     'role': "combobox",
# #                                                     'data-plugin': "customselect"
# #                                                     }),
# #             'salesagent_area':forms.TextInput(attrs={'class': 'form-control',
# #                                                     'aria-expanded': "false",
# #                                                     'tabindex': "0",
# #                                                     'aria-haspopup': "true",
# #                                                     'role': "combobox",
# #                                                     'data-plugin': "customselect"
# #                                                     }),
# #             'salesagent_country':forms.TextInput(attrs={'class': 'form-control',
# #                                                     'aria-expanded': "false",
# #                                                     'tabindex': "0",
# #                                                     'aria-haspopup': "true",
# #                                                     'role': "combobox",
# #                                                     'data-plugin': "customselect"
# #                                                     }),

# #             'salesagent_postalcode':forms.TextInput(attrs={'class': 'form-control',
# #                                                     'aria-expanded': "false",
# #                                                     'tabindex': "0",
# #                                                     'aria-haspopup': "true",
# #                                                     'role': "combobox",
# #                                                     'data-plugin': "customselect"
# #                                                     }),

# #         }








      