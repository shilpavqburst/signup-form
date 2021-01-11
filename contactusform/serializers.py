from rest_framework import serializers
from contactusform.models import Contactusform

class ContactusformSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contactusform
        fields = ('id','name','email','phone_no','description')
