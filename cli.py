# -*- coding: utf-8 -*-
from datetime import datetime


dummy = [
    {
        "username": "homie",
        "location": "台北市信義區",
        "avatar": "https://randomuser.me/api/portraits/women/35.jpg",
        "likes": 4200,
        "email": 'foo@gmail.com',
        "register_date": datetime(2016, 8, 11),
        "updated_date": datetime(2016, 8, 12),
        "products": [
            {
                "name": "準備愛心便當",
                "price": 100,
                "available": True,
                "amount": 5,
                "required_hour": 3.0,
                "description": "在忙碌的現代生活中來點媽媽的愛心~",
                "likes": 77,
                "pictures": "http://www.bentoubako.net/contestform02/img/156.jpg",
                "pub_date": datetime(2016, 8, 11),
                "update_date": datetime(2016, 8, 11)
            },
            {
                "name": "幸運手環-無限",
                "price": 45,
                "available": True,
                "amount": 10,
                "required_hour": 3.5,
                "description": "如同梅比斯之環一樣沒有止盡，讓愛無限",
                "likes": 42,
                "pictures": "http://cdn01.pinkoi.com/product/10fPdoDk/0/79/500x0.jpg",
                "pub_date": datetime(2016, 8, 12),
                "update_date": datetime(2016, 8, 12)
            },
            {
                "name": "手作黑天鵝",
                "price": 100,
                "available": True,
                "amount": 4,
                "required_hour": 5.0,
                "description": "以中國結手工編織之黑天鵝",
                "likes": 33,
                "pictures": "http://web.dfps.tp.edu.tw/~t87140/cgi-bin/photo615/%A4%A4%B0%EA%B5%B2%A7@%AB~/%A4%A4%B0%EA%B5%B2---%A4%D1%C3Z.JPG",
                "pub_date": datetime(2016, 8, 12),
                "update_date": datetime(2016, 8, 12)
            },
        ],
    },
    {
        "username": "陳湘婷",
        "location": "台北市大安區",
        "avatar": "https://randomuser.me/api/portraits/women/23.jpg",
        "likes": 5000,
        "email": "bar@yahoo.com.tw",
        "register_date": datetime(2016, 8, 10),
        "updated_date": datetime(2016, 8, 15),
        "products": [
            {
                "name": "金工-蝴蝶",
                "price": 250,
                "available": True,
                "amount": 5,
                "required_hour": 12.0,
                "description": "以金屬工藝打造出亮麗閃閃的蝴蝶，適合配戴",
                "likes": 50,
                "pictures": "http://magimg.chinayes.com/Mags/zbsj/20100712/Article/Content/201010231930240377930.jpg",
                "pub_date": datetime(2016, 8, 10),
                "update_date": datetime(2016, 8, 15)
            },
            {
                "name": "金工-摩托車",
                "price": 600,
                "available": False,
                "amount": 0,
                "required_hour": 32.0,
                "description": "以回收之金屬打造出帥氣的摩托車，適合裝飾書桌",
                "likes": 100,
                "pictures": "https://s.yimg.com/xd/api/res/1.2/xb.TyX80gi2GJ.jtjdDXUg--/YXBwaWQ9eXR3YXVjdGlvbnNlcnZpY2U7aD01NjE7cT04NTtyb3RhdGU9YXV0bzt3PTcwMDtwPW9wZW5jdg--/http://nevec-img.zenfs.com/prod/tw_ec05-7/1e710334-af2c-4115-a7f8-6b1584a3a2b9.jpg",
                "pub_date": datetime(2016, 8, 10),
                "update_date": datetime(2016, 8, 11)
            },
        ],
    },
    {
        "username": "王左妹",
        "email": "baz@hotmail.com",
        "location": "台北市中山區",
        "avatar": "https://randomuser.me/api/portraits/women/71.jpg",
        "likes": 5503,
        "register_date": datetime(2016, 8, 13),
        "updated_date": datetime(2016, 8, 20),
        "products": [
            {
                "name": "狼嚎",
                "price": 100,
                "available": True,
                "amount": 10,
                "required_hour": 4.0,
                "description": "以紙摺藝術創作出帶有生命力的狼，以狼嚎為題",
                "likes": 47,
                "pictures": "http://image.wangchao.net.cn/bt/1272050401485.jpg",
                "pub_date": datetime(2016, 8, 16),
                "update_date": datetime(2016, 8, 18)
            }
        ],
    }
]


if __name__ == '__main__':
    import os
    from os.path import isfile
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Homie.settings")
    import django
    django.setup()

    from django.contrib.auth.models import User
    from userp.models import UserProfile

    dbname = 'db.sqlite3'
    if isfile(dbname):
        os.remove(dbname)

    os.system(''' find . -name 'migrations' -exec rm -rvf {} \; ''')
    os.system(''' python manage.py migrate ''')
    os.system(''' python manage.py makemigrations userp ''')
    os.system(''' python manage.py migrate ''')

    try:
        User.objects.all().delete()
    except:
        pass
    for dic in dummy:
        username = dic.pop('username')
        email = dic.pop('email')
        products = dic.pop('products')
        user = User.objects.create(username=username, email=email)
        user.set_password('homie')
        profile = UserProfile.objects.create(user=user, **dic)
        for product in products:
            profile.products_set.create(**product)
        profile.save()
        user.save()
