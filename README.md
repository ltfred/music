###  A simple music website based on Django
- The song information is obtained by the spider, and the database information has been exported to a SQL file, which can be downloaded and used as needed.

### Run
- Installation Environment

 ```pip install -r requirement```
 
- Create database

```create database wusun_music charset=utf8;```

- Migrate

```python manage.py migrate```

- Import data

 ```mysql -u<username> -p<password> < music_info.sql```
