# 个人博客系统

这是一个基于 Django 框架开发的个人博客系统，提供了文章发布、分类管理、标签管理、评论等功能。

## 功能特点

- 文章管理：支持创建、编辑、删除文章
- 分类管理：文章分类功能
- 标签系统：文章标签管理
- 富文本编辑：集成 CKEditor 编辑器
- 响应式设计：适配各种设备屏幕
- 文章归档：按时间归档文章
- 友情链接：支持添加友情链接
- 关于页面：个人介绍页面

## 技术栈

- Python 3.8+
- Django 4.2.3
- Pillow 10.0.0（图片处理）
- django-ckeditor 6.7.0（富文本编辑器）
- django-crispy-forms 2.0（表单美化）
- crispy-bootstrap5 0.7（Bootstrap 5 支持）

## 环境要求

- Python 3.8 或更高版本
- pip（Python 包管理器）
- 虚拟环境（推荐使用）

## 安装步骤

1. 克隆项目到本地：
```bash
git clone [项目地址]
cd Blog
```

2. 创建并激活虚拟环境（Windows）：
```bash
python -m venv venv
venv\Scripts\activate
```

3. 安装依赖包：
```bash
pip install -r requirements.txt
```

4. 执行数据库迁移：
```bash
python manage.py migrate
```

5. 创建超级用户（管理员账号）：
```bash
python manage.py createsuperuser
```

## 启动项目

1. 启动开发服务器：
```bash
python manage.py runserver
```

2. 在浏览器中访问以下地址：
- 博客首页：http://127.0.0.1:8000/
- 管理后台：http://127.0.0.1:8000/admin/

## 项目结构

```
Blog/
├── blog/                   # 博客应用
├── blog_project/          # 项目配置
├── media/                 # 媒体文件
├── static/                # 静态文件
├── templates/             # 模板文件
├── manage.py             # Django 管理脚本
└── requirements.txt      # 项目依赖
```

## 主要功能入口

- 文章列表：http://127.0.0.1:8000/blog/
- 分类列表：http://127.0.0.1:8000/categories/
- 标签列表：http://127.0.0.1:8000/tags/
- 归档页面：http://127.0.0.1:8000/archive/
- 关于页面：http://127.0.0.1:8000/about/

## 配置说明

1. 数据库配置在 `blog_project/settings.py` 中
2. 静态文件配置在 `blog_project/settings.py` 中的 STATIC_URL 和 STATICFILES_DIRS
3. 媒体文件配置在 `blog_project/settings.py` 中的 MEDIA_URL 和 MEDIA_ROOT

## 注意事项

1. 开发环境下请保持 DEBUG = True
2. 生产环境部署时请修改 SECRET_KEY 并设置 DEBUG = False
3. 建议定期备份数据库
4. 上传图片会保存在 media 目录下

## 许可证

本项目采用 MIT 许可证 