from django.db import models

DEPARTMENT_TYPES = (
    ('OFFICE', 'Офис'),
    ('STOCKROOM', 'Склад'),
    ('CONVEYOR', 'Конвейер'),
    ('WORKSHOP', 'цех'),
)

JOBS = (
    ('BOSS', 'Директор'),
    ('CHiEF', 'Начальник'),
    ('MANAGER', 'Менеджер'),
    ('SPECIALIST', 'Специалист'),
    ('EXPERT', 'Эксперт'),
    ('INTERN', 'Стажёр'),
)


class Department(models.Model):
    name = models.fields.CharField(
        max_length=100,
        verbose_name='Название',
    )
    type = models.fields.CharField(
        max_length=50,
        choices=DEPARTMENT_TYPES,
        default='OFFICE',
        verbose_name='Тип',
    )
    head_department = models.ForeignKey(
        'Department',
        on_delete=models.SET_NULL,
        null=True,
        related_name='subordinate_department',
        verbose_name='Головной отдел',
    )

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Employee(models.Model):
    last_name = models.fields.CharField(
        max_length=50,
        verbose_name='Фамилия',
    )
    first_name = models.fields.CharField(
        max_length=50,
        verbose_name='Имя',
    )
    middle_name = models.fields.CharField(
        max_length=50,
        verbose_name='Отчество',
    )
    birth_date = models.fields.DateField(
        verbose_name='Дата рождения',
    )
    birth_place = models.fields.CharField(
        max_length=50,
        verbose_name='Место рождения',
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Job(models.Model):
    title = models.fields.CharField(
        max_length=50,
        choices=JOBS,
        verbose_name='Должность',
    )
    hire_date = models.fields.DateField(
        verbose_name='Дата устройства',
    )
    dismiss_date = models.fields.DateField(
        null=True,
        verbose_name='Дата увольнения',
    )
    salary = models.fields.PositiveIntegerField(
        verbose_name='Оклад',
    )
    bonus = models.fields.PositiveIntegerField(
        verbose_name='Премия %'
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='jobs',
        verbose_name='Сотрудник',
    )
    chief = models.ForeignKey(
        Employee,
        null=True,
        on_delete=models.SET_NULL,
        related_name='subordinate_employees',
        verbose_name='Начальник',
    )
    department = models.ForeignKey(
        Department,
        null=True,
        on_delete=models.SET_NULL,
        related_name='employees',
        verbose_name='Отдел',
    )

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Sale(models.Model):
    date = models.fields.DateField(
        verbose_name='Дата'
    )
    amount = models.fields.PositiveIntegerField(
        verbose_name='Сумма'
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='sales',
        verbose_name='Продавец',
    )

    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'
