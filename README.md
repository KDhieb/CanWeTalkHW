# Get the code
git clone https://github.com/app-generator/flask-dashboard-dattaable.git
cd flask-dashboard-dattaable
# Virtualenv modules installation (Unix based systems)
 virtualenv env
 source env/bin/activate

 # Virtualenv modules installation (Windows based systems)
  virtualenv env
  .\env\Scripts\activate

 # Install modules - SQLite Database
 pip3 install -r requirements.txt

 # OR with PostgreSQL connector
 pip install -r requirements-pgsql.txt

 # Set the FLASK_APP environment variable
 (Unix/Mac) export FLASK_APP=run.py
 (Windows) set FLASK_APP=run.py
 (Powershell) env:FLASK_APP = ".\run.py"

 # Set up the DEBUG environment
 (Unix/Mac) export FLASK_ENV=development
(Windows) set FLASK_ENV=development
 (Powershell) env:FLASK_ENV = "development"

 # Start the application (development mode)
  --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
  --port=5000    - specify the app port (default 5000)  
 flask run --host=0.0.0.0 --port=5000

 # Access the dashboard in browser: http://127.0.0.1:5000/
 
 
 # HackWestern7 Hackathon Project - CanWeTalk Mental Health Platform

## How to run this project

# Get the code
git clone https://github.com/app-generator/flask-dashboard-dattaable.git
cd flask-dashboard-dattaable

# Virtualenv modules installation (Unix based systems)
virtualenv env
source env/bin/activate

# Virtualenv modules installation (Windows based systems)
# virtualenv env
# .\env\Scripts\activate

# Install modules - SQLite Database
pip3 install -r requirements.txt

# OR with PostgreSQL connector
# pip install -r requirements-pgsql.txt

# Set the FLASK_APP environment variable
(Unix/Mac) export FLASK_APP=run.py
(Windows) set FLASK_APP=run.py
(Powershell) $env:FLASK_APP = ".\run.py"

# Set up the DEBUG environment
# (Unix/Mac) export FLASK_ENV=development
# (Windows) set FLASK_ENV=development
# (Powershell) $env:FLASK_ENV = "development"

# Start the application (development mode)
# --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
# --port=5000    - specify the app port (default 5000)  
flask run --host=0.0.0.0 --port=5000
# Access the dashboard in browser: http://127.0.0.1:5000/


## Inspiration
University students during the COVID-19 pandemic have experienced some of the worst mental-health concerns in the population, as we’re separated from our friends, family and forced to study online during lockdown. We wanted to create the best platform for students to easily connect with mental-health help from university therapists or counselors. 

## What it does
CanWeTalk is a platform that allows students to instantly text-message a university counsellor via a university-wide number, with no app downloads required. It’s designed to be as effortless as possible to connect with a school counselor. The moment their message is sent, it is received by the counsellors who can reply instantly, making campus mental health services more convenient for all students.

## How we built it
<ol>
<li>SMS routing is done via the Twilio API. It receives text messages and sends them to our back-end server, and vice-versa.</li>
<li>Chat rooms are built using Socket.IO API. It waits for messages to be received, and then posts them to the chat room and back to Twilio API to then respond back to the user.</li>
<li>Backend and frontend are powered via Python’s Flask Web-Framework and JavaScript. Bootstrap elements and components were used in designing a user-friendly UI</li>
</ol>

## Challenges we ran into
<ol>
<li>The first challenge was making Twilio API work. It took us a while in order to understand how the API is best implemented and how to have our Python code fetch the incoming message and number.</li>
<li>Once we figured that out, our next challenge was to push the messages over to a chat room.</li>
<li>We played around with a few API frameworks before landing on Socket.IO. While the system is very basic, it worked for our needs.</li>
<li>Additionally, we needed to configure Flask using a linux terminal which was a different process for each of our machines, as we needed to integrate and connect Flask from our frontend to the backend </li>
<li>Student

</ol>

## Accomplishments that we're proud of
<ol>
<li>Making the SMS chat work! When we were finally able to push the SMS message to our program and have it appear on chat (and vice-versa), we were proud of our work!</li>
<li>Our technology can be leveraged to improve thousands of students across Canada, who are struggling with mental health. Suicide and depression rates are currently increasing during the start of the COVID pandemic, we don’t want to lose anymore students</li>
<li>If CanWeTalk ever made it live and helped university students access mental health faster,  then we would be proud to have contributed to mental health access for university students through this hackathon project!</li>
<li>
</ol>

## What we learned
We had zero experience working with Twilio and Socket.IO APIs prior to this project. We have spent many, many hours trying to make our code work. If we had to do this again, we would hope to be able to mobilize the program much quicker in making the basic features work and being able to add more advanced features to our platform.



## Challenges we ran into
<ol>
<li>The first challenge was making Twilio API work. It took us a while in order to understand how the API works and how to have our Python code fetch the incoming message and number.</li>
<li>Once we figured that out, our next challenge was to push the messages over to a chat room.</li>
<li>We played around with a few API frameworks before landing on Socket.IO. While the system is very basic, it worked for our purposes.</li>
<li>We would likely have switched to a different framework like React if we were given enough time to perfect our JS skills.</li>
</ol>


## What's next for CanWeTalk
<ol>
<li>There are final touches we would like to finish before CanWeTalk is ready. We would like to make it easier for counselors to switch between multiple conversations.</li> <li>Furthermore, redesigning and building this application using a JavaScript stack would be easier and more efficient than using the Python Flask framework.
<li>This idea would need to be pitched to the universities and approved before they are launched. With their support, we can integrate CanWeTalk to access student information directly, while being able to securely authenticate registered students by implementing their system..</li>
</ol>


