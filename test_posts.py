import pytest
import json
import requests
import allure

with open("test_data/posts.json", "r")as ff:
    post_datas = json.load(ff)

@allure.feature("文章管理")
@allure.story("创建文章(数据驱动)")
@pytest.mark.parametrize("post_data", post_datas)
def test_create_post(base_url,post_data):
    #循环创建文章
    url=f"{base_url}/posts"
    response = requests.post(url, json=post_data)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == post_data["title"]
    
 