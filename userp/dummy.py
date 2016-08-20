# -*- coding: utf-8 -*-
"""Dummy data creation."""
from datetime import datetime

from django.contrib.auth.models import User
from userp.models import UserProfile


dummy = [
    {
        "username": "吳子琳",
        "location": "台北市信義區",
        "email": 'foo@gmail.com',
        "register_date": datetime(2016, 8, 11),
        "updated_date": datetime(2016, 8, 12),
        "products": [
            {
                "name": "幸運手環-無限",
                "price": 45,
                "available": True,
                "amount": 10,
                "required_hour": 3.5,
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
        "email": "bar@yahoo.com.tw",
        "register_date": datetime(2016, 8, 10),
        "updated_date": datetime(2016, 8, 15),
        "products": [
            {
                "name": "蝴蝶",
                "price": 250,
                "available": True,
                "amount": 5,
                "required_hour": 8.0,
                "likes": 50,
                "pictures": "http://magimg.chinayes.com/Mags/zbsj/20100712/Article/Content/201010231930240377930.jpg",
                "pub_date": datetime(2016, 8, 10),
                "update_date": datetime(2016, 8, 15)
            },
            {
                "name": "摩托車",
                "price": 600,
                "available": False,
                "amount": 0,
                "required_hour": 24.0,
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
        "register_date": datetime(2016, 8, 13),
        "updated_date": datetime(2016, 8, 20),
        "products": [
            {
                "name": "狼嚎",
                "price": 100,
                "available": True,
                "amount": 10,
                "required_hour": 4.0,
                "likes": 47,
                "pictures": "http://image.wangchao.net.cn/bt/1272050401485.jpg",
                "pub_date": datetime(2016, 8, 16),
                "update_date": datetime(2016, 8, 18)
            }
        ],
    }
]

if __name__ == '__main__':
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
