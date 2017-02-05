# Movie Aggregator

The console based application is built with the help of two packages, pdfkit and wkhtmltopdf.
The project runs on Python 2.7.12.

#How it works:
For this project, we have used 3 python files, that includes one main file and the other files are used as reference. 
The app.py file is the main file. This file takes all the input from the user. The constructor initializes the 
values of the movie class with the new entered values. Then we proceed on to convert the file.

For this, we pass on the object "movie" and also the "format_type" to be converted to the function "convert".
The "convert" function with the help of reflection property accesses the data functions of the "format_define" class.
Depending upon the format to be converted, the member functions "text" or "pdf" is accessed. 

The data is written into the file. If it needs to be converted to pdf, the pdfkit is used. 

The file is hence generated.

## To run the code:

1. Install the package "pdfkit" using the command "pip install pdfkit"
2. Install wkhtmltopdf package the same way as above. 
4. Now run the app using the command "python app.py"
5. It will ask you to input all the values along with the format you want it to be in.
6. The values will be written into a text file
7. The conversion will be done according to your specification.
