from django.db import models


class Cabinet(models.Model):
    user = models.OneToOneField('auth.User', related_name='cabinet')
    width = models.IntegerField()
    height = models.IntegerField()
    color = models.CharField(max_length=20)
    added = models.DateField(auto_now_add=True)
    floor = models.IntegerField()

    def __unicode__(self):
        return u'%s cabinet at %d floor' % (self.color.title(), self.floor)


class Folder(models.Model):
    cabinet = models.ForeignKey('Cabinet', related_name='folders')
    name = models.CharField(max_length=20)
    secrecy = models.IntegerField()

    def __unicode__(self):
        return u'Folder: %s' % (self.name)


class File(models.Model):
    folder = models.ForeignKey('Folder', related_name='files')
    type = models.ForeignKey('FileType', related_name='files')
    archive_num = models.CharField(max_length=20)
    content = models.TextField()

    def __unicode__(self):
        return u'%s %s' % (self.type.type, self.content[:30])

class FileType(models.Model):
    type = models.CharField(max_length=20)

    def __unicode__(self):
        return u'File type %s' % (self.type)
