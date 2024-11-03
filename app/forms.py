from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'notes', 'date']
        widgets = {
            'category': forms.Select(choices=Expense.Category.choices),  # Uses choices defined in the model
            'amount': forms.NumberInput(attrs={'step': '0.01'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_amount(self):
        amount = self.cleaned_data['amount']

        if amount <= 0:
            raise forms.ValidationError('Expense amount must be a positive value.')

        return amount



class MonthForm(forms.Form):
    month = forms.IntegerField(
        min_value=1,
        max_value=12,
        label='Month',  # Shorter label
        widget=forms.NumberInput(attrs={'placeholder': 'Enter month (1-12)'})  # More concise placeholder
    )



class CategoryMonthForm(forms.Form):
    month = forms.IntegerField(
        label="Month",
        min_value=1,
        max_value=12,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter month (1-12)'}),
    )
    category = forms.ChoiceField(
        choices=Expense.Category.choices,
        widget=forms.Select(attrs={'class': 'category-dropdown'}),
        label="Category",
    )
