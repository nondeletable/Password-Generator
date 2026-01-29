<div align="center">
  <a href="https://github.com/nondeletable/ComfyLauncher">
    <img src="promo/pwd_gen_icon.webp" alt="Logo" width="100" height="100">
  </a>
<h2>Password Generator</h2>
<p>A clean, offline desktop app for generating strong passwords - fast, configurable, and privacy-first.</p>
  <p>
    <a href="https://github.com/nondeletable/Password-Generator/tree/master/README/README-PG-EN.md">English </a> |  
    <a href="https://github.com/nondeletable/Password-Generator/tree/master/README/README-PG-DE.md">Deutsch </a> |
    <a href="https://github.com/nondeletable/Password-Generator/tree/master/README/README-PG-CN.md">简体中文 </a> | 
    <a href="https://github.com/nondeletable/Password-Generator/tree/master/README/README-PG-NV.md">Tiếng Việt </a> | 
    <a href="https://github.com/nondeletable/Password-Generator/tree/master/README/README-PG-Ru.md">Русский </a>
    <br>
    <br>
    <img src="promo/pwd_gen_1.png" alt="Password Generator by nondeletable" width="98%"/>
    <br>
    <br>
  </p>
</div>

## 🔐 这个应用做什么

- **离线**生成强密码（无遥测、无追踪）。
- 提供可直接使用的**策略**（Standard / Admin / NIST）。
- 通过**自动隐藏**与**自动清理剪贴板**降低复制/粘贴带来的风险。
- 按你的需求生成密码（长度、符号、数字等）。
- 简单省心：可携带的 ".exe"，极简界面，快速工作流。
&nbsp;
&nbsp;

## 🎨 功能特点

- 使用 Python `secrets` 进行加密级安全生成（不是 `random`）。
- 可自定义字符集：字母 / 数字 / 符号。
- 保证包含：从每个已选类别中至少包含 1 个字符。
- 密码强度指示（弱 / 一般 / 强）。
- **自动隐藏**：显示后的密码在 **10 秒**后自动隐藏。
- **剪贴板保护**：复制后 **30 秒**自动清空剪贴板。
- 一键复制。
- 内置**密码策略**：
  - **Standard** - 平衡复杂度
  - **Admin** - 面向高权限账号的更严格规则
  - **NIST** - 参考 NIST SP 800-63B（更长、更易用、更安全）
&nbsp;
&nbsp;

## 😎 隐私与安全

- ✅ **完全离线**运行。
- ✅ 无账号、无分析、无遥测。
- ✅ 不会向任何地方发送数据。
- ✅ 剪贴板自动清理可减少意外泄露。
&nbsp;
&nbsp;

## ⚒ 安装

- 打开 **Releases** 并下载最新的 ".exe"。
- 解压到任意位置（桌面、工具文件夹、U 盘）。
- 运行 "Password Generator.exe"。
&nbsp;
&nbsp;

## 🏓 使用方法

1. 选择一个策略（**Mode**），或自定义规则。
2. 开启/关闭符号与数字，并设置密码长度。
3. 点击 **Generate**。
4. 点击 **Copy** —— 剪贴板会在 30 秒后自动清空。

<p align="center">
  <img src="promo/pwd_gen.png" alt="Main window" width="60%"/>
</p>
&nbsp;
&nbsp;

## 💾 技术栈

- Python 3.13
- Flet（UI）
- pytest（测试）
- ruff、black、pre-commit（代码质量）
- PyInstaller（Windows 构建）
&nbsp;
&nbsp;

## ✅ 质量

- 测试覆盖率：**91%**
- Releases：**4**（总版本数：**6**）
- Windows 构建大小：约 **83 MB**
&nbsp;
&nbsp;

## ☎ 支持与联系

如需合作或讨论工作机会，请使用下方任一联系方式。
如需支持/反馈 Bug，建议使用 Discord 或 GitHub Issues。我通常会在 24 小时内回复。

- 🐙 **GitHub**（文档、发布、源码）  
  https://github.com/nondeletable
- 💬 **Discord** - 新闻、支持、提问与 Bug 反馈  
  https://discord.com/invite/6nvXwXp78u
- ✈️ **Telegram** - 私信  
  https://t.me/nondeletable
- 📧 **Email** - 商务/正式联系  
  nondeletable@gmail.com
- 💼 **LinkedIn** - 职业主页  
  https://www.linkedin.com/in/aleksandra-gicheva-3b0264341/
- ☕ **Boosty** - 捐助支持我的项目  
  https://boosty.to/codebird/donate  
&nbsp;
&nbsp;

感谢使用 Password Generator！祝你拥有强密码，以及真正属于你的隐私。🔐✨🙂
