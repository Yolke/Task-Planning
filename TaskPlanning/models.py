from django.db import models

class Task(models.Model):
    # Définition des status avec les tuples appropriés
    STATUS_CHOICES = [
        ('todo', 'À faire'),
        ('in_progress', 'En cours'),
        ('completed', 'Terminé'),
    ]

    name = models.CharField(max_length=35)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    creating_date = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        return self.name
