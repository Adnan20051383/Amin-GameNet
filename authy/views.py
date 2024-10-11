from datetime import datetime
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from authy.forms import ReservationForm
from authy.models import Table, Reserve, playMode, Snack, SnackOnReserve


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def reserve_page(request):
    reserved_tables = Reserve.objects.filter(is_ended=False)
    not_reserved_tables = Table.objects.filter(is_reserved=False)
    context = {
        'reserved_tables': reserved_tables,
        'not_reserved_tables': not_reserved_tables,
    }
    return render(request, 'reserve.html', context)


@login_required
def reserve_form(request, table_number):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.table = Table.objects.get(number=table_number)
            reservation.save()
            return redirect('reserve')
        else:
            print(form.errors)
            form = ReservationForm()
            return render(request, 'reserve_form.html', {'form': form})
    else:
        form = ReservationForm(initial={'table_number': table_number})
        return render(request, 'reserve_form.html', {'table_number': table_number, 'form': form})


@login_required
def release_form(request, reserve_id):
    reserve = Reserve.objects.get(id=reserve_id)
    table = reserve.table
    snacks = SnackOnReserve.objects.filter(reserve=reserve)
    sum = 0
    for snack in snacks:
        sum += float(snack.snack.price)
    price = round(calculate_price(time_difference(reserve.reserve_time), reserve.players_num), 0) + round(sum, 0)
    price_str = format_number_with_commas(price)
    if request.method == 'POST':
        Reserve.objects.filter(id=reserve_id).update(is_ended=True, price=price, reserve_end_time=timezone.now())
        Table.objects.filter(number=table.number).update(is_reserved=False)
        return redirect('reserve')
    else:
        context = {'reserve': reserve,
                   'price': price_str
        }
        return render(request, 'release_form.html', context)


def calculate_price(time, num_of_players):
    playModePrice = playMode.objects.get(players_num=num_of_players)
    return time * int(playModePrice.price)


def time_difference(time):
    if not isinstance(time, datetime):
        raise ValueError("The provided time must be a datetime object.")
    current_time = timezone.now()
    time_diff = (current_time - time).total_seconds()
    time_diff_in_hours = time_diff / 3600
    return round(time_diff_in_hours, 2)


def format_number_with_commas(number):
    return "{:,}".format(number)


def history(request):
    reserves = Reserve.objects.filter(is_ended=True).order_by('-id')
    return render(request, 'history.html', {'reserves': reserves})


def add_snack(request, reserve_id):
    reserve = Reserve.objects.get(id=reserve_id)
    snacks = Snack.objects.all().order_by('-id')
    snacks_on_reserve_nums = []
    for snack in snacks:
        snacks_on_reserve_nums.append(SnackOnReserve.objects.filter(reserve=reserve, snack=snack).count())
    zipped_lists = zip(snacks, snacks_on_reserve_nums)
    context = {
        'zipped_lists': zipped_lists,
        'reserve': reserve,
    }
    return render(request, 'snack-list.html', context)


def snackAdd(request, snack_id, reserve_id):
    snack = Snack.objects.get(id=snack_id)
    reserve = Reserve.objects.get(id=reserve_id)
    snackAdded = SnackOnReserve(snack=snack, reserve=reserve)
    snackAdded.save()
    return redirect('add-snack', reserve_id=reserve_id)


def snackDelete(request, snack_id, reserve_id):
    snack = Snack.objects.get(id=snack_id)
    reserve = Reserve.objects.get(id=reserve_id)
    snackDeleted = SnackOnReserve.objects.filter(snack=snack, reserve=reserve)[0]
    snackDeleted.delete()
    return redirect('add-snack', reserve_id=reserve_id)
