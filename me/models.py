from django.db import models

class AboutMe(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/',blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    choice_language = [
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript'),
        ('Java', 'Java'),
        ('C++', 'C++'),
        ('Ruby', 'Ruby'),
        ('Go', 'Go'),
        ('PHP', 'PHP'),
        ('C#', 'C#'),
        ("HTML/CSS", "HTML/CSS"),
        ('Other', 'Other'),

    ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    image = models.FileField(upload_to='project_images/')
    language = models.CharField(max_length=50, choices=choice_language, default='Python')


    

    def __str__(self):
        return self.name


from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_sent_to_telegram = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.email}"




