from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class MenuList(models.Model):
    module_name = models.CharField(max_length=100, db_index=True)
    menu_name = models.CharField(max_length=100, unique=True, db_index=True)
    menu_url = models.CharField(max_length=100, db_index=True, unique=True)
    menu_icon = models.CharField(max_length=100, db_index=True)
    parent_id = models.IntegerField(db_index=True, default=0)
    is_main_menu = models.BooleanField(default=False)
    is_sub_menu = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, db_index=True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'menu_list'
        verbose_name = 'Menu List'

    def __str__(self):
        return self.menu_name


class UserPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='permissions')
    menu = models.ForeignKey(MenuList, on_delete=models.CASCADE, related_name='permissions')
    can_view = models.BooleanField(default=False)
    can_add = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, db_index=True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_permission'
        verbose_name = 'User Permission'

    def __str__(self):
        return f"{self.user.username} - {self.menu.menu_name}"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_by = models.CharField(max_length=100, db_index=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            self.slug = base_slug

            counter = 1
            while Category.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    author = models.CharField(max_length=100, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    class Meta:
        db_table = 'post'
        verbose_name = 'Post'

    def __str__(self):
        return self.title  