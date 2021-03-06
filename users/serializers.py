from rest_framework import serializers


from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('username', 'email', 'first_name', 'last_name', 'telephone', 'is_student', 'is_teacher', 'is_supervisor')
