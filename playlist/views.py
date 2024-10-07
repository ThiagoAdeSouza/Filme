from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from playlist.forms import FilmeForm, PlaylistForm
from playlist.models import Filme, Playlist 

class PlaylistListView(ListView):
    model = Playlist
    template_name = 'playlist/playlist_list.html'
  
class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = 'playlist/playlist_detail.html'

class PlaylistCreateView(CreateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = 'playlist/playlist_form.html'
    success_url = reverse_lazy('playlist_list')

class PlaylistUpdateView(UpdateView):
    model = Playlist
    fields = ['nome', 'filmes']  
    template_name = 'playlist/playlist_form.html'
    success_url = reverse_lazy('playlist_list')  

class PlaylistDeleteView(DeleteView):
    model = Playlist
    success_url = reverse_lazy('playlist_list')  



class FilmeListView(ListView):
    model = Filme
    template_name = 'filmes/filme_list.html'

class FilmeDetailView(DetailView):
    model = Filme
    template_name = 'filmes/filme_detail.html'

class FilmeCreateView(CreateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'filmes/filme_form.html'
    success_url = reverse_lazy('filme_list')

class FilmeUpdateView(UpdateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'filmes/filme_form.html'
    success_url = '/filmes/'

class FilmeDeleteView(DeleteView):
    model =Filme
    template_name = 'filmes/filme_confirm_delete.html'
    success_url = reverse_lazy('filme_list')