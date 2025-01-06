import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
django.setup()

from blog.models import Post, Category, Tag
from django.contrib.auth.models import User

def update_posts():
    try:
        # 更新 Go 项目配置文章
        go_post = Post.objects.get(title="Go 项目的配置流程")
        go_post.content = """
# Windows 下 Go 项目环境配置指南 🚀

本文将指导你如何在 Windows 系统上正确配置 Go 项目的开发环境。通过以下步骤，你可以快速搭建一个完整的 Go 开发环境。

## 1. 安装 Go 语言环境 🛠️

### 1.1 下载安装包

1. 访问 Go 官方网站：[https://golang.org/dl/](https://golang.org/dl/)
2. 下载 Windows 版本的安装包（选择 `.msi` 格式）
3. 双击运行安装程序，按照提示完成安装

### 1.2 验证安装

打开命令提示符（CMD）或 PowerShell，输入：
```bash
go version
```
如果看到类似 `go version go1.21.0 windows/amd64` 的输出，说明安装成功。

## 2. 配置环境变量 ⚙️

### 2.1 系统变量设置

1. 右键 "此电脑" → "属性" → "高级系统设置" → "环境变量"
2. 在系统变量中添加或修改：
   - `GOROOT`：Go 安装目录（例如：`C:\\Go`）
   - `GOPATH`：Go 工作空间目录（例如：`D:\\GoProjects`）
   - 将 `%GOROOT%\\bin` 添加到 `Path` 变量

### 2.2 创建工作目录

在 GOPATH 下创建以下目录：
- `src`：源代码目录
- `pkg`：包文件目录
- `bin`：可执行文件目录

## 3. 配置代理设置 🌐

为了加快依赖包的下载速度，建议配置 Go 模块代理：

```bash
go env -w GO111MODULE=on
go env -w GOPROXY=https://goproxy.cn,direct
```

## 4. 编辑器配置 📝

### 4.1 安装 VS Code

1. 下载并安装 [Visual Studio Code](https://code.visualstudio.com/)
2. 安装 Go 扩展：
   - 打开 VS Code
   - 按 `Ctrl+Shift+X`
   - 搜索并安装 "Go" 扩展

### 4.2 配置 Go 工具

在 VS Code 中：
1. 按 `Ctrl+Shift+P`
2. 输入 "Go: Install/Update Tools"
3. 全选所有工具并安装

## 5. 测试环境 ✨

创建一个测试项目：

1. 创建项目目录：
```bash
mkdir hello
cd hello
go mod init hello
```

2. 创建测试文件 `main.go`：
```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, Go!")
}
```

3. 运行测试：
```bash
go run main.go
```

## 6. 常见问题解决 🔧

1. **找不到 GOPATH**
   - 检查环境变量是否正确设置
   - 重启命令行或 IDE

2. **模块下载失败**
   - 确认代理设置是否正确
   - 检查网络连接

3. **IDE 工具安装失败**
   - 确保网络连接正常
   - 尝试使用管理员权限运行 VS Code

## 总结 📚

完成以上步骤后，你就拥有了一个完整的 Go 开发环境。现在可以开始你的 Go 语言开发之旅了！

记住：
- 定期更新 Go 版本
- 保持工具链更新
- 合理组织项目结构

祝你编码愉快！🎉
"""
        go_post.excerpt = "详细介绍如何在 Windows 系统上配置 Go 项目开发环境，包括安装、环境变量设置、代理配置、IDE 设置等完整步骤。"
        go_post.use_markdown = True
        go_post.save()
        
        # 更新 Git 同步文章
        git_post = Post.objects.get(title="git 同步上游仓库到远端仓库")
        git_post.content = """
# Git 仓库同步指南：上游到远端 🔄

本文将介绍如何使用 Git 将上游仓库（upstream）的更新同步到你的远端仓库（remote）。这在参与开源项目或团队协作时特别有用。

## 1. 基本概念 📚

在开始之前，让我们先理解几个重要概念：

- **上游仓库（Upstream）**：原始仓库，你 fork 的来源
- **远端仓库（Remote）**：你在 GitHub/GitLab 上的仓库副本
- **本地仓库（Local）**：你电脑上的代码副本

## 2. 配置仓库 ⚙️

### 2.1 查看远程仓库

首先，检查当前配置的远程仓库：

```bash
git remote -v
```

### 2.2 添加上游仓库

如果还没有配置上游仓库，使用以下命令添加：

```bash
git remote add upstream https://github.com/original/repository.git
```

## 3. 同步流程 🔄

### 3.1 获取上游更新

1. 切换到主分支：
```bash
git checkout main  # 或 master
```

2. 获取上游仓库的更新：
```bash
git fetch upstream
```

### 3.2 合并更新

将上游的更新合并到本地分支：

```bash
git merge upstream/main
```

### 3.3 推送到远端

将更新推送到你的远端仓库：

```bash
git push origin main
```

## 4. 处理冲突 ⚔️

如果遇到合并冲突：

1. 使用编辑器打开冲突文件
2. 寻找冲突标记（`<<<<<<<`, `=======`, `>>>>>>>`）
3. 手动解决冲突
4. 保存文件
5. 添加修改：
```bash
git add .
```
6. 提交更改：
```bash
git commit -m "解决合并冲突"
```

## 5. 最佳实践 ✨

1. **定期同步**
   - 经常从上游拉取更新
   - 避免产生大量冲突

2. **创建分支**
   - 在新分支上开发新功能
   - 保持主分支与上游同步

3. **提交信息**
   - 写清晰的提交信息
   - 说明同步的目的和内容

## 6. 常见问题 🔧

1. **无法添加上游仓库**
   - 检查 URL 是否正确
   - 确认有访问权限

2. **推送被拒绝**
   - 可能需要先拉取远端更新
   - 解决可能的冲突

3. **合并冲突频繁**
   - 考虑更频繁地同步
   - 改进开发工作流程

## 总结 📝

通过以上步骤，你可以轻松地保持你的仓库与上游仓库同步。记住：

- 定期同步可以减少冲突
- 保持良好的分支管理习惯
- 仔细处理每个冲突

祝你的代码同步顺利！🎉
"""
        git_post.excerpt = "详细介绍如何使用 Git 将上游仓库的更新同步到远端仓库，包括基本概念、配置步骤、同步流程、冲突处理等内容。"
        git_post.use_markdown = True
        git_post.save()
        
        print("文章更新成功！✨")
        
    except Post.DoesNotExist:
        print("未找到指定文章！")

