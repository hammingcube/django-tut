django-admin startproject mysite

.
├── README.md
└── mysite
    ├── manage.py
    └── mysite
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

cat mysite/settings.py

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

Some of the INSTALLED_APPS make use of at least one database table, so we need to create the tables in the database before we can use them.

python manage.py migrate

Operations to perform:
  Apply all migrations: admin, contenttypes, auth, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying sessions.0001_initial... OK

python manage.py runserver 8080

ls
db.sqlite3 manage.py  mysite

python manage.py startapp polls

polls/
├── __init__.py
├── admin.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py




Remember the three-step guide to making model changes:

Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.
The reason there’s separate commands to make and apply migrations is because you’ll commit migrations to your version control system and ship them with your app; they not only make your development easier, they’re also useable by other developers and in production.


python manage.py makemigrations 
python manage.py migrate


Operations to perform:
  Apply all migrations: admin, contenttypes, polls, auth, sessions
Running migrations:
  Applying polls.0001_initial... OK


Creating an admin user
python manage.py createsuperuser

Update Question model to include a pretty printing via __str__.
Observe we haven't really changed schema, so no need to run migrations. 

Try adding another model as follows.

class Choice(models.Model):
	choice_text = models.CharField(max_length=200)
	def __str__(self):
		return self.choice_text

Update polls/admin.py as follows:

from polls.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)

Visit localhost:8080/admin/polls and click Choices.
You see OperationalError with message
no such table: polls_choice.

Run the following steps and everything will run fine.

python manage.py makemigrations 
python manage.py migrate


A view is a “type” of Web page in your Django application that generally 
serves a specific function and 
has a specific template. 

In Django, web pages and other content are delivered by views. Each view is represented by a simple Python function (or method, in the case of class-based views). Django will choose a view by examining the URL that’s requested (to be precise, the part of the URL after the domain name).

CurrentView:

.
├── db.sqlite3
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── polls
    ├── __init__.py
    ├── admin.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── 0002_choice.py
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py


Create a view:

 from django.shortcuts import render
+from django.http import HttpResponse

-# Create your views here.
+def index(request):
+       return HttpResponse("Hello, this is index view of polls app!")


On mysite/urls.py, add:
+    url(r'^polls/', 'polls.views.index', name='polls_index')


views.py

def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

polls/urls.py

from polls import views


urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/results/5/
    url(r'^results/(?P<question_id>\d+)/$', views.detail, name='alt'),
)





