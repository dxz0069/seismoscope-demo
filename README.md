# 候风 Seismoscope 演示仓库

Fork 本仓库 → Actions 自动运行候风安全审查 → **Security 标签页** 查看告警（约 1 分钟）。

[app.py](app.py) 故意包含 5 类典型 vibe-coding 漏洞：硬编码密钥、反射型 XSS、SQL 注入、命令注入、IDOR。

审查工具：[候风 Seismoscope](https://github.com/dxz0069/seismoscope) —— `pip install seismoscope`
