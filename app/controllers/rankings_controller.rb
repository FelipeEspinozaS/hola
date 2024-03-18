class RankingsController < ApplicationController
    def create
        @director = Director.find(params[:director_id])
        @ranking = @director.rankings.new(ranking_params)
        if @ranking.save
            render json: @ranking, status: :created
        else
            render json: @ranking.errors, status: :unprocessable_entity
        end
    end

    def index_by_director
        @director = Director.find(params[:director_id])
        @rankings = @director.rankings
        render json: @rankings
    end

    def top_rankings
        quantity = params[:quantity].to_i
        @rankings = Ranking.all.sort_by{|ranking|(ranking.score - ranking.min_score)/(ranking.max_score - ranking.min_score)}.reverse
        @rankings2 = @rankings.first(quantity)
        render json: @rankings2

    end
    
    def index_movie_director
        @movie = Movie.find(params[:movie_id])
        @director = @movie.director
        @rankings = @director.rankings
        render json: @rankings
    end

    def destroy_worst_director
        @rankings = Ranking.all.sort_by{|ranking|(ranking.score - ranking.min_score)/(ranking.max_score - ranking.min_score)}.first
        @worst_director = @rankings.director
        if @worst_director
            @worst_director.destroy
            render json: @worst_director
        else
            render json: {error: 'No se encontró un director con el peor ranking.'}, status: :not_found
        end
    end

    def index_by_pages
        @pages = Ranking.distinct.pluck(:page)
        @rankings_by_pages = {}
      
        @pages.each do |page|
          rankings_for_page = Ranking.where(page: page).order(score: :desc) 
          @rankings_by_pages[page] = rankings_for_page
        end
      
        render json: @rankings_by_pages
    end
      

    private

    def ranking_params
        params.require(:ranking).permit(:page, :min_score, :score, :max_score, :director_id)
    end
end
