# Backup_Application

## Environment Setup
1. Clone the repository to the PyCharm.
2. Once the project opens, check project interpreter from the Click File > Settings > Project Interpreter.
3. Click on the settings button on the top right and then click Add local. A pop-up will open.
4. Make sure Virtual Environment is selected. In that make sure New Environment is selected.
5. Select the base interpreter and point it to the python.exe - It would be in the folder where you installed python. 
6. Click OK and wait for the environment to get created.

## Basic Installations
Click terminal from pycharm and run the following commands for basic setup. Close and re-open to make sure you are in Virtual Environment.
1. Run `pip install Django==3.1`
2. Run `cd myproject`
3. Run `python manage.py makemigrations`
4. Run `python manage.py migrate`
5. Run `python manage.py runserver`


## Running the application
1. Once everything is setup. After running python manage.py runserver This should start up the application in few seconds
2. On Home page, there are three button like Create backup,Purge backup and Search backup.
3. On clicking Create backup button which help to back up all information from pokemon card and store it to database.
4. On clicking purge backup button which remove saved data to database.
5. On clicking search backup button which useful for filtering data based on name,hit point and rarity .
