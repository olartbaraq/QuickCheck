from django.db import models

# Create your models here.


class News(models.Model):
    """this class represents the table for the synced news

    Args:
        models (_type_): _description_
    """
    
    news_number = models.PositiveIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.news_number}"
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'News'