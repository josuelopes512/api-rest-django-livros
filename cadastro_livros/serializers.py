

from .models import Livro
# from .convert_slug import *
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.db import IntegrityError
from rest_framework.serializers import ModelSerializer, ValidationError

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"

    def validate(self, data):
        # count = 0;
        if 'slug' in data.keys():
            data['slug'] = slugify(data['titulo'])

        if not 'slug' in data.keys():
            try:
                data['slug'] = slugify(data['titulo'])
            except IntegrityError.ValidationError as e:
                raise ValidationError(e + "ERRO")
            
            # count += 1
        
        
        # if 'slug' in data.keys() and count == 0:
        #     if data['slug'] == slugify(data['titulo']):
        #         data['slug'] = data['slug']+'-'+ str(len(data['slug'])) + '1'
        #         return data
        
        return data