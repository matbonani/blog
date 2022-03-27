from django.db import models

from django.contrib.auth.models import User


class Base(models.Model):
    criacao = models.DateField('Criação', auto_now_add=True)
    atualizacao = models.DateField('Atualização', auto_now='True')

    class Meta:
        abstract = True


class Post(Base):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(User, default=User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)
