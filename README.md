# AAVE-ChatBot
 A Django project which connects to openai ChatGPT using API. This ia a ChatBot which answers queries specific to AAVE and assist AAVE users. 

#### Intergrated Django UI from [Link](https://github.com/Johnkh2002/ChatGPT-Tutorial)

# Setup

Prerequisites
-------------

Before getting started with the project, you will need to have an OpenAI API key. You can get the key by signing up on the [OpenAI's website](https://platform.openai.com/account/api-keys). Once you have an API key, you can integrate it with the Streamlit interface.

Integration
-----------

* Install the requirements by:
```sh
pip install -r requirements.txt
```

* Once all the requirement libraries are installed, create a file called `apikey.py`

* Declare a varibale named `openai_api_key` with API key value.
```sh
echo "openai_api_key = '<Enter your OpenAI Key here>' " > apikey.py
```

Running the Django Application
-------------------------

Migrate Django DB

```sh
python manage.py makemigrations
```

```sh
python manage.py migrate
```


Run the Django app using the following command:

```sh
python manage.py runserver     
```

The app should now be running on your localhost.

```sh
http://127.0.0.1:8000
```
