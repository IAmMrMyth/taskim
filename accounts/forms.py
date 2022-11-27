from django import forms


class RegisterForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField()
    password_confirm = forms.CharField()
    email = forms.EmailField()

    def clean_password_confirm(self):
        cleaned_data = self.cleaned_data
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('password_confirm')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "your password must match with your password confirmation.",
                code='password_mismatch',
            )
        return password2


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
