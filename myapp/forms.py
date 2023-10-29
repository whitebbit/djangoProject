import phonenumbers
from django import forms
from phonenumbers.phonenumberutil import NumberParseException

from .models import Teacher, Group, Student


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        try:
            parsed_phone = phonenumbers.parse(phone, None)

            return phonenumbers.format_number(
                parsed_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL
            )
        except NumberParseException as e:
            raise forms.ValidationError(e.args[0])


class PhoneNumberForm(forms.Form):
    phone = forms.CharField(label="Номер телефона", max_length=15)

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        try:
            parsed_phone = phonenumbers.parse(phone, None)

            return phonenumbers.format_number(
                parsed_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL
            )
        except NumberParseException as e:
            raise forms.ValidationError(e.args[0])
