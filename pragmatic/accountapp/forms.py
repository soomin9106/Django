from django.contrib.auth.forms import UserCreationForm


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True #초기화 이후에 바꿔지는 부분