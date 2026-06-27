import requests
import json
from pathlib import Path
   
def test_github_user_with_token():
    #读取配置
    config_path = Path(__file__).parent / "github_config.json"
    with open(config_path, "r") as f:
        config = json.load(f)
        
    #使用token访问github api
    headers = {"Authorization": f"Bearer {config['token']}"}
    response = requests.get(f"{config['base_url']}/user", headers=headers)
    
    #duanyan
    assert response.status_code == 200
    data = response.json()
    assert data["login"] == "MRwang-cmd"
    
def test_github_user_without_token():
    #读取配置
    config_path = Path(__file__).parent / "github_config.json"
    with open(config_path, "r") as f:
        config = json.load(f)
        
    #不使用token访问github api
    response = requests.get(f"{config['base_url']}/user")
    
    #断言
    assert response.status_code == 401
    
def test_github_list_repos():
    config_path = Path(__file__).parent / "github_config.json"
    with open(config_path, "r") as f:
        config = json.load(f)

    headers = {"Authorization": f"Bearer {config['token']}"}
    response = requests.get(f"{config['base_url']}/user/repos", headers=headers)

    assert response.status_code == 200
    repos = response.json()
    assert len(repos) > 0
    # 你的测试项目 repo 应该在列表里
    repo_names = [r["name"] for r in repos]
    assert "api-test-framework" in repo_names
    assert "web-ui-automation" in repo_names
