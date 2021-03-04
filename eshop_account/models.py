from django.db import models


class Favorite(models.Model):
    favorite_product = models.IntegerField(blank=True, null=True)
    current_user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "علاقه مندی"
        verbose_name_plural = "علاقه مندی ها"
