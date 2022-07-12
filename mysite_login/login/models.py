from django.db import models


class User(models.Model):
    '''用户表'''

    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)
    match_status_choices = (
        (1, "允许匹配"),
        (2, "暂时不允许匹配"),
        (3, "匹配成功"),
    )
    match_status = models.SmallIntegerField(verbose_name="匹配状态", choices=match_status_choices, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Test1(models.Model):
    user = models.ForeignKey(User, related_name="User_id", on_delete=models.CASCADE, default=4)
    Q1_choices = (
        (1, "A"),
        (2, "B"),
        (3, "C"),
        (4, "D"),
    )
    Q1 = models.SmallIntegerField(verbose_name="问题1", choices=Q1_choices, default=1)
    Q2_choices = (
        (1, "A"),
        (2, "B"),
        (3, "C"),
        (4, "D"),
    )
    Q2 = models.SmallIntegerField(verbose_name="问题2", choices=Q2_choices, default=1)
    Q3_choices = (
        (1, "A"),
        (2, "B"),
        (3, "C"),
        (4, "D"),
    )
    Q3 = models.SmallIntegerField(verbose_name="问题1", choices=Q3_choices, default=1)


class love(models.Model):
    user_receive = models.SmallIntegerField(verbose_name="收到喜欢", default=1)
    user_deliver = models.SmallIntegerField(verbose_name="提出喜欢", default=1)
