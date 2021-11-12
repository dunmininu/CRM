# from rest_framework import serializers

# from .models import Lead, Agent, User


# class UserCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             "username",
#             "first_name",
#             "last_name",
#             "email",
#             "is_staff",
#             "is_active",
#             "date_joined",
#         ]


# class AgentCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Agent
#         fields = ["user"]


# class LeadCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Lead
#         fields = ["__all__"]
