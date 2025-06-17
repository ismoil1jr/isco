from django.db import models



class About(models.Model):
    image = models.ImageField(upload_to='About_img/')
    text = models.TextField()

    @property
    def imageURL(self):
        if self.image:
            return self.image.url
        else:
            return None


class Project(models.Model):
    image = models.ImageField('Project_img/')
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=100)
    url = models.URLField()

    @property
    def imageURL(self):
        if self.image:
            return self.image.url
        return ''


class VisitorInfo(models.Model):
    ip_address = models.GenericIPAddressField()
    mac_address = models.CharField(max_length=50, blank=True, null=True)  # MAC olish ko'proq advanced ish
    user_agent = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} | {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"



















