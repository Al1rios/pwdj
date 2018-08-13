import pytest
from django.test import Client
from django.urls import reverse

from pwdj.galeria.models import Model


@pytest.fixture
def resp_without_user(client: Client):
    return client.get(reverse('galeria:create'),
                      data={
                          'titulo': 'Social media now takes',
                          'preco': '400,00',
                          'descricao': 'We need people like you, and we need people not like',
                      })


@pytest.fixture
def user(django_user_model):
    usr = django_user_model(name='Ali')
    usr.save()
    return usr


@pytest.fixture
def resp(user, client: Client):
    client.force_login(user)
    return resp_without_user(client)


def test_status_code_user_not_logged(resp_without_user):
    assert resp_without_user.url.startswith(reverse('login'))


def test_status_code_user_logged(resp):
    assert resp.url.startswith(reverse('galeria:index'))


def test_galeria_salva(resp):
    assert Model.objects.exists()
