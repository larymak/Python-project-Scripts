# I have built my Portfolio website :relaxed:
### Link?
[Website hosted with python flask as Back-end server](https://deepaksai.pythonanywhere.com) 
##### I successfully worked on the back-end with Python flask, and now I'm working on the front-end with very basic HTML, CSS, JS knowledge. OFC, using templates!

## So, how do websites work? 
Here I'm going to focus on the python side of things. But I want to help you understand what we're building and how everything works. Hopefully, you're able to actually change your portfolio to your own liking and showcase yourself. So I have a website for you here, we have www.google.com; if I click refresh here or enter this URL, I'm taken to this Website, but  

### Note:
If you are a person who doesn't wanna follow the below steps to build a web for yourself, then do Hire me as a Freelancer:blush:
I'll work it out for you:wink:
### How does this actually work? 
How is my browser, ex. Google Chrome, able to display this Web page for me? I need to be connected to the Internet. So, there's some sort of data that's being transferred for me to be able to see this. So, let's explore how this works. 

![How websites work](/readme%20media/1.png)


In this pic, I'll attempt to tell you exactly how it works. It's quite simple. We have our browser right here, which can be Google Chrome, SAFARI, Firefox. It doesn't matter. In this browser, we can type into it a website or maybe Google for a website and then click on a website when we click on a website. What happens is that through Internet, the browser makes a request all the way to another machine. And this machine, which we call a server, is located anywhere in the world. It doesn't really matter because, through our Internet network, the browser will say, hey, this website, who owns that website or which machine can serve me the files for that website? And using some complex logic, it's going to find this server, which is just a computer at the end of the day. We're actually going to see how to deploy our own server. Well, it simply says, hey, give me some data, because, without data, I'm not able to display anything on a webpage.HTML<CSS<JS is that data btw And the server, well, first of all, they communicate over something called HTTP? HTTPS because the browser and the server are two different machines, right? HTTP/HTTPS, which is a secured encrypted version of communication, allows me to access data belonging to a website 
#### So, the request has just been made; this server just happens to have three files that we need. 
### One is an HTML file :  
This HTML file is the text or content of the website. 
### The other one is the CSS file : 
This CSS file contains all the styling of the website. So that is colours, maybe some fonts, maybe the position of the elements, anything to do with style. So, it doesn't look like a boring piece of text. 
### And then we have JavaScript :  
JavaScript is what gives websites behaviour. When I log into Facebook or maybe tweet something on Twitter, JavaScript is allowed me to perform those actions because, with just HTML and CSS, we just have the text and some pretty styling. With JavaScript, we can take action, but we don't need to focus on that too much.  
### Do you think that this server has to be written in Python? 
What do you think? No, it doesn't. The browser doesn't care what this machine is like. All it cares about are these three files. And because we're speaking in this HTTP/S protocol. The browser says, hey, I don't care what language you speak, I don't care anything, I'm just going to tell you through this. Just give me the data that I want, and we can do whatever logic we want in here. I can send emails from here if I want. I can send text messages. I can do math operations. I can play a game on this computer if I want. 
It doesn't really matter as long as I can send these files back to the browser. 

 ### So, we can start running the server right away with Python, 
 but we can do that with other languages like PHP, Java; we can write a server in any type of language. 
 
 ## Youtube Video on 'How I made this will be updated soon here! Meanwhile, check out my other projects.
 

### I successfully worked on backend with Python flask and now i'm working on frontend with very basic HTML,CSS,JS. afc, using templates!

## To built your website based on my code, Do follow the instructions:
all are windows based cmds, i'll link documentation. follow it as per your os.
1. Clone this Folder as it is!\
we are going to do this in Virtual Environment.
2. go to dir of this portfo\
    ```py -3 -m venv venv```\
   ``` venv\Scripts\activate```\
   ```pip install Flask```\
   ```set FLASK_APP=hello.py```\
   ```$env:FLASK_APP = "server.py"```\
   ```$env:FLASK_ENV = "development"``` This will  turn on Debug mode and changes made to our page will auto attached to flask app!\
   ```python -m flask run ```\
   Now head over to http://127.0.0.1:5000/, and you should see my website running on your local server i.e your pc.\
   if you dont see, then something went wrong! do contact me for quick solve!\
   [Documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
   
   ### NOTE: Do edit or replace the HTML,CSS,JS according to your needs :)
   
### We have our flask application.
nicely,Right?We have a beautiful website. We even have contact forms which will get saved to csv and text file(encoded into server.py)\
But there's a problem here. You see, we're running the browser as well as the server on the same computer.But this isn't real life because if I give this  URL to a friend, they're not going to be able to see it because this Address points to a local host. It's the same thing,local host simply means your computer, so it's not like anybody else but us can access our app. That's not very fun, is it?\
Ideally, we can create this app so we can send it to all our friends, our family members and possibly future employers.\
Stick to me, We got this buddy!

### So how can we do this?
From here, I'm going to show you a really fun, easy way to deploy your application or your website online. We're going to use something called [Pythonanywhere](https://www.pythonanywhere.com/), and [Pythonanywhere](https://www.pythonanywhere.com/) is going to allow us to host our files. That is all the files that we have here onto a server that they give us for free. So this is completely free. All you have to do is simply log in. And you can click on sign up, you can see that they have a different pricing plan, so you can actually pay for their service. But for a beginner who plan to create one Web application, we can do that for free.\
So let's create a beginner account and create your username and password. - [Pythonanywhere](https://www.pythonanywhere.com/)\
We have our dashboard. Now, the way Python, anywhere it works is that we need to load up the files on a machine, like how we have our files over here on our computer. We need to somehow upload them to Python Anywhere's computers. Now, the way we can do that is using GitHub.


3. Now, Upload everything on github like me!\
steps intended: 
 - 1. open your GitHub account
 - 2. click on new repositories and create new project here, so let's just call it. Portfo, because it sounds kind of cool and all the trendy names are short like this, so this is your  portfolio project, keep it public and then initialise with readme  and then create a repository. 
 - 3. copy CODE->CLONE->HTTPS->LINK
 - 4. Now, from here, I'm going to clone. but How? as always, follow me!
       - a. Go to Terminal and remember we are in Portfo Directory or else go to Portfo directory
       - b. git clone LINK
       - c. go to git cloned folder and pastic all your files and folders except "_pycache" ,"venv".
       - d. go to Cloned directory in cmd/powershell ( ```cd portfo\```)
       - e. ```git add.```
       - f. ```git commit -m "comment on update```
       - g. ```git push origin master``` or this it showed some error then ```git push```
       Now go to github repo and BOOM! uploaded.
       
4. go to [Pythonanywhere](https://www.pythonanywhere.com/) Dashboard and click on bash then [Pythonanywhere](https://www.pythonanywhere.com/) bash terminal opens up!
  - 1. ```git clone LINK``` link -> 3.3
  - 2. check all the files with ```ls``` -> ```cd porfo/``` -> ```ls``` or head over to dashboard again -> files -> portfo 
  - 3. head over to dashboard -> webapp -> add a new web app -> next -> manual -> py 3.6 -> webapp page
        There we go, we have our Python project at this given address.-> (your username).pythonanywhere.com
        But if I click on this. All right, I get a hello world, it's working, but this isn't our portfolio, so how can we make that work? 
        There's a few things that we need to set up.
        [Documentation for setup](https://help.pythonanywhere.com/pages/Flask/)
      **But i'm going step by step:**
   - 4. head over to webapp page -> CODE -> Source code -> enter ```portfo``` then it auto set to path in 4.2
   - 5. head over to bash then execute the below cmds
         ```mkvirtualenv --python=/usr/bin/python3.6 my-virtualenv```
         ```pip install flask```
         ```workon my-virtualenv```
         ```pip install -r requirements.txt```
   - 6. head over to webapp page -> WSGI configuration file: -> xx_wsgi.py <- open \
    clear everything! as we were working with flask, we do as below
```py
import sys
path = '/home/deepaksai/Portfo' #yoursername->deepaksai i.e project path
if path not in sys.path:
    sys.path.append(path)
    
from server import app as application
```
   - 7. click save and click reload 
   
5. :boom: our website is now live.\
    forms will be saved into csv file and text file

### NOTE: 
Do contact me for any projects or to hire me :)\
html templates are from HTML5UP

### -- SIGNING OFF --
# DEEPAK SAI PENDYALA
      
       
 

