#!/bin/bash

# 如果任何命令失败，立即退出脚本
set -e

echo "Starting build process..."

# 安装依赖
echo "Installing dependencies..."
pip install -r requirements.txt

# 收集静态文件
echo "Collecting static files..."
python manage.py collectstatic --noinput

# 创建构建目录
echo "Creating build directory..."
rm -rf ./build
mkdir -p ./build

# 复制必要的文件到构建目录，使用 -L 选项解析符号链接
echo "Copying files to build directory..."
for item in manage.py requirements.txt runtime.txt Procfile blog blog_project static staticfiles templates; do
    if [ -e "$item" ]; then
        cp -rL "$item" ./build/
    fi
done

echo "Build process completed." 