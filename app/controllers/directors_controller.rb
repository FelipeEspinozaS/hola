class DirectorsController < ApplicationController
    def index
        @directors = Director.all
        render json:@directors
    end

    def create
        @director = Director.new(director_params)
        if @director.save
            render json: @director, status: :created
        else
            render json: @director.errors, status: :unprocessable_entity
        end
    end

    def show
        @director = Director.find(params[:id])
        render json: @director
    end

    def destroyer
        @director = Director.find(params[:id])
        @director.destroy
        #LLORA
        render json: {}
    end

    def destroy_all
        @directors = Director.all
        Director.destroy_all
        render json:@directors
    end

    def directors_with_oscars
        @directors = Director.where(has_oscars: true)
        render json: @directors
    end

    private
      
    def director_params
        params.require(:director).permit(:name, :age, :country, :has_oscars)
    end
end
