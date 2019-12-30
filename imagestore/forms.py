from django import forms
from imagestore.models import CICD

class TrackerForm(forms.ModelForm):
    class Meta:
        model = CICD
        fields = ['tech','deploy_date','environment','machine_name','classifier','smoke_test','smoke_test_status']
        