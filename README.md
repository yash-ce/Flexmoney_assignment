# Flexmoney_assignment

1. Clone the repository into your system
git clone https://github.com/yash-ce/Flexmoney_assignment.git

2. cd .\Flexmoney_assignment\

3. create virtual environment into your system
 py -m venv myproject
4. Run this command  
.\myproject\Scripts\activate

5. From this ( .\myproject\Scripts\activate  )command if are getting error like "execution of scripts is disabled on this system."
then use this link for debugging  
https://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system

then after debugging run .\myproject\Scripts\activate again 

6. if your virtual environment is activated 
  then run this command
  
  cd .\yoga\

7. Install the requirements for this project use this command

  pip install -r .\requirements.txt
  
8. apply migrations 

  python .\manage.py makemigrations

9.apply changes 
python .\manage.py migrate

10. Run the server 

  python .\manage.py runserver
  
  you access the website going to this link
  
  http://127.0.0.1:8000/
  
10. For acessing the backend create superuser

  python manage.py createsuperuser
  
  run the server again

11.You can access the backend by opening this url

  http://127.0.0.1:8000/admin
  
  
