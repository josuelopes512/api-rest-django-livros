from django.db.models.signals import pre_save
from django.utils.text import slugify
from isbn_field import ISBNField
from django.urls import reverse
from uuid import uuid4
from django.db.models import (
    Model,
    UUIDField,
    SlugField,
    CharField,
    DateField,
    PositiveIntegerField,
    ImageField,
    FileField,
    DateTimeField
)
# Create your models here.

OPTIONS = (
    ("1", "Ativo"), 
    ("2", "Não Ativo")
)
T = True


class Livro(Model):
    id_livro = UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, default='None')
    autor = CharField(max_length=255)
    isbn = ISBNField(clean_isbn=False)
    data_de_lancamento = DateField()
    estado = CharField(max_length=6, choices = OPTIONS, default='Ativo')
    paginas = PositiveIntegerField(null=True)
    empresa_publicadora = CharField(max_length=255)
    capa = ImageField(upload_to='capas', null=True)
    pdf = FileField(upload_to='pdfs', null=True)
    create_at = DateField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.titulo

    def get_absolute_url(self):
        return reverse("cadastro_livros:detail", kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ("-create_at",)


def create_slug(instance, new_slug=None):
    slug = slugify(instance.titulo)
    if new_slug is not None:
        slug = new_slug
    qs = Livro.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Livro)