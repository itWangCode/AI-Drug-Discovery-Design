## Git 与 GitHub 的链条配置详细步骤

Git 是一个分布式版本控制系统，而 GitHub 是一个基于 Git 的代码托管平台。以下步骤详细说明了如何在本地配置 Git、链接 GitHub，并进行基本的 Git 操作。

---

### 步骤 1：安装 Git

#### Windows 系统
1. 前往 [Git 官方网站](https://git-scm.com/)，下载适合 Windows 的安装程序。
2. 按照安装向导完成 Git 的安装。
   - 在安装过程中，可以选择默认设置。如果你需要自定义，可以根据自己的需求调整配置。
3. 完成安装后，使用 **Git Bash** 或 **命令提示符** 来执行 Git 命令。

#### macOS 系统
1. Git 通常会预装在 macOS 中，你可以通过终端运行以下命令来检查是否已经安装：

```bash
git --version
```

如果没有安装，你可以使用 Homebrew 安装 Git：

```bash
brew install git
```

---

### 步骤 2：配置 Git

完成安装后，使用以下命令在本地配置 Git：

```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

这将设置你的 Git 全局用户名和邮箱，GitHub 将根据这些信息识别你的身份。

你可以使用以下命令查看配置是否成功：

```bash
git config --list
```

---

### 步骤 3：生成 SSH 密钥并添加到 GitHub

使用 SSH 密钥可以实现 GitHub 与本地 Git 的安全连接。

#### 生成 SSH 密钥
1. 打开终端或 Git Bash，输入以下命令生成 SSH 密钥：

```bash
ssh-keygen -t rsa -b 4096 -C "youremail@example.com"
```

- 你将会被提示选择保存密钥的位置，按回车使用默认路径 (`~/.ssh/id_rsa`)。
- 你可以设置一个密码短语，或者按回车跳过。

2. 生成密钥后，查看公钥：

```bash
cat ~/.ssh/id_rsa.pub
```

3. 复制生成的公钥。

#### 将公钥添加到 GitHub
1. 登录 [GitHub](https://github.com)，进入个人设置页面。
2. 在左侧菜单中，找到 **SSH and GPG keys** 选项。
3. 点击 **New SSH key**，将刚才复制的公钥粘贴到输入框中，并为其命名。
4. 保存密钥。

---

### 步骤 4：测试 SSH 连接

在终端或 Git Bash 中运行以下命令，测试是否成功连接到 GitHub：

```bash
ssh -T git@github.com
```

如果一切正常，你将会看到类似如下的信息：

```bash
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

此时，本地 Git 已经与 GitHub 成功连接。

---

### 步骤 5：创建或克隆 GitHub 仓库

#### 方法 1：创建新仓库

1. 登录 GitHub，点击右上角的 **+** 号，选择 **New repository**。
2. 填写仓库名称、描述，选择是否公开或私有。
3. 创建成功后，你将看到仓库的 HTTPS 或 SSH 链接。

在本地初始化 Git 仓库并将其推送到 GitHub：

```bash
# 在本地创建一个新项目文件夹
mkdir AI-drug-design
cd AI-drug-design

# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 提交变更
git commit -m "Initial commit"

# 链接远程仓库（使用你的仓库链接替换下方的链接）
git remote add origin git@github.com:itWangCode/AI-drug-design.git

# 推送代码到远程仓库
git push -u origin master
```

#### 方法 2：克隆现有仓库

你也可以直接克隆已有的 GitHub 仓库到本地：

```bash
git clone git@github.com:itWangCode/AI-drug-design.git
```

---

### 步骤 6：基本 Git 操作

#### 1. 提交更改

在本地修改代码后，使用以下命令提交更改：

```bash
# 查看更改状态
git status

# 添加文件到暂存区
git add .

# 提交变更
git commit -m "Your commit message"

# 推送到远程仓库
git push origin master
```

#### 2. 拉取最新代码

在团队合作时，你可以从远程仓库拉取最新的代码：

```bash
git pull origin master
```

#### 3. 创建分支

如果你需要开发新功能或修复 bug，建议创建新分支：

```bash
# 创建新分支
git checkout -b new-feature

# 提交更改后，将新分支推送到远程仓库
git push origin new-feature
```

#### 4. 合并分支

完成开发后，可以将分支合并到主分支：

```bash
# 切换到主分支
git checkout master

# 合并新分支
git merge new-feature

# 推送更新到远程仓库
git push origin master
```

