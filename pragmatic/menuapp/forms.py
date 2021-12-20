

from django import forms


class DailyForm(forms.Form):
    view_choices = [
        ('accumulate','누적'),
        ('period','기간별'),
    ]
    view_days = forms.CharField(
        choices=view_choices,
        default='accumulate',
    )

    platforms = forms.ChoiceField(choices=[],required=False)
    targets = forms.ChoiceField(choices=[],required=False)
