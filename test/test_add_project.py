from model.project import Project


def test_add_project(app, json_projects):

    project = json_projects
    old_projects = app.project.get_projects_list()
    app.project.create_project(project)
    assert len(old_projects) + 1 == app.project.count_projects()





#import pytest
#from data.groups import constant as testdata


#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
#def test_add_group(app, json_groups):
    #group = json_groups
    #old_groups = app.group.get_group_list()
    #app.group.create(group)
    #assert len(old_groups) + 1 == app.group.count()
    #new_groups = app.group.get_group_list()
    #old_groups.append(group)
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


