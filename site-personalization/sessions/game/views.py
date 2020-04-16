import random

from django.shortcuts import render
from .models import Player, Game, PlayerGameInfo
from .forms import GameForm, Player2Form


def show_home(request):
    game_id = request.session.get('game_id', 0)
    player_id = request.session.get('player_id', 0)
    if player_id:
        player = Player.objects.get(id=player_id)
    else:
        player = Player.objects.create()
        request.session['player_id'] = player.id
    if not game_id:


        game = Game.objects.last()

        if not game or game and game.is_finished:
            # create new game player 1
            context = {
                'player': 1,
                'start_game': True,
                'form': GameForm,
            }
            game = Game.objects.create()
            game.players.add(player)
            game.save()
            pgi = PlayerGameInfo.objects.get(player=player, game=game)
            pgi.is_author = True
            pgi.save()
        else:
            # start game player2
            context = {
                'player': 2,
                'start_game': True,
                'form': Player2Form,
                'min': game.min_value,
                'max': game.max_value,
            }
            game.players.add(player)
            game.save()
        request.session['game_id'] = game.id

    else:
        # game has already started
        game = Game.objects.get(id=game_id)
        pgi = PlayerGameInfo.objects.get(player=player, game=game)

        if request.method == 'POST':

            if pgi.is_author:
                # initialization of the game
                form = GameForm(request.POST)
                if form.is_valid():
                    form.clean()
                    game.min_value = form.cleaned_data.get('min_value')
                    game.max_value = form.cleaned_data.get('max_value')
                    game.game_value = random.randint(game.min_value, game.max_value)
                    game.save()
                    context = {
                        'player': 1,
                        'start_game': False,
                        'text': f'Ваше число {game.game_value}',
                    }
                else:
                    context = {
                        'player': 1,
                        'start_game': True,
                        'form': form,
                    }
            else:
                # guess attempt
                form = Player2Form(request.POST)
                if form.is_valid():
                    pgi.attempts += 1
                    pgi.save()
                    context = {
                        'player': 2,
                        'start_game': False,
                        'end_game': False,
                        'form': Player2Form,
                        'min': game.min_value,
                        'max': game.max_value
                    }
                    attempt = form.cleaned_data.get('attempt')
                    request.session['attempt'] = attempt
                    game_value = game.game_value
                    if attempt > game_value:
                        context['text'] = f'Загаданное число меньше {attempt}'
                    elif attempt < game_value:
                        context['text'] = f'Загаданное число больше {attempt}'
                    else:
                        context['end_game'] = True
                        game.is_finished = True
                        game.save()
                        context['text'] = f'Вы угадали! Загаданное число {attempt}. Вам понадобилось {pgi.attempts} попыток'
                        request.session['game_id'] = 0
                        pgi_author = PlayerGameInfo.objects.get(game=game, is_author=True)
                        pgi_author.attempts = pgi.attempts
                        pgi_author.save()
        else:
            if pgi.is_author:
            # player1 wait or get result
                if game.is_finished:
                    context = {
                        'player': 1,
                        'start_game': False,
                        'end_game': True,
                        'text': f'Ваше число угадали за {pgi.attempts} попыток'
                    }
                    request.session['game_id'] = 0
                else:
                    context = {
                        'player': 1,
                        'start_game': False,
                        'end_game': False,
                        'text': f'Ваше число пока не угадано'
                    }
            else:
                # player2 refresh page without attempt
                context = {
                    'player': 2,
                    'start_game': False,
                    'end_game': False,
                    'form': Player2Form,
                }
                attempt = request.session.get('attempt')
                game_value = game.game_value
                if attempt > game_value:
                    context['text'] = f'Загаданное число меньше {attempt}'
                else:
                    context['text'] = f'Загаданное число больше {attempt}'

    return render(
        request,
        'home.html',
        context
    )
