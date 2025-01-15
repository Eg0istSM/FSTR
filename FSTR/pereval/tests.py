import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from pereval.serializers import *


class PerevalApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.pereval_one = Pereval.objects.create(
            user=User.objects.create(
                email="TestOne@mail.ru",
                fam="TestOne",
                name="TestOne",
                otc="TestOne",
                phone="8-001-001-01-01"
            ),
            beauty_title="PerevalOne",
            title="PerevalOne",
            other_title="PerevalOne",
            connect="",
            coords=Coords.objects.create(
                latitude=27.00001,
                longitude=10.00001,
                height=3991
            ),
            level=Level.objects.create(
                winter='a1',
                summer='a1',
                autumn='a1',
                spring='a1'
            )
        )
        self.images_1_1 = Images.objects.create(
            data="https://pereval.ru/pereval1-1.jpg",
            title="pereval1-1",
            pereval=self.pereval_one
        )
        self.images_1_1 = Images.objects.create(
            data="https://pereval.ru/pereval1-2.jpg",
            title="pereval1-2",
            pereval=self.pereval_one
        )

        self.pereval_two = Pereval.objects.create(
            user=User.objects.create(
                email="TestTwo@mail.ru",
                fam="TestTwo",
                name="TestTwo",
                otc="TestTwo",
                phone="8-002-002-02-02"
            ),
            beauty_title="PerevalTwo",
            title="PerevalTwo",
            other_title="PerevalTwo",
            connect="",
            coords=Coords.objects.create(
                latitude=27.00002,
                longitude=10.00002,
                height=3992
            ),
            level=Level.objects.create(
                winter='a2',
                summer='a2',
                autumn='a2',
                spring='a2'
            )
        )
        self.images_2_1 = Images.objects.create(
            data="https://pereval.ru/pereval2-1.jpg",
            title="pereval2-1",
            pereval=self.pereval_two
        )
        self.images_2_2 = Images.objects.create(
            data="https://pereval.ru/pereval2-2.jpg",
            title="pereval2-2",
            pereval=self.pereval_two
        )

        self.pereval_three = Pereval.objects.create(
            user=User.objects.create(
                email="TestThree@mail.ru",
                fam="TestThree",
                name="TestThree",
                otc="TestThree",
                phone="8-003-003-03-03"
            ),
            beauty_title="PerevalThree",
            title="PerevalThree",
            other_title="PerevalThree",
            connect="",
            coords=Coords.objects.create(
                latitude=27.00003,
                longitude=10.00003,
                height=3993
            ),
            level=Level.objects.create(
                winter='a3',
                summer='a3',
                autumn='a3',
                spring='a3'
            ),
            status="pending"
        )
        self.images_3_1 = Images.objects.create(
            data="https://pereval.ru/pereval3-1.jpg",
            title="pereval3-1",
            pereval=self.pereval_three
        )
        self.images_3_2 = Images.objects.create(
            data="https://pereval.ru/pereval3-2.jpg",
            title="pereval3-2",
            pereval=self.pereval_three
        )

    def test_get(self):
        url = reverse('pereval')
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_one, self.pereval_two, self.pereval_three], many=True).data
        for pereval in Pereval.objects.all():
            print('********')
            print(pereval.id)
            print('--------')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 3)

    def test_get_detail(self):
        pass
