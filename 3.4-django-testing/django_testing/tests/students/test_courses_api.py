import pytest

from students.models import Course

BASE_URL = '/api/v1/courses/'

# def test_example():
#     assert False, "Just test example"




@pytest.mark.django_db
def test_get_course(client, course_factory, student_factory):
    """проверка получения первого курса
        создаем курс
        создаем урл и  делаем гет
        проверяем
    """
    students = student_factory(_quantity=25)
    courses = course_factory(_quantity=5,students=students)
    url = BASE_URL + str(courses[0].id) + "/"
    response = client.get(url)
    data = response.json()

    assert response.status_code == 200
    assert data['id'] == courses[0].id


@pytest.mark.django_db
def test_get_courses(client, course_factory):

    """
    проверка списка
    """
    courses = course_factory(_quantity=20)
    response = client.get(BASE_URL)
    data = response.json()
    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, d in enumerate(data):
        assert d['id'] == courses[i].id


@pytest.mark.django_db
def test_get_course_filter_id(client, course_factory):
    """
    проверка фильтрации списка курсов по id
    """
    courses = course_factory(_quantity=5)
    url = BASE_URL + '?id=' + str(courses[0].id)
    response = client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert data[0]['id'] == courses[0].id



@pytest.mark.django_db
def test_get_course_filter_name(client, course_factory):
    """
    проверка фильтрации по нэйму
    """
    courses = course_factory(_quantity=10)
    url = BASE_URL + '?name=' + courses[0].name
    response = client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert data[0]['name'] == courses[0].name


@pytest.mark.django_db
def test_create_course(client):
    """
    создание курса
    """
    count = Course.objects.count()
    response = client.post(BASE_URL, data={'name': 'курс молодого мерзавца'})
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, course_factory):
    """
    изменение курса (создаем и изменяем)
    """
    # courses = course_factory(_quantity=10)
    response = client.post(BASE_URL, data={'name': 'курс молодого мерзавца'})
    assert response.status_code == 201
    response = client.get(BASE_URL)
    data = response.json()
    # print(data)
    # print(data[0]['id'])
    url = BASE_URL + str(data[0]['id']) + '/'
    response = client.patch(url, data={'name': 'курс юного винокура'})
    data = response.json()

    assert response.status_code == 200
    assert data['name'] == 'курс юного винокура'


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    """
    удалеж
    """
    courses = course_factory(_quantity=10)
    count = Course.objects.count()
    url = BASE_URL + str(courses[0].id) + '/'
    response = client.delete(url)

    assert response.status_code == 204
    assert Course.objects.count() == count - 1