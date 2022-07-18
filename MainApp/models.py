from django.db import models
from tinymce.models import HTMLField
from PIL import Image
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from django.urls import reverse_lazy

# Create your models here.

HISTORY_TYPE = (
    ('WORLD_HISTORY', 'WORLD_HISTORY'),
    ('ANCIENT', 'ANCIENT'),
    ('MIDDLE', 'MIDDLE'),
    ('MODERN', 'MODERN'),
    ('INDIA_AFTER_FREEDOM', 'INDIA_AFTER_FREEDOM')
)


class Common(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    post = HTMLField()
    viewcounter = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class HistoricalPlaceModel(Common):
    image = models.ImageField(upload_to='image/historical', null=True)

    class Meta:
        verbose_name_plural = 'HistoricalPlaceModel'
        ordering = ['-timestamp']

    def save(self, *args, **kwargs):
        im = Image.open(self.image)
        output = BytesIO()
        im = im.resize((275, 183))
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        self.image = InMemoryUploadedFile(output, 'ImageFiled', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',

                                          sys.getsizeof(output), None)
        return super(HistoricalPlaceModel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('ADBH:historicalplacesdetail', kwargs={'slug': self.slug})


class IndianHistoryModel(Common):
    type = models.CharField(choices=HISTORY_TYPE, max_length=100, default='ANCIENT')

    class Meta:
        verbose_name_plural = 'IndianHistoryModel'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return reverse_lazy('ADBH:indianhistorydetail', kwargs={'slug': self.slug})


class CurrentIndianModel(Common):
    class Meta:
        verbose_name_plural = 'CurrentIndianModel'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return reverse_lazy('ADBH:currentindiadetail', kwargs={'slug': self.slug})


class FreedomFighterModel(Common):
    image = models.ImageField(upload_to='image/freedom', null=True)

    class Meta:
        verbose_name_plural = 'FreedomFighterModel'
        ordering = ['-timestamp']

    def save(self, *args, **kwargs):
        im = Image.open(self.image)
        output = BytesIO()
        im = im.resize((275, 183))
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        self.image = InMemoryUploadedFile(output, 'ImageFiled', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output), None)
        return super(FreedomFighterModel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('ADBH:freedomfighterdetail', kwargs={'slug': self.slug})


class FactBlogModel(Common):
    image = models.ImageField(upload_to='image/fact', null=True)

    class Meta:
        verbose_name_plural = 'FactBlogModel'
        ordering = ['-timestamp']

    def save(self, *args, **kwargs):
        im = Image.open(self.image)
        output = BytesIO()
        im = im.resize((275, 183))
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        self.image = InMemoryUploadedFile(output, 'ImageFiled', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output), None)
        return super(FactBlogModel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('ADBH:factblogdetail', kwargs={'slug': self.slug})


class CustomAndTraditionModel(Common):
    image = models.ImageField(upload_to='image/tradition', null=True)

    class Meta:
        verbose_name_plural = 'CustomandTraditionModel'
        ordering = ['-timestamp']

    def save(self, *args, **kwargs):
        im = Image.open(self.image)
        output = BytesIO()
        im = im.resize((275, 183))
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        self.image = InMemoryUploadedFile(output, 'ImageFiled', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output), None)
        return super(CustomAndTraditionModel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('ADBH:customandtraditiondetail', kwargs={'slug': self.slug})


class Comments(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'Commented by {self.name}'


class HistoricalPlaceComments(Comments):
    post = models.ForeignKey(HistoricalPlaceModel, on_delete=models.CASCADE, related_name='historicalplacecomments')

    class Meta:
        verbose_name_plural = 'HistoricalPlaceComments'


class IndianHistoryComments(Comments):
    post = models.ForeignKey(IndianHistoryModel, on_delete=models.CASCADE, related_name='indianhistorycomments')

    class Meta:
        verbose_name_plural = 'IndianHistroyComments'


class CurrentIndiaComments(Comments):
    post = models.ForeignKey(CurrentIndianModel, on_delete=models.CASCADE, related_name='currentindiacomments')

    class Meta:
        verbose_name_plural = 'CurrentIndiaComments'


class FreedomFighterComments(Comments):
    post = models.ForeignKey(FreedomFighterModel, on_delete=models.CASCADE, related_name='freedomfightercomments')

    class Meta:
        verbose_name_plural = 'FreedomFighterComments'


class FactBlogComments(Comments):
    post = models.ForeignKey(FactBlogModel, on_delete=models.CASCADE, related_name='factblogcomments')

    class Meta:
        verbose_name_plural = 'FactBlogComments'


class CustomAndTraditionComments(Comments):
    post = models.ForeignKey(CustomAndTraditionModel, on_delete=models.CASCADE,
                             related_name='customandtraditioncomments')

    class Meta:
        verbose_name_plural = 'CustomAndTraditionComments'


class SlideImage(models.Model):
    image = models.ImageField(upload_to='slide/image')
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    link = models.URLField()

    def save(self, *args, **kwargs):
        im = Image.open(self.image)
        output = BytesIO()
        im = im.resize((1280, 500))
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        self.image = InMemoryUploadedFile(output, 'ImageFiled', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output), None)
        return super(SlideImage, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
