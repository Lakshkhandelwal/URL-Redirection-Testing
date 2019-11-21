# URL-Redirection-Testing
URL Redirection is a vulnerability in which by providing the right parameter & value a bad actor can redirect the user request to any malicious website.I developed a tool to find out the URLs having the parameters that can be used for URL Redirection.

# Instructions for direct execution without python or any other dependency installed.
1. Download or Clone the repository.
2. Open the "exeFile" folder.
3. Enter the list of URLs containing parameters in to the file named "input.txt" in the format specified below.
4. Execute the "urlredirect.exe"
5. It will automatically create an ouptut.csv file containing the output.
Caution : Do not rename the input file or exe file.

# Instructions for executing the program.
1. The program is dependent on the requests library so install that using pip.
2. Create an input file in the format specified below.
3. Execute the program from cmd specifying the input file as a parameter.

  **Command - python urlredirect.py "name of the input file".**
  
  
  ![Image of cmd](https://raw.githubusercontent.com/Lakshkhandelwal/URL-Redirection-Testing/master/images/cmd1.PNG?token=AIMORKMTSVKENO763POMTGK537C5A)

4. It will automatically create an output.csv file containing the output.

 ![Image of output](https://raw.githubusercontent.com/Lakshkhandelwal/URL-Redirection-Testing/master/images/output.png?token=AIMORKOKOSFWIPNEWSVPSH2537ER6)

# Input Format
The input format that program accepts is a text file containing list of urls containg parameters at each line, the image below shows the input format.

![Image of input](https://raw.githubusercontent.com/Lakshkhandelwal/URL-Redirection-Testing/master/images/input.PNG?token=AIMORKN23TZHCBP7F5ELWZK537FCA)
