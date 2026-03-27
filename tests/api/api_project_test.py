import pytest
from api.ProjectApi import ProjectApi


def test_get_projects(api_client: ProjectApi):
    assert api_client.get_all_projects().get('content') is not None
    assert len(api_client.get_all_projects().get('content')) >= 0


def test_create_project(api_client: ProjectApi):
    project_list_before = api_client.get_all_projects().get('content')

    api_client.create_project('Создался проект')

    project_list_after = api_client.get_all_projects().get('content')

    assert len(project_list_after) - len(project_list_before) == 1


def test_delete_project(api_client: ProjectApi):
    new_project = api_client.create_project("Проект для удаления")
    project_id = new_project['id']
    project_list_before = api_client.get_all_projects().get('content')

    resp = api_client.delete_project_by_id(project_id)
    print(resp)

    project_list_after = api_client.get_all_projects().get('content')

    assert len(project_list_before) - len(project_list_after) == 1
