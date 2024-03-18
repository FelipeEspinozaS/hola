Rails.application.routes.draw do
  # Parte 1
  get '/directors', to: 'directors#index'
  post '/directors', to: 'directors#create'
  get '/director/:id', to: 'directors#show'
  delete '/director/:id', to: 'directors#destroyer'
  delete '/directors', to: 'directors#destroy_all'
  get '/directors/oscars', to: 'directors#directors_with_oscars'

  # Parte 2
  get '/director/:director_id/movies', to: 'movies#index_by_director'
  post '/director/:director_id/movies', to: 'movies#create_movie'
  patch '/director/:director_id/movies/:movie_id', to: 'movies#update'
  get '/movies/sinopsis/:keyword', to: 'movies#index_by_sinopsis'

  # Parte 3
  post '/ranking/:director_id', to: 'rankings#create'
  get '/ranking/:director_id', to: 'rankings#index_by_director'
  get '/ranking/top/:quantity', to: 'rankings#top_rankings'
  get '/movies/:movie_id/director/rankings', to: 'rankings#index_movie_director'
  delete '/director/ranking/low', to: 'rankings#destroy_worst_director'
  get '/ranking/pages/all', to: 'rankings#index_by_pages'
end
