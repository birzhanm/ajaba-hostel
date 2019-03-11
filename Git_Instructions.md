A short note on working with git and github for members of Ajaba Labs

Initial copying (cloning) of this repo into your machine. All of the following commands
are written in command line (CL):
1. Go to the directory you wish to place this porject
2. git clone https://github.com/birzhanm/ajaba-hostel.git
3. Start a virtual environment called 'venv': python3 -m venv venv (for Mac)
4. Activate your virtual environment: source venv/bin/activate
5. Install project dependencies: pip install -r requirements.txt
6. Migrate into your database: python manage.py migrate
7. Start development server: python manage.py runserver
8. Start developing the changes you wish to see!

Pushing changes into the original repo:
1. Sync your local repo with the remote repo: git pull origin master
2. If you wish to develop some changes, create a separate branch: git checkout -b 'add-new-models'
3. Change the code
4. Add your changes to your local git repo: git add .
5. Commit your changes: git commit -m "added new models"
6. Push your changes into the branch of remote repo: git push origin add-new-models
