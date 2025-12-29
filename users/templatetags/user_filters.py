from django import template
from datetime import timedelta
from django.utils import timezone

register = template.Library()

@register.filter
def humanized_date(value):
    if value:
        value = timezone.localtime(value)  # সময় localize করা
        today = timezone.localtime(timezone.now()).date()
        yesterday = today - timedelta(days=1)

        if value.date() == today:
            return f"Today at {value.strftime('%I:%M %p')}"
        elif value.date() == yesterday:
            return f"Yesterday at {value.strftime('%I:%M %p')}"
        else:
            return f"{value.strftime('%B %d, %Y at %I:%M %p')}"
    return "No record available"
