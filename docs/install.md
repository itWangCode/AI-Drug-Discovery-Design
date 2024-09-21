
# 配置代码环境

### ❤️如果是小白的话，请您谦虚的看着下面的步骤：

### 一、Windows 和 macOS 系统上安装和配置 Git，并拉取我的代码到本地。

如果你想要了解 更多的Git的知识，请您前往[如果操作git流程.md]

接下来，我将一步步为你讲解如何在 Windows 和 macOS 系统上安装和配置 Git，并拉取我的代码到本地。

### Windows 系统

#### 1. 下载并安装 Git

- 前往 [Git 官方下载页面](https://git-scm.com/)。
- 选择 Windows 版本进行下载，并按照提示完成安装。
  - 安装时，默认选项即可。如果想要自定义，可以根据需要选择不同的配置，比如编辑器、环境变量等。

#### 2. 配置 Git

安装完成后，打开终端（或 Git Bash）并配置你的 Git 用户信息：

```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

这样，Git 就会在你每次提交代码时使用这些信息来标识你的身份。

#### 3. 生成 SSH 密钥

在 Windows 上，打开 Git Bash，输入以下命令生成 SSH 密钥：

```bash
ssh-keygen -t rsa -b 4096 -C "youremail@example.com"
```

- 按回车后，你会看到提示选择存储密钥的位置，默认按回车即可。
- 然后你需要设置一个密码，可以为空，但建议设置。

#### 4. 添加 SSH 密钥到 GitHub

- 使用以下命令显示你生成的公钥：

```bash
cat ~/.ssh/id_rsa.pub
```

- 复制公钥并登录 GitHub。
- 前往 GitHub 的 [SSH 和 GPG 密钥页面](https://github.com/settings/keys)，点击 **New SSH key**。
- 将你刚才复制的公钥粘贴到文本框中，添加后保存。

#### 5. 克隆 GitHub 仓库

完成 SSH 密钥配置后，你可以使用以下命令克隆代码仓库：

```bash
git clone git@github.com:itWangCode/AI-drug-design.git
```

#### 6. 成功拉取代码

运行命令后，Git 会将代码拉取到本地的文件夹中。如果成功，你将看到类似如下的信息：

```bash
Cloning into 'AI-drug-design'...
```

这时，代码已经拉取成功。

---

### macOS 系统

#### 1. 安装 Git

macOS 上通常已经自带 Git，如果没有，可以通过 Homebrew 安装 Git：

- 打开终端，输入以下命令安装 Homebrew（如果没有安装）：

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- 安装完成后，输入以下命令安装 Git：

```bash
brew install git
```

#### 2. 配置 Git

- 打开终端，输入以下命令配置 Git：

```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

#### 3. 生成 SSH 密钥

- 在终端中输入以下命令生成 SSH 密钥：

```bash
ssh-keygen -t rsa -b 4096 -C "youremail@example.com"
```

- 跟 Windows 一样，按回车使用默认路径存储密钥，设置密码（可选）。

#### 4. 添加 SSH 密钥到 GitHub

- 在终端中使用以下命令查看公钥：

```bash
cat ~/.ssh/id_rsa.pub
```

- 复制输出的公钥，登录 GitHub，将公钥添加到 [GitHub SSH Keys](https://github.com/settings/keys) 页面。

#### 5. 克隆 GitHub 仓库

使用以下命令克隆你的仓库到本地：

```bash
git clone git@github.com:itWangCode/AI-drug-design.git
```

#### 6. 成功拉取代码

Git 会将代码下载到当前目录，表示代码拉取成功。

这样，你就成功配置了 Git 并克隆了代码仓库。



### 二、如何在 Windows 和 macOS 系统上下载和安装 Anaconda-Navigator 并配置你的环境

#### 1. 下载 Anaconda-Navigator

##### Windows：

- 前往 [Anaconda 官方网站](https://www.anaconda.com/products/distribution)。
- 点击下载按钮，选择适合 Windows 系统的版本（通常为 64-bit）。
- 下载完成后，运行安装程序并按照提示完成安装。

##### macOS：

- 同样前往 [Anaconda 官方网站](https://www.anaconda.com/products/distribution)。
- 选择 macOS 系统的版本下载并安装。

安装过程中，建议勾选 "Add Anaconda to my PATH environment variable" 选项，以便在终端中可以直接使用 `conda` 命令。

#### 2. 打开 Anaconda-Navigator

安装完成后：

- 在 Windows 上，可以通过开始菜单找到 Anaconda-Navigator 并运行它。
- 在 macOS 上，可以在 "应用程序" 文件夹中找到 Anaconda-Navigator，点击启动。

#### 3. Git clone 你的仓库

在 Anaconda 环境中进行配置之前，首先需要将你的 GitHub 仓库克隆到本地。

1. 打开终端（macOS）或 Git Bash（Windows）。
2. 运行以下命令，克隆你的仓库：

```bash
git clone git@github.com:itWangCode/AI-drug-design.git
```

这将下载包含 `AIDrugDesign.yml` 文件的仓库到本地。

#### 4. 创建 Conda 环境

进入克隆的项目文件夹，并通过 `.yml` 文件创建新的 Conda 环境：

1. 在终端或 Git Bash 中，切换到你克隆的仓库目录：

```bash
cd AI-drug-design
```

2. 运行以下命令，根据 `AIDrugDesign.yml` 文件创建 Conda 环境：

```bash
conda env create -f AIDrugDesign.yml
```

❤️请您耐心等待15分钟以上，请您连接       ***wifi***        !!!!!!!

3. Conda 将自动根据 `.yml` 文件安装所需的依赖包并创建环境。

#### 5. 列出 Conda 环境

安装完成后，使用以下命令查看所有环境，检查是否创建了 `AI-drug-design` 环境：

```bash
conda env list
```

你应该会看到类似如下的输出，其中包含 `AI-drug-design`：

```bash
# conda environments:
#
base                  *  /path/to/anaconda3
AI-drug-design           /path/to/anaconda3/envs/AI-drug-design
```

#### 6. 激活环境

最后，使用以下命令激活 `AI-drug-design` 环境：

```bash
conda activate AI-drug-design
```

你现在已成功配置并激活了 `AI-drug-design` 环境，可以开始使用该环境进行开发了。

## 安装好所有的配置

### 运行

![15c1411d3a43c97a1c005f046e0ce81b](img/1.png)

![15c1411d3a43c97a1c005f046e0ce81b](img/2.png)

## ☕️☕️☕️能否支持我喝一杯咖啡☕️☕️☕️☕️☕️，谢谢！！让我更有动力，写作💪🏻！！！

<figure class="third">
  <div style="display: flex;align-items: center;justify-content: space-between;">
      <img src="img/qqpay.png" width="350"/>
      <img src="img/wx.jpg"  width="350"/>
  </div>

</figure>




###  三、software

- https://www.jetbrains.com/pycharm/



####  Pycharm 2024.2.1 最新激活码，破解版安装教程（亲测至2099年~）

废话不多说，先上 Pycharm 2024.2.1 版本破解成功的截图，如下，可以看到已经成功破解到 2099 年辣，舒服！

![Pycharm  2024.2.1 版本激活到 2099 年截图](https://img.quanxiaoha.com/quanxiaoha/172533110318555)

###  卸载老版本 Pycharm

接下来，我就将通过图文的方式, 来详细讲解如何激活 Pycharm 2024.2.1 版本至 2099 年。首先，如果小伙伴的电脑上有安装老版本的 Pycharm , 需要将其卸载掉，如下所示（没有安装则不用管，直接安装即可）：

![下载老版本的 Pycharm](https://img.quanxiaoha.com/quanxiaoha/172282014058597)

将**删除缓存和本地历史勾选上**，点击*卸载*按钮开始卸载：

![关闭 Pycharm  卸载弹框](https://img.quanxiaoha.com/quanxiaoha/172282024162978)

卸载完成后，点击*关闭*按钮。

###  下载 Pycharm 安装包

访问 Pycharm 官网：https://www.jetbrains.com/pycharm/download，下载 Pycharm 2024.2.1 版本的安装包。

![下载 Pycharm  2024.2.1 版本安装包](https://img.quanxiaoha.com/quanxiaoha/172533118116545)

###  开始安装

下载完成后，双击 `.exe` 安装包开始安装 Pycharm :

![双击 Pycharm  2024.2.1 安装包](https://img.quanxiaoha.com/quanxiaoha/172282074667784)

点击*下一步*按钮：

![开始安装 Pycharm  2024.2.1 版本](https://img.quanxiaoha.com/quanxiaoha/172282080451067)

**自定义安装路径**，我这里安装在了 `E:\` 盘下，继续点击*下一步*按钮：

![自定义 Pycharm  2024.2.1 版本安装路径](https://img.quanxiaoha.com/quanxiaoha/172282084671682)

进入到**安装选项**的选择，**将下图标注的部分，全部勾选上**，点击*下一步*按钮：

![Pycharm  2024.2.1 安装选项](https://img.quanxiaoha.com/quanxiaoha/172282089279793)

点击*安装*按钮，等待 Pycharm 安装完成：

![等待 Pycharm  2024.2.1 安装完成](https://img.quanxiaoha.com/quanxiaoha/172282099624727)

安装成功后，会弹出如下提示框，一个是立即启动，不要勾选它。我们勾选 “*否，我会在之后重新启动*”，因为需要先破解成功后再启动 Pycharm :

![Pycharm  2024.2.1 安装结束](https://img.quanxiaoha.com/quanxiaoha/172282103297215)

点击*完成*按钮，关闭弹框。

###  下载破解脚本

破解脚本我放置在了网盘中，并提供了多个备用链接，以防下载失效。

> **提示：破解脚本的网盘链接文末获取 ~**
>
> **提示：破解脚本的网盘链接文末获取 ~**
>
> **提示：破解脚本的网盘链接文末获取 ~**

下载成功后，如下，是个压缩包，先对它进行解压：

![JetBrains 全家桶激活脚本](https://img.quanxiaoha.com/quanxiaoha/172264867677452)

###  开始激活

进入到解压后的文件夹 `/win2020-2024(一键激活)` 中，双击 *Pycharm 激活.vbs* ，若提示 `Success!!! Now you can enjoy Pycharm to 2099` , 则表示 Pycharm 激活成功啦 ~

![开始激活 Pycharm](https://img.quanxiaoha.com/quanxiaoha/172282116551955)

###  检查是否激活成功

激活成功后，双击桌面的 Pycharm 快捷启动图标，来打开 Pycharm 。注意，首次安装 Pycharm 可能会弹出如下提示框，勾选 `Do not import settings`, 点击 *OK* 按钮即可：

![img](https://img.quanxiaoha.com/quanxiaoha/172264916211594)

进入 Pycharm 中后，点击菜单栏 *Help | Register...* , 即可查看 Pycharm 的激活到期时间：

![检查 Pycharm  2024.2.1 的到期时间](https://img.quanxiaoha.com/quanxiaoha/172282146863829)

### Pycharm 激活码

EUWT4EE9X2-eyJsaWNlbnNlSWQiOiJFVVdUNEVFOVgyIiwibGljZW5zZWVOYW1lIjoic2lnbnVwIHNjb290ZXIiLCJhc3NpZ25lZU5hbWUiOiIiLCJhc3NpZ25lZUVtYWlsIjoiIiwibGljZW5zZVJlc3RyaWN0aW9uIjoiIiwiY2hlY2tDb25jdXJyZW50VXNlIjpmYWxzZSwicHJvZHVjdHMiOlt7ImNvZGUiOiJQU0kiLCJmYWxsYmFja0RhdGUiOiIyMDI1LTA4LTAxIiwicGFpZFVwVG8iOiIyMDI1LTA4LTAxIiwiZXh0ZW5kZWQiOnRydWV9LHsiY29kZSI6IlBDIiwiZmFsbGJhY2tEYXRlIjoiMjAyNS0wOC0wMSIsInBhaWRVcFRvIjoiMjAyNS0wOC0wMSIsImV4dGVuZGVkIjpmYWxzZX0seyJjb2RlIjoiUFBDIiwiZmFsbGJhY2tEYXRlIjoiMjAyNS0wOC0wMSIsInBhaWRVcFRvIjoiMjAyNS0wOC0wMSIsImV4dGVuZGVkIjp0cnVlfSx7ImNvZGUiOiJQV1MiLCJmYWxsYmFja0RhdGUiOiIyMDI1LTA4LTAxIiwicGFpZFVwVG8iOiIyMDI1LTA4LTAxIiwiZXh0ZW5kZWQiOnRydWV9LHsiY29kZSI6IlBDV01QIiwiZmFsbGJhY2tEYXRlIjoiMjAyNS0wOC0wMSIsInBhaWRVcFRvIjoiMjAyNS0wOC0wMSIsImV4dGVuZGVkIjp0cnVlfV0sIm1ldGFkYXRhIjoiMDEyMDIyMDkwMlBTQU4wMDAwMDUiLCJoYXNoIjoiVFJJQUw6MzUzOTQ0NTE3IiwiZ3JhY2VQZXJpb2REYXlzIjo3LCJhdXRvUHJvbG9uZ2F0ZWQiOmZhbHNlLCJpc0F1dG9Qcm9sb25nYXRlZCI6ZmFsc2V9-FT9l1nyyF9EyNmlelrLP9rGtugZ6sEs3CkYIKqGgSi608LIamge623nLLjI8f6O4EdbCfjJcPXLxklUe1O/5ASO3JnbPFUBYUEebCWZPgPfIdjw7hfA1PsGUdw1SBvh4BEWCMVVJWVtc9ktE+gQ8ldugYjXs0s34xaWjjfolJn2V4f4lnnCv0pikF7Ig/Bsyd/8bsySBJ54Uy9dkEsBUFJzqYSfR7Z/xsrACGFgq96ZsifnAnnOvfGbRX8Q8IIu0zDbNh7smxOwrz2odmL72UaU51A5YaOcPSXRM9uyqCnSp/ENLzkQa/B9RNO+VA7kCsj3MlJWJp5Sotn5spyV+gA==-MIIETDCCAjSgAwIBAgIBDTANBgkqhkiG9w0BAQsFADAYMRYwFAYDVQQDDA1KZXRQcm9maWxlIENBMB4XDTIwMTAxOTA5MDU1M1oXDTIyMTAyMTA5MDU1M1owHzEdMBsGA1UEAwwUcHJvZDJ5LWZyb20tMjAyMDEwMTkwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCUlaUFc1wf+CfY9wzFWEL2euKQ5nswqb57V8QZG7d7RoR6rwYUIXseTOAFq210oMEe++LCjzKDuqwDfsyhgDNTgZBPAaC4vUU2oy+XR+Fq8nBixWIsH668HeOnRK6RRhsr0rJzRB95aZ3EAPzBuQ2qPaNGm17pAX0Rd6MPRgjp75IWwI9eA6aMEdPQEVN7uyOtM5zSsjoj79Lbu1fjShOnQZuJcsV8tqnayeFkNzv2LTOlofU/Tbx502Ro073gGjoeRzNvrynAP03pL486P3KCAyiNPhDs2z8/COMrxRlZW5mfzo0xsK0dQGNH3UoG/9RVwHG4eS8LFpMTR9oetHZBAgMBAAGjgZkwgZYwCQYDVR0TBAIwADAdBgNVHQ4EFgQUJNoRIpb1hUHAk0foMSNM9MCEAv8wSAYDVR0jBEEwP4AUo562SGdCEjZBvW3gubSgUouX8bOhHKQaMBgxFjAUBgNVBAMMDUpldFByb2ZpbGUgQ0GCCQDSbLGDsoN54TATBgNVHSUEDDAKBggrBgEFBQcDATALBgNVHQ8EBAMCBaAwDQYJKoZIhvcNAQELBQADggIBABqRoNGxAQct9dQUFK8xqhiZaYPd30TlmCmSAaGJ0eBpvkVeqA2jGYhAQRqFiAlFC63JKvWvRZO1iRuWCEfUMkdqQ9VQPXziE/BlsOIgrL6RlJfuFcEZ8TK3syIfIGQZNCxYhLLUuet2HE6LJYPQ5c0jH4kDooRpcVZ4rBxNwddpctUO2te9UU5/FjhioZQsPvd92qOTsV+8Cyl2fvNhNKD1Uu9ff5AkVIQn4JU23ozdB/R5oUlebwaTE6WZNBs+TA/qPj+5/we9NH71WRB0hqUoLI2AKKyiPw++FtN4Su1vsdDlrAzDj9ILjpjJKA1ImuVcG329/WTYIKysZ1CWK3zATg9BeCUPAV1pQy8ToXOq+RSYen6winZ2OO93eyHv2Iw5kbn1dqfBw1BuTE29V2FJKicJSu8iEOpfoafwJISXmz1wnnWL3V/0NxTulfWsXugOoLfv0ZIBP1xH9kmf22jjQ2JiHhQZP7ZDsreRrOeIQ/c4yR8IQvMLfC0WKQqrHu5ZzXTH4NO3CwGWSlTY74kE91zXB5mwWAx1jig+UXYc2w4RkVhy0//lOmVya/PEepuuTTI4+UJwC7qbVlh5zfhj8oTNUXgN0AOc+Q0/WFPl1aw5VV/VrO8FCoB15lFVlpKaQ1Yh+DVU8ke+rt9Th0BCHXe0uZOEmH0nOnH/0onD

如下图标注所示，根据日期显示直到 2099 年才会失效，确实是破解成功了：

![Pycharm  2024.2.1 已经成功激活到 2099 年](https://img.quanxiaoha.com/quanxiaoha/172282158688560)

###  激活脚本下载地址

> PS: 激活脚本由于**提取人数过多**，**导致分享的百度网盘链接容易被封**：![Pycharm  2024.2.1 破解补丁分享失败](https://img.chajianxw.com/chajian/164604365771068)蛋疼 ing，为限制人数，目前暂不提供页面直接下载，**改为从笔者公众号下载**。

> 需要的小伙伴，**扫描下方公众号二维码**，或者**关注公众号**： *Python 见习室*，**回复关键字**：*2099*, **即可免费无套路获取激活码、破解补丁，持续更新中 ~。**

![img](https://img.chajianxw.com/chajian/164612710335617)

更多的额操作：请您参考：【https://www.exception.site/article/1762】
