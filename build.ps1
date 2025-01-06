# PowerShell构建脚本

# 设置环境变量
$env:Path = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine) + ";" + [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::User)

Write-Host "Starting build process..."

# 如果发生错误，停止执行
$ErrorActionPreference = "Stop"

# 安装依赖
Write-Host "Installing dependencies..."
pip install -r requirements.txt

# 收集静态文件
Write-Host "Collecting static files..."
python manage.py collectstatic --noinput

# 创建构建目录
Write-Host "Creating build directory..."
if (Test-Path .\build) {
    Remove-Item .\build -Recurse -Force
}
New-Item -ItemType Directory -Path .\build

# 复制必要的文件到构建目录
Write-Host "Copying files to build directory..."
$items = @("manage.py", "requirements.txt", "runtime.txt", "Procfile", "blog", "blog_project", "static", "staticfiles", "templates")

foreach ($item in $items) {
    if (Test-Path $item) {
        Copy-Item -Path $item -Destination .\build -Recurse -Force
    }
}

Write-Host "Build process completed." 