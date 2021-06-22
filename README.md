# yoyo-api

# setup

```
pip install -r requirements.txt
python manage.py migrate

```

# run project

```
export WEATHER_API_KEY=your_api_key_here
python manage.py runserver

```

# test project

```
export WEATHER_API_KEY=your_api_key_here
python manage.py test
```

# api key

for development, ignore if you only running it
yoyoapi/.env
WEATHER_API_KEY=your_api_key_here
