from django.db import models

STATUS_CHOICES = (
    ('active', 'ACTIVE'),
    ('pending', 'PENDING'),
    ('inactive', 'INACTIVE'),
    ('deleted', 'DELETED'),
)



TITLE_CHOICES = (
    ('executive', 'EXECUTIVE'),
    ('manager', 'MANAGER'),
    ('employees', 'EMPLOYEES'),
)


class Employee(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(choices=TITLE_CHOICES, default='EMPLOYEES', max_length=100)
    fullname = models.CharField(max_length=255, default='')
    status = models.CharField(choices=STATUS_CHOICES, default='ACTIVE', max_length=100)
    salary = models.FloatField(max_length=25, default=0)
    alerts = models.IntegerField( default=0)
    address = models.TextField()

    class Meta:
        ordering = ('created',)


class Department(models.Model):
    name = models.CharField(max_length=255, default='')
    employees = models.ManyToManyField(Employee)

    class Meta:
        ordering = ('name',)


class Store(models.Model):
    name = models.CharField(max_length=255, default='')
    address = models.TextField()
    departments = models.ManyToManyField(Department)

    class Meta:
        ordering = ('name',)
