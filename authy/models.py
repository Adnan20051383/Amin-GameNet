from django.db import models
from django.db.models.signals import post_save


class Table(models.Model):
    number = models.IntegerField()
    is_reserved = models.BooleanField(default=False)


class Reserve(models.Model):
    reserver = models.TextField(null=True, blank=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    players_num = models.IntegerField(null=True, blank=True)
    reserve_time = models.DateTimeField(auto_now_add=True)
    is_ended = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    reserve_end_time = models.DateTimeField(null=True, blank=True)

    def show_price(self):
        return "{:,}".format(self.price)

    def reserve_table(sender, instance, *args, **kwargs):
        reserve = instance
        table = reserve.table
        Table.objects.filter(number=table.number).update(is_reserved=True)


class playMode(models.Model):
    players_num = models.IntegerField(null=True, blank=True)
    price = models.TextField(null=True, blank=True)


class Snack(models.Model):
    name = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)

    def show_price(self):
        return "{:,}".format(self.price)


class SnackOnReserve(models.Model):
    reserve = models.ForeignKey(Reserve, on_delete=models.CASCADE)
    snack = models.ForeignKey(Snack, on_delete=models.CASCADE)


post_save.connect(Reserve.reserve_table, sender=Reserve)
