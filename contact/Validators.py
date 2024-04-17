from django.core.exceptions import ValidationError
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def validate_number(num):
    num = num.replace(' ', '')
    if (len(num) != 13) or (num[0] != '+') or (num[1:4] != '998'):
        raise ValidationError

    if not (all([True if num[i] in nums else False for i in range(4, 13)])):
        raise ValidationError

