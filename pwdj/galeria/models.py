from django.db import models


class Categoria(models.Model):
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo


class Model(models.Model):
    class Meta:
        ordering = 'categoria ultima_alteracao'.split()

    titulo = models.CharField(max_length=50)
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    descricao = models.TextField()
    foto = models.ImageField(max_length=200, upload_to='galeria/', null=True)
    categoria = models.ForeignKey(Categoria, models.SET_NULL, null=True)
    criacao = models.DateField(auto_now_add=True)
    ultima_alteracao = models.DateField(auto_now=True)

    def __str__(self):
        return self.titulo

    def __repr__(self):
        return f'Model(titulo={self.titulo!r}, preco={self.preco!r}, descricao={self.descricao!r})'
