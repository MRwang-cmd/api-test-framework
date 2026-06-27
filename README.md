# 接口自动化测试框架

基于 Python + Pytest + Requests + Allure 搭建的接口自动化测试框架，对 REST API 进行 CRUD 全流程自动化测试及 GitHub API 鉴权接口测试，共 **18 条**用例。

## 技术栈

| 组件 | 用途 |
|------|------|
| Python 3.13 | 编程语言 |
| Pytest 9.1 | 测试框架 |
| Requests 2.34 | HTTP 客户端 |
| Allure 2.43 | 测试报告 |
| JSON | 测试数据存储 |

## 项目结构

```
api_test_project/
├── test_demo.py               # 文章CRUD + 用户参数化测试
├── test_posts.py              # 数据驱动创建文章测试
├── test_users_posts.py        # 关联接口：用户→帖子归属验证
├── test_create_and_verify.py  # 关联接口：POST创建后GET验证一致性
├── test_github_auth.py        # GitHub API 鉴权测试（含token/无token/查仓库）
├── conftest.py                # pytest fixture（base_url 等公共配置）
├── test_data/
│   ├── users.json        # 用户测试数据
│   └── posts.json        # 文章测试数据
├── allure-results/       # Allure 原始报告数据
├── requirements.txt      # 依赖清单
└── README.md
```

## 测试范围

### 文章管理（feature）
- 获取文章列表
- 获取单篇文章
- 创建文章
- 修改文章
- 删除文章
- 文章不存在（404）

### 用户管理（feature）
- 获取用户（数据驱动，5组用户ID）
- 验证用户帖子归属（关联接口：GET /users → GET /users/{id}/posts）
- POST 创建后 GET 验证一致性（写操作后验证持久化，含 JSONPlaceholder 模拟特性说明）

### GitHub API 鉴权测试（feature）
- 带 token 请求 `/user`，验证返回用户信息（200）
- 不带 token 请求 `/user`，验证拒绝访问（401）
- 带 token 请求 `/user/repos`，验证仓库列表包含项目仓库

## 快速开始

```bash
# 1. 创建虚拟环境
python -m venv venv
venv\Scripts\activate

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行测试
pytest -v

# 4. 生成 Allure 报告
pytest -v --alluredir=./allure-results --clean-alluredir
allure serve ./allure-results
```

## 被测接口

- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) — 免费公开的 REST API，无需认证
- [GitHub REST API](https://docs.github.com/en/rest) — 需 Personal Access Token 鉴权

## 项目亮点

- **数据驱动**：测试数据与代码分离，新增用例只需修改 JSON 文件
- **fixture 管理**：通过 conftest.py 统一管理 base_url 等公共配置
- **鉴权测试**：覆盖 token 鉴权（200 vs 401），模拟真实业务中的权限校验场景
- **异常覆盖**：覆盖正常场景与异常场景（404）
- **可视化报告**：Allure 报告按 feature/story 分组，可追溯每条用例的执行结果
