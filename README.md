# MS4 - commercial website for taxi ompany - Rim-Tours.
![am_i_responsive](url)

---

Table of Contents:
1. [INTROUDUCTION](url)
2. [USER EXPERIENCE (UX) ](url)
3. [TESTING](url)
4. [DEPLOYMENT](url)
5. [CREDITS](url)
6. [DISCLAIMER](url)

------

## 1. **INTROUDUCTION**
The web aplication was created as Milestone 4 project during Full Stack Development course by Code Institue to demonstrate Python/Django,JavaScript/HTML/CSS skills acquired during the course.
The application was built based in existing website for the taxi company RIM-TOURS operating in Italy and Rome. 
The application has authentication functionality (Register/ Login) and commercial comonent based on Stripe online payment platform.
* Link to the Application: [Name](url)
* Step-By-Step development process (XXX steps) is here:[Name](url):
* testing process description is here: [Name](url):
#
## 2. **USER EXPERIENCE (UX)**
### **GOALS**
### **USER STORIES**
### **DESIGN PROCESS**
1. STRATEGY
2. SCOPE
3. STRUCTURE
4. SKELETON
5. SURFACE

### **FEATURES**
### **Features implemented**

### **Features Not implemented:**
### **TECHNOLOGIES**
  * **Languages**
    - _HTML_ - Hyperlinked markup language, to develop the fornt end pages.
    - _CSS_ - cascading style sheets to decorate html webpages, I used basic decoration with litle attention to design, focusing on functionality
    - _Javascript_ - programming language for interactive experienc, in this project I used it only for certain front-end features.
    - _Python_ - programming language to Create, Read, Update and Delete data on the Mongo DB 
  * **Libraries**
    - Django_ - python framework for comercial sites forntend application, falsk helps to reduce amount of html development and use  python with html.
    - _Bootstap_  - css library with common wed elements - used to save time on developing buttons, navbars, sidebars, and website responsiveness
    - _FontAwesome_ - icons collection - used for UX design.
    - _JQuery_ - simplified JavaScript library - to reduce amount of js coding.
    - _Stripe_ -
    - _Postgres_
    - _AWS_
  * **Tools**
    - _GitPod_ - clud based edi pogramming environment
    - _GitHub_ - cloud based development repository - this project is saved on askfrsltn profile.
    - _CLI_ - command line interface used to 
    - _Heroku_- it is clud based platform to build, and run web applications, in this project used to deploy the application to the web  
    - _MS Powerpoint_- was used to build visual structure, flow, data schema, and wireframes.  
    - _GoogleDrive_- used to store the wireframe document in pdf format.
#
## 3. **[TESTING](/testing.md)**
Testing consists of 6 sections:
1. **UserStories** 
2. **Aplication Navigation**
3. **Accessibility** 
4. **Responsivenes**
5. **Browser compatibility** 
6. **Code Validation**
7. **Site Performance with Lighthouse**
Testing details can be found here[here](/testing.md)
#
## 4. DEPLOYMENT
Theree are 4 sections in deployment chapter - (1) hosting on GitHub, Forking GitHUb repo, (2) Forking the repository (3) Running the project Locally and (4) Deploying the application to Heroku.

Working with Github and using Git was needed to host and develop the code in the cloud while Heroku was used to deploy the application to the web. 

### **GITHUB**
### **(1) Open a new repo:**
  - Register into own account on GitHub
  - Press gree Button "new"
  - On repository template select Code-institute-Org/gitpod-full-template
  - Next to the "Owner" type "Repository Name"
  - Select "public" option
  - Press green button "Create Repository" = ? new repository created based on standard Code Institute template
  - Press green button "Gitpod" - you will be prompted to cloud based EDI wher you can start editing the application code and README file.

