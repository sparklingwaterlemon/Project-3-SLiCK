from django.shortcuts import render, redirect
import os

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bet, Team

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse


# Home Page
# http://localhost:8000/
def home(request):
    return render(request, "home.html")

# Bets Index
# http://localhost:8000/bets/
@login_required
def bets(request):
    bets = Bet.objects.filter(user=request.user)
    return render(request, "bets.html", {
        'bets': bets
        })

# Bets Detail
# http://localhost:8000/bets/123/
@login_required
def bets_detail(request, bet_id):
    bets = Bet.objects.get(id=bet_id)
    teams_bets_doesnt_have = Team.objects.exclude(id__in=bets.teams.all().values_list('id'))

    # grabbing all teams in bets
    all_teams = Bet.objects.get(id=bet_id).teams.all()

    # creating this new variable..
    bet_total_score = Bet.objects.get(id=bet_id).total_score

    # resetting score to 0
    bet_total_score = 0
    bets.total_score = bet_total_score
    bets.save()

    # for loop for iterating thru all teams
    # adding team score to bets_score
    for team in all_teams:
        bet_total_score += team.score
        bets.total_score = bet_total_score
        bets.save()
        
    return render(request, 'bets/detail.html', {
        'bets': bets,
        'teams': teams_bets_doesnt_have
    })








# Create a New Bet
# http://localhost:8000/bets/create/
class BetsCreate(LoginRequiredMixin, CreateView):
    model = Bet
    fields = ['name', 'wager']
    # This inherited method is called when a
  # valid cat form is being submitted
    def form_valid(self, form):
      # Assign the logged in user (self.request.user)
      form.instance.user = self.request.user  # form.instance is the cat
      # Let the CreateView do its job as usual
      return super().form_valid(form)

    def get_success_url(self, **kwargs):
        # http://localhost:8000/bets/123/
        # path('bets/<int:bet_id>/', views.bets_detail, name='detail'),
        return reverse('detail', args=(self.object.id, ))

# Update Bet
# http://localhost:8000/bets/123/update/
class BetsUpdate(LoginRequiredMixin, UpdateView):
    model = Bet
    # Only allows user to update wager and name
    fields = ['name', 'wager']

    def get_success_url(self, **kwargs):
        # back to details page of bet
        # path('bets/<int:bet_id>/', views.bets_detail, name='detail'),
        return reverse('detail', args=(self.object.id,))

# Delete Bet
# http://localhost:8000/bets/123/delete/
class BetsDelete(LoginRequiredMixin, DeleteView):
    model = Bet
    success_url = '/bets/'


# List of Teams
# http://localhost:8000/teams/
class TeamList(LoginRequiredMixin, ListView):
    model = Team

# Team Detail
# http://localhost:8000/teams/123/
class TeamDetail(LoginRequiredMixin, DetailView):
    model = Team

# Team Create
# http://localhost:8000/teams/create/
class TeamCreate(LoginRequiredMixin, CreateView):
    model = Team
    fields = '__all__'

    success_url = '/teams/'

# Team Update
# http://localhost:8000/teams/123/update/
class TeamUpdate(LoginRequiredMixin, UpdateView):
    model = Team
    fields = ['name', 'score']

    def get_success_url(self, **kwargs):
        # back to details page of bet
        # path('teams/<int:pk>/', views.TeamDetail.as_view(), name='teams_detail'),
        return reverse('teams_detail', args=(self.object.id,))

# Team Delete
# http://localhost:8000/teams/112/delete/
class TeamDelete(LoginRequiredMixin, DeleteView):
    model = Team
    success_url = '/teams/'


# Adding Teams to Bet
# http://localhost:8000/bets/123/assoc_team/123/
@login_required
def assoc_team(request, bet_id, team_id):
    Bet.objects.get(id=bet_id).teams.add(team_id)

    # score adding functionality here ---- :
    # grabbing the 'total_score' of an individual bet
    bet_total_score = Bet.objects.get(id=bet_id).total_score

    # grabbing the 'score' of the individual team
    team_individual_score = Team.objects.get(id=team_id).score

    # bet total score is adding team individual score
    bet_total_score += team_individual_score
    
    # updating/saving the new bet total score
    bet = Bet.objects.get(id=bet_id)
    bet.total_score = bet_total_score
    bet.save()

    return redirect('detail', bet_id=bet_id)


# Removing Teams from Bet
# http:///localhost:8000/best/123/remove_team/123/
@login_required
def teams_remove(request, bet_id, team_id):
    Bet.objects.get(id=bet_id).teams.remove(team_id)

    # score adding functionality here ---- :
    # grabbing the 'total_score' of an individual bet
    bet_total_score = Bet.objects.get(id=bet_id).total_score

    # grabbing the 'score' of the individual team
    team_individual_score = Team.objects.get(id=team_id).score

    # bet total score is adding team individual score
    bet_total_score -= team_individual_score
    
    # updating/saving the new bet total score
    bet = Bet.objects.get(id=bet_id)
    bet.total_score = bet_total_score
    bet.save()

    return redirect('detail', bet_id=bet_id)




def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('bets')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
    
def some_function(request):
    secret_key = os.environ['SECRET_KEY']


