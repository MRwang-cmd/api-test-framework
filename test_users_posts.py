import requests
import allure

@allure.feature("用户管理")
@allure.story("验证用户的文章归属")
def test_user_posts_belong_to_user(base_url):
    # 测试获取用户的文章列表，并验证每篇文章的userId是否与用户ID匹配
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200
    users = response.json()
    assert len(users) > 0, "No users found in the response"

    for user in users:
        user_id = user["id"]
        url = f"{base_url}/users/{user_id}/posts"
        response = requests.get(url)
        assert response.status_code == 200
        posts = response.json()
        for post in posts:
            assert post["userId"] == user_id, f"Post ID {post['id']} does not belong to User ID {user_id}"