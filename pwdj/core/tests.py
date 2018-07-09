import pytest

from pwdj.django_assertions import dj_assert_contains


def test_status_code(client):
    response = client.get('/')
    return 200 == response.status_code


@pytest.mark.parametrize(
    'content', [
        'Project Work Django',
        'ali.rios@gmail.com',
        '+55 31 971-906677',
    ]
)
def test_home(client, content):
    response = client.get('/')
    dj_assert_contains(response, content)