def add_vscode_nodejs_debug_post():
    try:
        # 获取或创建分类
        category, _ = Category.objects.get_or_create(name='技术教程')
        
        # 获取或创建标签
        vscode_tag, _ = Tag.objects.get_or_create(name='VSCode')
        nodejs_tag, _ = Tag.objects.get_or_create(name='Node.js')
        debug_tag, _ = Tag.objects.get_or_create(name='调试')
        
        # 获取作者
        author = User.objects.get(id=1)
        
        # 创建文章
        post = Post.objects.create(
            title="使用 VSCode 调试 Node.js 代码",
            content="""
# 使用 VSCode 调试 Node.js 代码指南 🔍

本文将详细介绍如何使用 Visual Studio Code (VSCode) 来调试 Node.js 代码，帮助你更高效地进行开发和问题排查。

## 1. 环境准备 🛠️

### 1.1 必要软件安装

1. **Node.js**
   - 访问 [Node.js 官网](https://nodejs.org/)
   - 下载并安装最新的 LTS 版本
   - 验证安装：
     ```bash
     node --version
     npm --version
     ```

2. **Visual Studio Code**
   - 下载并安装 [VSCode](https://code.visualstudio.com/)
   - 安装 Node.js 调试插件（内置）

## 2. 调试配置 ⚙️

### 2.1 创建调试配置文件

1. 在 VSCode 中打开你的项目
2. 点击左侧的调试图标（或按 `Ctrl+Shift+D`）
3. 点击 "创建 launch.json 文件"
4. 选择 "Node.js" 环境

VSCode 会自动创建 `.vscode/launch.json` 文件，基本配置如下：

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "node",
            "request": "launch",
            "name": "启动程序",
            "skipFiles": [
                "<node_internals>/**"
            ],
            "program": "${workspaceFolder}/app.js"
        }
    ]
}
```

### 2.2 配置说明

- **type**: 调试器类型，使用 "node" 表示 Node.js 调试器
- **request**: 请求类型，"launch" 表示启动新进程
- **name**: 配置名称，显示在调试配置下拉菜单中
- **program**: 启动时运行的文件
- **skipFiles**: 调试时要跳过的文件

## 3. 开始调试 🚀

### 3.1 设置断点

1. 在代码行号左侧点击设置断点
2. 或在代码行使用 `F9` 快捷键
3. 断点会显示为红色圆点

### 3.2 启动调试

1. 按 `F5` 启动调试
2. 或点击调试面板中的绿色播放按钮
3. 程序会在断点处暂停

### 3.3 调试控制

使用调试工具栏或快捷键：
- **继续 (F5)**: 继续执行到下一个断点
- **单步跳过 (F10)**: 执行当前行，不进入函数
- **单步调试 (F11)**: 进入函数内部
- **单步跳出 (Shift+F11)**: 跳出当前函数
- **重启 (Ctrl+Shift+F5)**: 重新启动调试
- **停止 (Shift+F5)**: 终止调试会话

## 4. 高级调试功能 💡

### 4.1 条件断点

1. 右键点击断点
2. 选择"编辑断点"
3. 输入条件表达式，如：`count > 5`

### 4.2 监视变量

1. 在调试面板中展开"监视"
2. 点击 + 添加表达式
3. 输入要监视的变量或表达式

### 4.3 调试控制台

1. 使用调试控制台执行命令
2. 在暂停状态下查看变量值
3. 使用 `console.log` 输出信息

## 5. 常见调试场景 🎯

### 5.1 异步代码调试

```javascript
async function fetchData() {
    try {
        const response = await fetch('https://api.example.com/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
}
```

### 5.2 Express 应用调试

```json
{
    "type": "node",
    "request": "launch",
    "name": "启动 Express",
    "program": "${workspaceFolder}/app.js",
    "env": {
        "PORT": "3000"
    }
}
```

## 6. 调试技巧 💪

1. **使用 logpoints**
   - 右键断点选择"添加 logpoint"
   - 输入日志消息，不会暂停执行

2. **使用 source maps**
   - 确保启用 source maps
   - 在 `launch.json` 中设置 `"sourceMaps": true`

3. **调试生产环境**
   - 使用 `--inspect` 标志启动 Node.js
   - 配置远程调试

## 总结 📝

通过本文的学习，你应该能够：
- 配置 VSCode 的 Node.js 调试环境
- 使用断点和调试控制器
- 处理常见的调试场景
- 运用高级调试技巧

记住：
- 合理使用断点
- 熟练使用调试快捷键
- 善用监视和调试控制台

祝你调试顺利！🎉

> 参考链接：[使用 vscode 调试 nodejs 代码](https://www.cnblogs.com/strive-sun/p/18560976)
""",
            excerpt="详细介绍如何使用 VSCode 调试 Node.js 代码，包括环境配置、调试技巧、断点设置等内容，帮助开发者更高效地进行代码调试。",
            author=author,
            category=category,
            use_markdown=True
        )
        
        # 添加标签
        post.tags.add(vscode_tag, nodejs_tag, debug_tag)
        
        print("VSCode 调试 Node.js 文章添加成功！✨")
        
    except Exception as e:
        print(f"添加文章时出错：{str(e)}")

if __name__ == "__main__":
    update_posts()
    add_vscode_nodejs_debug_post() 