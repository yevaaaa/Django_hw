from django.db import models

"""
DJANGO HW 2
Deadline: OCT 20, 20:00
"""

"""
Problem 1

Create a Human model. It has name, surname, year_of_birth, and gender (can be Male or Female). 
Create a migration and syncronize with the db.
"""

MY_CHOICES = [
    ('Female', 'Female'),
    ('Male', 'Male'),
]


class Human(models.Model):
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=20)
    year_of_birth = models.IntegerField()
    gender = models.CharField(max_length=20, choices=MY_CHOICES, default='private')



"""
Problem 2

In the terminal, set DJANGO_SETTINGS_MODULE to your project settings. Open the shell. 
and create some Human objects.
"""
# >>> Human.objects.create(name='Yeva', surname='Tsughunyan', year_of_birth=2003, gender='Female')
# <Human: Human object (1)>
# >>> Human.objects.create(name='Harry', surname='Potter', year_of_birth=1980, gender='Male')
# <Human: Human object (2)>
# >>> Human.objects.create(name='Till', surname='Lindemann', year_of_birth=1963, gender='Male')
# <Human: Human object (3)>

"""
Problem 3

We want to see the Human model in the admin panel. Create a HumanAdmin class in admin.py
We want to display human's name, surname and age (*note, Human class has no field age) on the admin panel.
"""

# @admin.register(Human)
# class HumanAdmin(admin.ModelAdmin):
#     list_display = ('name', 'surname', 'age')
#
#     def age(self, obj):
#         z = 2021 - obj.year_of_birth
#         return str(z)
#
#     age.short_description = 'age'


"""
Problem 4

We want to create a route (URL) where we can see some data about humans. 
Create a view function. Inside the view function get a Human class object with id=2 and assign it to a variable. 
*the objects method might be highlighted, just ignore it
"""

# from myfirstapp.models import Human
#
#
# def about(request):
#     v = Human.objects.get(id=2)
#     return render(request, 'myfirstapp/about.html', {'context': v})



"""
Problem 5

The view function should render an HTML template. The HTML template should display the name, surname of the human.
The URL 127.0.0.1:8000/human should display that HTML.
"""

#
# def human(request):
#     h = Human.objects.get(id=1)
#     return render(request, 'myfirstapp/human.html', {'context': h})