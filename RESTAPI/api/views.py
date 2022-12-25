from django.views import View
from django.http import JsonResponse
import json
from .models import Person
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class Person(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        p_name = data.get('name')
        p_age = data.get('age')
        p_date_of_birth = data.get('date_of_birth')

        person_data = {
            'name': p_name,
            'age': p_age,
            'date_of_birth': p_date_of_birth,
        }

        person = Person.objects.create(**person_data)

        data = {
            "message": f"Someone was added with id: {person.id}"
        }
        return JsonResponse(data, status=201)

    def get(self, request):
        person_count = Person.objects.count()
        people = Person.objects.all()

        person_data = []
        for person in people:
            person_data.append({
                'name': person.name,
                'age': person.age,
                'date_of_birth': person.date_of_birth,
            })

        data = {
            'person': person_data,
            'count': person_count,
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class PersonUpdate(View):
    def patch(self, request, person_id):
        data = json.loads(request.body.decode("utf-8"))
        person = Person.objects.get(id=person_id)
        person.date_of_birth = data['date_of_birth']
        person.save()

        data = {
            'message': f'Person with id:{person_id} has been updated'
        }

        return JsonResponse(data)
    
    def delete(self, request, person_id):
        person = Person.objects.get(id=person_id)
        person.delete()

        data = {
            'message': f'Person {person_id} has been deleted'
        }

        return JsonResponse(data)