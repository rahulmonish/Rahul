
import movie
from convert_file import convert


if __name__ == '__main__':
   
    
    name = raw_input("Enter the Movie name: ")
    run_time = raw_input("Enter the run time: ")
    language = raw_input("Enter the language: ")
    lead_actor = raw_input("Enter the lead actor: ")
    genre = raw_input("Enter the genre: ")
    format_type = raw_input("Which format do you want the output? ")
    
    #now we have all the input we require
    
    movie = movie.Movie(name, run_time, language, lead_actor, genre)  #calling the constructor of the Class Movie
    convert(movie, format_type)            #this is for converting the file to the specified format
