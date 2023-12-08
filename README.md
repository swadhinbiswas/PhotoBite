
# PhotoBite

photobite is a image Gallery using Django .It's a biggner friendly project made by Me(swadhinbiswas).And it not a complete project.More feature will be added .

## Features

➡️ AnyOne can Upload photo          

➡️Home page Image Gallery  

➡️Sign Up         

➡️Sign In  

➡️User DashBoard

➡️personal Gallery

## Roadmap

- Google Drive,One Drive,Mega etc Stroage Photo adding On personal Gallery

- Multiple Stroage Connetion 

- Gallery catagory 

- Multiple photo Upload

- Connect Local Stroage Photo

- Share with friends 
- Not downloadable



# Logo

![Logo](https://gitlab.com/pyhub2/assets/-/raw/f3875de550c037dad040c362aacce2d252b9eb61/Screenshot_from_2023-12-09_02-12-11.png)


## Screenshots
#### Homepage
![App Screenshot](https://gitlab.com/pyhub2/assets/-/raw/main/Screenshot_from_2023-12-09_02-19-47.png)

#### Login page

![App Screenshot](https://gitlab.com/pyhub2/assets/-/raw/main/Screenshot_from_2023-12-09_02-29-26.png)


#### SignUp page

![App Screenshot](https://gitlab.com/pyhub2/assets/-/raw/main/Screenshot_from_2023-12-09_02-27-39.png)


#### Dashboard

![App Screenshot](https://gitlab.com/pyhub2/assets/-/raw/main/Screenshot_from_2023-12-09_02-19-47.png)


#### upload page
![App Screenshot](https://gitlab.com/pyhub2/assets/-/raw/main/Screenshot_from_2023-12-09_02-23-32.png)

## Installation

```
sudo apt update && upgrade
```
```
sudo apt install pyhton3
```
```
python3.11 --version
```
### set env
```
sudo apt install -y python3-venv

mkdir test_environment && cd test_environment

sudo python3 -m venv my_test_env

ls my_test_env

source my_test_env/bin/activate

```
### install all necessary packages 

```
pip3 install pillow

pip3 install django

```

# Database Change 

#### this part is not necessary for now 
## Deployment

To deploy this project run

```
git clone 

cd PhotoBite

python3 manage.py makemigration

pyhton3 manage.py migrate

python3 manage.py createsuperuser

pyhton3 manage.py runserver

```


