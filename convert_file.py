import pdfkit



class final_op(object):
    
    @staticmethod
    def get_op(movies):
        
        fname = 'output.txt'      #this is the file we are writing into                                                     
        fw = open(fname, 'w')
        s = "MOVIE NAME | \t RUN TIME | \t LANGUAGE | \t LEAD ACTOR | \t GENRE \n"
        fw.write(s)               #using the write function
        
        
        for movie in movies:      #now we write all the values into the file
            fw.write("%10s "%  movie.name + "| \t" +"%9s"% movie.run_time + " | \t" +
                    "%9s"% movie.language + " | \t" + "%11s"% movie.lead_actor + " | \t" +"%6s"% movie.genre + "\n")
        fw.close()                 #file is closed





class format_define(final_op):
    

    @staticmethod
    def text(movies):                                #this is the case where you want a text file as output
        final_op.get_op(movies)



    @staticmethod
    def pdf(movies):                                 #this is the case where you want a pdf file as an output
        final_op.get_op(movies)
        pdfkit.from_file('output.txt', 'output.pdf')  #using pdfkit the file is converted to pdf






def convert(movie, export_method):                     #this function converts the file to the pdf format
    class_name = "format_define"
    format_type = export_method
    obj = globals()[class_name]()
    getattr(obj, format_type)([movie])                 #using reflection property to acess the attribute of the object
