from rest_framework import serializers
from api.models import  *

class SuporteeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Suportee
    fields = ('name', 'age', 'birthday', 'location', 'autobiography',
              'contactAt', 'findMeAt', 'supporters')

class SuporterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Supporter
    fields = ('name', 'age')

class GoalsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Goals
    fields = ('suportee', 'completed', 'dateOfCompletion', 'meansToAchieve')

class PledgeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pledge
    fields = ('suportee', 'suporter', 'value')