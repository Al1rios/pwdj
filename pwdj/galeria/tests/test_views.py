from os import path

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from pwdj.django_assertions import dj_assert_contains
from pwdj.galeria.models import Model


def test_app_link_in_home(client):
    response = client.get('/')
    dj_assert_contains(response, reverse('galeria:index'))


IMAGE_PATH = path.dirname(__file__)
IMAGE_PATH = path.join(IMAGE_PATH, 'intel.jpg')


@pytest.fixture
def galeria(db):
    image = SimpleUploadedFile(
        name='intel.jpg', content=open(IMAGE_PATH, 'rb').read(), content_type='image/jpeg')
    model = Model(
        titulo='Social media now takes',
        preco='400.00',
        foto=image,
        descricao='We need people like you, and we need people not like')

    model.save()
    return [model]


@pytest.fixture
def resp(client, galeria):
    return client.get(reverse('galeria:index'))


def test_status_code(resp):
    assert 200 == resp.status_code


@pytest.mark.parametrize(
    'content', [
        '400,00',
        'TechPortfolio',
        'We need people',
    ]
)
def test_index_content(resp, content):
    dj_assert_contains(resp, content)


def test_image_url(resp, galeria):
    model = galeria[0]
    dj_assert_contains(resp, model.foto.url)
