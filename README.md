Проект-шаблон для api на FastApi
Запуск возможен через докер файл, командой docker build . --tag fastapi_app && docker run -p 83:83 fastapi_app. 
На Ubuntu 2204, 80 порт занимает апач. поэтому поменял на 83, а так можно 80 указать
Так же возможно запустить локально, командой - uvicorn main:app --reload
