# Проект

## Цель

Систематизировать и применить на практике знания полученные на курсе

## Тема

Тема: "_**Frontend-тестирование на основе веб-приложения Opencart и Backend-тестирование на основе API Reqres.in**_"

# Backend-тестирование на основе API Reqres.in

## Инструкции

### Для запуска в контейнере Docker:

docker build -t tests_api . 

docker run -it --rm tests_api

### Для запуска в Jenkins:
Создать параметр: THREADS - Number of parallel test threads

#### Freestyle job:

```
docker build -t tests_api . 

docker run --name testing -e THREADS tests_api -n "$THREADS"

docker cp testing:/app/allure-results . 

docker rm testing
```

#### Pipeline job:
 - Используйте  Jenkinsfile