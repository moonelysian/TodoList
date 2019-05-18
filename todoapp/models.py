from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    priority = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    due = models.DateField(blank=True, null=True)
    check = models.BooleanField(default=False)
   
    def __str__(self):
        return self.title
    
    def summery(self):
        return self.content[:100]
    
