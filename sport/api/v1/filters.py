from ...models import Plan
import django_filters

class PlanFilter(django_filters.FilterSet):

    class Meta:
        model = Plan
        fields = {
            'course': ['exact'],
            'action':['exact'],
            'action__title':['icontains'],
            'day_of_week':['iexact']
        }