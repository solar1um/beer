from django.shortcuts import render
import random
from beer.forms import GenForm
from beer.models import Generation


rand_prip = [
    'strelok',
    'cTaTucT',
    'TaHkucT',
    'CTpeJLok',
    'demon',
    'Mr',
    'TAHC',
    'TAHK',
    'VIP',
    'Joker',
    'Top4ik',
    'MAHb9K',
    'DNO',
    'SPARTAK',
    'CSKA',
    '3EHUT',
    'mega',
    'MEGA',
    'Black',
    'LOX',
    'Crazy',
    'bondit',
    'ZM',
    '57',
    'BAIKE',
    'BMW',
    'NSDAP',
    'KPSS',
    'VKPM',
    'VKPB',
    'CCCP',
    'kyrgyz',
    'menen',
    'CTapuk',
    'Ded',
    'Big',
    'FIFA',
    'WoT',
    'LGBT',
    'BLM',
    'NS',
    'Eby_BCEX',
    'Ha_KoJlenu',
    '50kg',
    'FAT',
    'monik',
    'chik',
    'rus',
    'shinomontaj',
    'koala',
    'Ha_Paccjlabone',
    'B_TANKE',
    'FOOTBOLL',
    'bOPEC',
    ''


]

dictionary = {
        ' ': ' ',
        '.': '.',
        'a': 'a',
        'A': 'a',
        'b': 'b',
        'B': 'b',
        'c': 'c',
        'C': 'c',
        'D': 'D',
        'd': 'D',
        'E': 'E',
        'e': 'e',
        'F': 'F',
        'f': 'F',
        'G': 'r',
        'g': 'r',
        'H': 'X',
        'h': 'X',
        'I': 'U',
        'i': 'u',
        'J': 'JlL',
        'j': 'JlL',
        'K': 'K',
        'k': 'k',
        'L': 'JL',
        'l': 'JL',
        'M': 'M',
        'm': 'm',
        'N': 'H',
        'n': 'H',
        'O': 'O',
        'o': 'o',
        'P': 'n',
        'p': 'n',
        'Q': 'Ky',
        'q': 'Ky',
        'R': 'P',
        'r': 'p',
        'S': 'C',
        's': 'c',
        't': 'T',
        'T': 'T',
        'U': 'Y',
        'u': 'y',
        'V': 'B',
        'v': 'B',
        'W': 'B',
        'w': 'B',
        'X': 'X',
        'x': 'x',
        'Y': 'Y',
        'y': 'y',
        'Z': '3',
        'z': '3',
        '?': '?'

    }


def generation(request):

    if request.method == 'POST':
        form = GenForm(request.POST)
        if form.is_valid():
            form.save()

    name = Generation.objects.all().values_list('name', flat=True).last()
    form = GenForm

    res = []
    for i in name:
        res.append(dictionary[i])
    res = ''.join(res)
    if random.getrandbits(2) == 1:
        name = f'{random.choice(rand_prip)}_{res}_{str(random.randrange(1958, 1993))}'
    elif random.getrandbits(2) == 2:
        name = f'{str(random.randrange(1958, 1993))}_{ res }_{random.choice(rand_prip)}'
    else:
        name = f'{str(random.randrange(1958, 1993))}_{res}_{random.choice(rand_prip)}__'
    context = {
        'name': name,
        'form': form
    }
    return render(request, 'index.html', context)
