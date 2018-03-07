from .models import User, Event
from rest_framework import serializers
from . import mybarcode
import random


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'email', 'phone', 'created_date')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id','url', 'name', 'description', 'price', 'organized_by', 'date', 'time', 'picture', 'location', 'created_on', 'updated_on')

    def create(self, validated_data):
    	event = Event(
            name = validated_data['name'],
            description = validated_data['description'],
            price = validated_data['price'],
            organized_by = validated_data['organized_by'],
            date = validated_data['date'],
            time = validated_data['time'],
            location = validated_data['location'],
            picture = validated_data['picture']
    		)
        event.save()
        barcode_file_name = 'barcode_event_' + str(event.id)
        unique_code = random.randint(9000000,100000000)
        barcode = mybarcode.MyBarcodeDrawing(unique_code).save(formats=['gif'],outDir='media/barcodes',fnRoot=barcode_file_name)
        barcode = barcode.replace('media/', "")

        event.unique_code = unique_code
        event.barcode = barcode

        event.save()

        return event

    # def update(self, instance, validated_data):
    #     instance.name = validated_data['name'],
    #     instance.description = validated_data['description'],
    #     instance.price = validated_data['price'],
    #     instance.organized_by = validated_data['organized_by'],
    #     instance.date = validated_data['date'],
    #     instance.time = validated_data['time'],
    #     instance.location = validated_data['location'],
    #     instance.picture = validated_data['picture']

    #     instance.save()

    #     return instance

