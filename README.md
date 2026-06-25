# 接口自动化测试框架

基于 Python + Pytest + Requests + Allure 搭建的接口自动化测试框架，对 REST API 进行 CRUD 全流程自动化测试。

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
├── test_demo.py          # 文章CRUD + 用户参数化测试
├── test_posts.py         # 数据驱动创建文章测试
├── conftest.py           # pytest fixture（base_url 等公共配置）
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

## 快速开始

```bash
# 1. 创建虚拟环境
python -m venv venv
venv\Scripts\activate

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行测试
pytest test_demo.py test_posts.py -v

# 4. 生成 Allure 报告
pytest test_demo.py test_posts.py -v --alluredir=./allure-results --clean-alluredir
allure serve ./allure-results
```

## 被测接口

[JSONPlaceholder](https://jsonplaceholder.typicode.com/) — 免费公开的 REST API，无需认证。

## 项目亮点

- **数据驱动**：测试数据与代码分离，新增用例只需修改 JSON 文件
- **fixture 管理**：通过 conftest.py 统一管理 base_url 等公共配置
- **异常覆盖**：覆盖正常场景与异常场景（404）
- **可视化报告**：Allure 报告按 feature/story 分组，可追溯每条用例的执行结果
