import requests

def test_create_and_verify_post(base_url):
    # 测试创建文章并验证其存在
    url = f"{base_url}/posts"
    new_data = {"title": "test_title", "body": "test_body", "userId": 1}
    response = requests.post(url, json=new_data)
    assert response.status_code == 201
    data = response.json()
    post_id = data["id"]
    
    # 验证新创建的文章是否存在
    get_response = requests.get(f"{base_url}/posts/{post_id}")
    assert get_response.status_code in [200, 404], f"Unexpected status: {get_response.status_code}"
    # JSONPlaceholder 不真实持久化数据，POST 创建后 GET 可能返回 404
    # 真实项目中应断言 200 并验证数据一致性
    if get_response.status_code == 200:
       get_data = get_response.json()
       assert get_data["id"] == post_id
       assert get_data["title"] == "test_title"