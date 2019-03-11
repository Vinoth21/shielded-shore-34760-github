from rest_framework import serializers
from orderapp.models import Menu, UserObjects
from django.contrib.auth.models import User
from datetime import date

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        url = serializers.HyperlinkedIdentityField(view_name='menu-list', read_only=True)
        fields = ('id','item', 'price','image','url')
        read_only_fields = ('image', )

class UserObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserObjects
        user = serializers.ReadOnlyField(source='owner.username')
        fields = ('item', 'user', 'like_status', 'date_liked')
"""
        if self.request.user:
            menu = Menu.objects.all()
            for userobj in model.objects.all():
                if (userobj.like_status == True and userobj.date_liked == date.today):
                    menu.votes += 1
"""

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        #quantity = serializers.ReadOnlyField()
        fields =('item', 'price')



"""

class UserSerializer(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(many=True, queryset=Menu.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'menu')

"""