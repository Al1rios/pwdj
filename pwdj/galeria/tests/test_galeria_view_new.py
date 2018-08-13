import pytest
from django.test import Client
from django.urls import reverse

from pwdj.django_assertions import dj_assert_contains


@pytest.fixture
def resp_without_user(client):
    return client.get(reverse('galeria:new'))


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
    assert 302 == resp_without_user.status_code


def test_status_code_user_logged(resp):
    assert 200 == resp.status_code


@pytest.mark.parametrize(
    'content', [
        '<input type="text" class="form-control" name="titulo"',
        '<input type="number" class="form-control" name="preco"',
        '<textarea name="descricao"',
        '<button type="submit"',
    ]
)
def test_index_content(resp, content):
    dj_assert_contains(resp, content)
