from django.db.models import Model, CharField, DateTimeField, IntegerField


class Movie(Model):
    name = CharField(max_length=255, blank=True, null=True, verbose_name="Název filmu")
    rate = IntegerField(blank=True, null=True, verbose_name="Hodnocení")
    added_at = DateTimeField(auto_now_add=True, verbose_name="Čas vložení")

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return f"{self.name} - {self.rate}"
