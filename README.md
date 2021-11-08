# telemedicine-backend

### Initial Installations
#### For ubuntu
1. virtualenv
```console
yash97@yash:~$ sudo apt-get install virtualenv
```
2. pip3
```console
yash97@yash:~$ sudo apt-get install python3-pip
```
#### For windows
1. virtualenv
```console
PS C:\Users\yasht> python -m pip install --upgrade pip
PS C:\Users\yasht> python -m pip install --user virtualenv
```

### Initial Setup
#### For ubuntu
1. Make Projects directory
```console
yash97@yash:~$ mkdir Projects/
yash97@yash:~$ cd Projects
```
2. Clone the repository
```console
yash97@yash:~$ git clone https://github.com/yashrtalele97/telemedicine-backend.git
yash97@yash:~$ cd telemedicine-backend/
```
3. Create virtual environment
```console
yash97@yash:~$ virtualenv venv
```
4. Activate virtual environment
```console
yash97@yash:~$ source venv/bin/activate
```
5. Install requirements.txt
```console
yash97@yash:~$ pip3 install -r requirements.txt
```
#### For windows
1. Clone the repository
```console
PS C:\Users\yasht> git clone https://github.com/yashrtalele97/telemedicine-backend.git
PS C:\Users\yasht> cd telemedicine-backend/
```
2. Create virtual environment
```console
PS C:\Users\yasht> python -m venv env
```
3. Activate virtual environment
```console
PS C:\Users\yasht> .\env\Scripts\activate
```
4. Install requirements.txt
```console
PS C:\Users\yasht> pip install -r requirements.txt
```

### Steps to start the backend server
#### For ubuntu
1. Make initial migrations
```console
yash97@yash:~$ python manage.py makemigrations
```
2. Migrate
```console
yash97@yash:~$ python manage.py migrate
```
3. Run the server
  - On the localhost  
    ```console
    yash97@yash:~$ python manage.py runserver
    ```
  - On the IP address
    ```console
    yash97@yash:~$ ip address
    ```
   
    > copy the inet address from wl01 <br />
    > PORT can be any 4 digits number, but make sure that port is not used by any other application
    ```console
    yash97@yash:~$ python manage.py runserver 192.XXX.X.XXX:PORT
    ```
#### For windows
1. Make initial migrations
```console
PS C:\Users\yasht> python manage.py makemigrations
```
2. Migrate
```console
PS C:\Users\yasht> python manage.py migrate
```
3. Run the server
  - On the localhost  
    ```console
    PS C:\Users\yasht> python manage.py runserver
    ```
  - On the IP address (for the following the powershell or windows terminal need to be run as administrator)
    ```console
    PS C:\WINDOWS\system32> Get-NetIPAddress -AddressFamily IPV4
    ```
   
    > copy the ip address <br />
    > PORT can be any 4 digits number, but make sure that port is not used by any other application
    ```console
    PS C:\Users\yasht> python manage.py runserver 192.XXX.X.XXX:PORT
    ```
