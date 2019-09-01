###  一个基于Django的简单音乐网站
- 歌曲信息通过爬虫获取，数据库信息已经导出成SQL文件，可根据需要下载使用。

### 运行
- 安装环境

 ```pip install -r requirement```
 
- 创建数据库

```create database wusun_music charset=utf8;```

- 迁移

```python manage.py migrate```

- 导入数据

 ```mysql -u<用户名> -p<密码> < music_info.sql```
