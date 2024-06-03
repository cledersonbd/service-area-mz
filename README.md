
# Introduction

As <company_name> expands internationally, we have a growing problem that many transportation suppliers we'd like to integrate cannot give us concrete zip codes, cities, etc that they serve.
To combat this, we'd like to be able to define custom polygons as their "service area" and we'd like for the owners of these shuttle companies to be able to define and alter their polygons whenever they want, eliminating the need for <company_name> employees to do this boring grunt work.


### Requirement:

* Build a JSON REST API with CRUD operations for Provider (name, email, phone number, language an currency) and ServiceArea (name, price, geojson information)

+ Create a specific endpoint that takes a lat/lng pair as arguments and return a list of all polygons that include the given lat/lng. The name of the polygon, provider's name, and price should be returned for each polygon. This operation should be FAST.

+ Use unit tests to test your API;

+ Write up some API docs (using any tool you see fit);

+ Create a Github account (if you don’t have one), push all your code and share the link with us;

+ Deploy your code to a hosting service of your choice. <company_name> is built entirely on AWS, so bonus points will be awarded for use of AWS.

### Considerations:

+ All of this should be built in Python/DjangoRest. 

+ Use any extra libraries you think will help, choose whatever database you think is best fit for the task, and use caching as you see fit.

+ Ensure that your code is clean, follows standard PEP8 style (though you can use 120 characters per line) and has comments where appropriate.

+ It should take you 8-10 hours to complete 

+ We will not look at any attachments, screenshots or files sent by you, only Github and your deployed server.

## Dependencies 
### Python 3.12
### PosgreSQL with PostGIS

Python Packages:
```
asgiref==3.8.1
awsebcli==3.20.10
blessed==1.20.0
botocore==1.31.85
cement==2.8.2
certifi==2024.2.2
charset-normalizer==3.3.2
colorama==0.4.3
Django==5.0.6
django-environ==0.11.2
django-geojson==4.1.0
djangorestframework==3.15.1
djangorestframework-gis==1.0
Faker==25.3.0
geojson==3.1.0
idna==3.7
jmespath==1.0.1
pathspec==0.10.1
psycopg2-binary==2.9.9
python-dateutil==2.9.0.post0
PyYAML==6.0.1
requests==2.32.3
semantic-version==2.8.5
setuptools==70.0.0
six==1.16.0
sqlparse==0.5.0
termcolor==1.1.0
urllib3==1.26.18
wcwidth==0.1.9
```
