import requests
import pytest
import json
import allure

@allure.feature("文章管理")
@allure.story("获取文章列表")
def test_get_posts(base_url):
	 #测试获取文章列表
	url=f"{base_url}/posts"
	response = requests.get(url)
	assert response.status_code == 200

@allure.feature("文章管理")
@allure.story("获取单篇文章")
def test_get_single_post(base_url):
	#测试获取单个文章
	url=f"{base_url}/posts/1"
	response = requests.get(url)
	assert response.status_code == 200
	data = response.json()
	assert data["id"] == 1

@allure.feature("文章管理")
@allure.story("创建文章")
def test_create_post(base_url):
	#测试创建文章
	url=f"{base_url}/posts"
	new_data = {"title": "test_title", "body": "test_body", "userId": 1}
	response =  requests.post(url, json=new_data)
	assert response.status_code == 201
	data = response.json()
	assert data["id"] is not None
	assert data["title"] == "test_title"

@allure.feature("文章管理")
@allure.story("文章不存在")
def test_get_not_found_post(base_url):
	#测试获取不存在的文章
	url=f"{base_url}/posts/9999"
	response = requests.get(url)
	assert response.status_code == 404

with open("test_data/users.json", "r")as f:
    user_ids = json.load(f)

@allure.feature("用户管理")
@allure.story("获取用户")
@pytest.mark.parametrize("user_id", user_ids)
def test_get_user(user_id,base_url):
     #测试多个用户都返回200
     url=f"{base_url}/users/{user_id}"
     response = requests.get(url)
     assert response.status_code==200
     data = response.json()
     assert data["id"] == user_id

@allure.feature("文章管理")
@allure.story("修改文章")
def test_update_post(base_url):
    #测试修改文章
    url=f"{base_url}/posts/1"
    update_data = {"title": "updated_title"}
    response = requests.put(url,json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "updated_title"

@allure.feature("文章管理")
@allure.story("删除文章")
def test_delete_post(base_url):
    #测试删除文章
    url=f"{base_url}/posts/1"
    response = requests.delete(url)
    assert response.status_code == 200