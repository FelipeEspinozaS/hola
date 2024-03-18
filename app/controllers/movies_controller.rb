class MoviesController < ApplicationController
    def index_by_director
        @director = Director.find(params[:director_id])
        @movies = @director.movies
        render json: @movies
    end

    def create_movie
        @director = Director.find(params[:director_id])
        @movie = @director.movies.new(movie_params)
        if @movie.save
          render json: @movie, status: :created
        else
          render json: @movie.errors, status: :unprocessable_entity
        end
    end

    def update
        @director = Director.find(params[:director_id])
        @movie = @director.movies.find(params[:movie_id])
        if @movie.update(movie_params)
            render json: @movie
        else
            render json: @movie.errors, status: :unprocessable_entity
        end
    end

    def index_by_sinopsis
        keyword = params[:keyword]
        @movies = Movie.where('sinopsis LIKE ?', "%#{keyword}%")
        render json: @movies
    end

    private

    def movie_params
        params.require(:movie).permit(:title, :sinopsis, :duration, :premiere)
    end
end
