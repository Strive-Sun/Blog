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
mkdir -p ./build

# 复制所有文件到构建目录
echo "Copying files to build directory..."
cp -r * ./build/ 2>/dev/null || :
cp -r .* ./build/ 2>/dev/null || :

echo "Build process completed." 