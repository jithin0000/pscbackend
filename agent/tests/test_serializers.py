from rest_framework.test import APITestCase
from agent.serializers import AgentSerializer


class AgentSerializerTest(APITestCase):
    def test_serialzer_phone_number_is_digit_with_12_number(self):
        data = {
            "name": "firstname", "phone_number": "1234578adf", "address_state": "kerala",
            "address_city": "Thrissur", "address_pin": "1234"
        }
        serializer = AgentSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_serialzer_phone_number_should_be_digit(self):
        data = {
            "name": "firstname", "phone_number": "12ee567890", "address_state": "kerala",
            "address_city": "Thrissur", "address_pin": "1234"
        }
        serializer = AgentSerializer(data=data)
        assert serializer.is_valid() == False

    def test_serialzer_phone_number_is_valid(self):
        data = {
            "name": "firstname", "phone_number": "123456789011", "address_state": "kerala",
            "address_city": "Thrissur", "address_pin": "1234"
        }
        serializer = AgentSerializer(data=data)
        assert serializer.is_valid() == True

    def test_serialzer_should_show_error_when_len_of_name_less_than_three(self):
        data = {
            "name": "fir", "phone_number": "1234567890", "address_state": "kerala",
            "address_city": "Thrissur", "address_pin": "1234"
        }
        serializer = AgentSerializer(data=data)
        assert serializer.is_valid() == False
