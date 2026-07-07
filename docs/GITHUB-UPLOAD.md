# 今天上传 iBrain 到 GitHub

## 第 1 步：在 GitHub 网页创建仓库

1. 打开 https://github.com/new
2. Repository name: `iBrain`
3. Description: `Scenario-based AI memory for students, built on GBrain`
4. 选 Public 或 Private
5. **不要**勾选 "Add a README"（本地已有）
6. 点 Create repository

## 第 2 步：在终端上传

```bash
cd ~/Documents/iBrain
git init
git add .
git commit -m "feat: add student study-coach skill and project docs"
git branch -M main
git remote add origin https://github.com/你的用户名/iBrain.git
git push -u origin main
```

把 `你的用户名` 换成你的 GitHub 用户名。

## 第 3 步：验证

刷新 GitHub 仓库页面，应看到：

- README.md（项目介绍）
- skillpacks/student/skills/study-coach/SKILL.md
- ROADMAP.md
- docs/

## 常见问题

**push 时要登录？**  
用 GitHub Personal Access Token 作为密码，或配置 SSH key。

**remote 已存在？**  
```bash
git remote set-url origin https://github.com/你的用户名/iBrain.git
```
