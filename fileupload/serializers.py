from rest_framework import serializers
from fileupload.models import FileUpload
import inspect
allowed_exts = ['jpg','png','jpeg']

class FileUploadSerializer(serializers.ModelSerializer):
    """ serializer for file upload """
    class Meta:
        model = FileUpload
        fields = "__all__"

    def validate_image_url(self,data):
        """ validate image url """
        file_data = str(data).split(".")
        if file_data[-1] not in allowed_exts:
            raise serializers.ValidationError("file type should be jpg, jpeg, or png")
        if data.size > 10000000:
            raise serializers.ValidationError("size should be less than 10 mb")
        return data