### **(2) Forking the GitHub Repository**
To fork a repository:
- go to github page, find repository that you want to fork, enter it
- press "Fork" button at the top right corner of the repository
- Now you have a copy that you can work with without impacting it
More information can be found in gitHud Documentation [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

### **(3) Running this Project Locally** 
I did not run the project locally, however Anna Greaves explains in detail how to run the project localle with detailed instructions. next Project I will do in VS code. Detailed instruction can be found here: [Running the project Locally](https://github.com/AJGreaves/familyhub/blob/master/README.md#how-to-run-this-project-locally)

### **HEROKU**
### **(4) Hosting on Heroku**
In order to deply the app to Heroku you need to go thorugh following steps:
1. Gitpod - tell heroku which apps and dependencies are required to run an app - create requirments.txt file:

        pip3 freeze --local>requirements.txt   
2. create Procfile for Heroku (important to have space before python and delete last line space in Procfile - it is very important for connection):

        echo web: python app.py>Procfile
NOTE: When deployed the file it is very important that procfile contains very precise inforomation, with no spaces or last emplty line otherwise it won't connect to heroku. 
3. Create new app at heroku profile, app name: ask-pft-meetinghub,
4. Go to heroku website - open the app frim github,  
5. Deploy and enable Automatic Deployment, select "main" branch and press deploy. 
6. After a while - press View - check "hello world"
7. Go to settings and set up config vars:

      IP: "0.0.0.0"
      PORT: "5000"
      SECRET_KEY: (from env.py)
      MONGO_URI: see the step below
      MONGO_DBNAME: "ms3"
8. Hide config vars
9. Check if requiremets.txt and Procfile was created in repository

        CLI: git status
10. Push using commit command for each of the 2 files one by one:

        git add requirements.txt     + Enter
        git commit -m "..."          + Enter
        git add Procfile             + Enter
        git commit -m "..."          + Enter
        git push                     + Enter
11. Connect Mongo DB to heroku as well:
12. In CLI: Install flask-pymongo and dus-python to use mongo srv connection string:
        
        CLI:
        pip3 install flask-pymongo
        pip3 install dns-python

13. Update requirments.txt

        pip3 freeze --local>requirements.txt
14. in app.py install PyMongo and OjectId form the libraries

        from flask_pymongo import PyMongo
        from bson.objectid import ObjectId

15. define app configuration in app.py:

        app.config["MONGO_DBNAME"]= os.environ.get("MONGO_DBNAME")
        app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
        app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

16. Creaete URI key: go to MongoDb, select "databases", go to "connect", go to "connect your application", copy the key and replace 3 parameters;
            
        "mongodb+srv://askformongodb:password@clustername.eqlwe.mongodb.net/databasename?retryWrites=true&w=majority"
        where:
        1. password: XXXXXX
        2. clustername: your_cluster
        3. databasename: your_dtb
You can find more details and sequence of steps on [step by step developemnt process](/sbsdev.md)

#
## 5. CREDITS
### **Content**
  * The conetnt for the application was developed myself based on 15 years of operaational consulting experience and thanks to the team from [Alexandr Proudfoot consulting company](https://proudfoot.com/) - Monique, Kamal, Tim Sebastian who were great partners in brainstorming the wireframes.

### **Media**
  All the media content was developed by myself in Powerpoint and stored in jpg format

### **Acknowledgements**
  - Code institute for the backend project Example and all the great videos on Python, Flask and database management. Also for github template - I used for code development.
  - Chriss Quin for mentorship, good tips and critical advices
  - Kevin, Miklosh and Johan for great lessons and support during coding problem solving
  - Special thanks to Anna Greaves - she is a constant source of motivation for me. She is a benchmark of development and perfection. I really get inspired by what she does and how deep she goes when it comes to learning new things.
  - "Alexandr Proudfoot" consulting company for giving me inspiration assigning me to Digital Results Hub workstream and letting me use one of the 5 modules as a prototype for my project
  - Stack overflow and bloggers: 
    - Punit Jajodia and his website [programiz](https://www.programiz.com/python-programming/datetime/current-datetime)
  - My family - for patience, motivation and energy.
#
## 6. DISCLAIMER
- This project is for educationall purpose only. It is a part of the Code Institute course of Software Development. Module - Python Flask and Backend development.