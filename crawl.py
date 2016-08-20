import requests

if __name__ == '__main__':
    import os
    from os.path import isfile
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Homie.settings")
    import django
    django.setup()

    from datetime import datetime
    import random

    from django.contrib.auth.models import User
    from django.db import IntegrityError
    from userp.models import UserProfile

    url = 'http://api.randomuser.me/?gender=female&inc=name,picture,email,location,registered&results=500&nat=US&noinfo'
    resp = requests.get(url)
    assert resp.status_code == 200, 'staus code != 200'

    data = resp.json()['results']

    for d in data:
        d['email']
        username = d['name']['first'] + ' ' + d['name']['last']
        print(username)
        try:
            user = User.objects.create(
                username=username,
                password='homie',
                email=d['email'],
            )
            profile = UserProfile.objects.create(
                user=user,
                avatar=d['picture']['large'],
                likes=random.choice(xrange(500, 10000)),
                location=d['location']['city'],
                register_date=datetime.strptime(d['registered'], '%Y-%m-%d %H:%M:%S'),
                updated_date=datetime.strptime(d['registered'], '%Y-%m-%d %H:%M:%S'),
            )
            user.save()
            profile.save()
        except IntegrityError:
            pass
