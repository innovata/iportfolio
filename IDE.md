
#============================================================
# Google Cloud Platform
#============================================================

# pip install google-cloud-storage
cachetools-3.1.0
google-api-core-1.8.2
google-auth-1.6.3
google-cloud-core-0.29.1
google-cloud-storage-1.14.0
google-resumable-media-0.3.2
googleapis-common-protos-1.5.9
protobuf-3.7.1
pyasn1-0.4.5
pyasn1-modules-0.2.4 rsa-4.0

# Deploy the app to the App Engine

https://cloud.google.com/python/django/appengine
gcloud auth login
virtualenv env
source env/bin/activate
python manage.py makemigrations
python manage.py makemigrations polls
python manage.py migrate


#============================================================
# Django
#============================================================
