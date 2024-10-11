from django.contrib import admin

from authy.models import Table, Reserve, playMode, Snack, SnackOnReserve


class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'is_reserved')


class ReserveAdmin(TableAdmin):
    list_display = ('reserver', 'table', 'reserve_time')


class PlayModeAdmin(admin.ModelAdmin):
    list_display = ('players_num', 'price')


class SnackAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class SnackOnReserveAdmin(SnackAdmin):
    list_display = ('reserve', 'snack')


admin.site.register(SnackOnReserve, SnackOnReserveAdmin)
admin.site.register(Snack, SnackAdmin)
admin.site.register(playMode, PlayModeAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Reserve, ReserveAdmin)
