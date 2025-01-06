#!/bin/bash

# 安装依赖
pip install -r requirements.txt

# 收集静态文件
python manage.py collectstatic --noinput

# 创建构建目录
mkdir -p ./build
cp -r . ./build/ 