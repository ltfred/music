from django.db import models


# Create your models here.
class Music(models.Model):

    id = models.AutoField(max_length=11, db_column='music_id', primary_key=True)
    name = models.CharField(max_length=255, db_column='music_name', blank=False)
    singer = models.CharField(max_length=255, db_column='singer', blank=False)
    came_from = models.CharField(max_length=255, db_column='came_from', blank=True)
    kbps = models.CharField(max_length=255, db_column='music_kbps', blank=True)
    size = models.CharField(max_length=255, db_column='music_size', blank=True)
    language = models.CharField(max_length=255, db_column='music_language', blank=True)
    released_data = models.CharField(max_length=255, db_column='released_data', blank=True)
    url = models.CharField(max_length=255, db_column='bdyun_url', blank=False)
    password = models.CharField(max_length=255, db_column='bdyun_password', blank=True)

    class Meta:
        db_table = 'music_info'  # 表名

    def __str__(self):
        return self.name