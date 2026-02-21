from django.core.exceptions import ValidationError


def validate_price_reasonable(value):
    if value > 10000:
        raise ValidationError("Price is unrealistically high.")


def validate_description_length(value):
    if len(value.strip()) < 15:
        raise ValidationError("Description must be at least 15 characters long.")

def validate_image_size(image):
    limit = 5 * 1024 * 1024
    if image.size > limit:
        raise ValidationError("Image file too large. Maximum size is 5MB.")

def validate_review_body(value):
    if len(value.strip()) < 10:
        raise ValidationError(
            "Review must contain at least 10 characters."
        )