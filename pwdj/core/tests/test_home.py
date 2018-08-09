import pytest

from pwdj.django_assertions import dj_assert_contains


def test_home_status_code(client):
    response = client.get('/')
    return 200 == response.status_code


@pytest.mark.parametrize(
    'content', [
        'Project Work Django',
        'ali.rios@gmail.com',
        '+55 21 971-906677',
        'href="/contato/"',
    ]
)
def test_home(client, content):
    response = client.get('/')
    dj_assert_contains(response, content)


def test_contact_status_code(client):
    response = client.get('/contato/')
    return 200 == response.status_code


@pytest.mark.parametrize(
    'content', [
        '21 971-906677',
        'Rua Paissandu Rj',
        '22210-085',
    ]
)
def test_contact_content(client, content):
    response = client.get('/contato/')
    dj_assert_contains(response, content)
