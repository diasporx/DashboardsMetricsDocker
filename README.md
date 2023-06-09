# Flask приложение в Cloud Native окружении

В этом репозитории находится Flask приложение, которое завернуто в Cloud Native окружение. Оно реализует тривиальный HTTP "Hello, world!" web-сервер на Python.

* app/ - папка с кодом Flask приложения
* app/__init__.py - инициализация Flask приложения и регистрация маршрутов
* app/routes.py - определение маршрутов для Flask приложения
* docker-compose.yml - определение сервисов и конфигураций для Docker Compose
* Dockerfile - файл для сборки Docker образа приложения
* README.md - файл с инструкцией по использованию и структурой проекта

## Как начать использовать

* Убедитесь, что у вас установлен Docker и Docker Compose.
* Склонируйте этот репозиторий.
* Перейдите в папку с проектом.
* Запустите приложение и все необходимые сервисы: docker-compose up.
* Откройте браузер и перейдите на страницу http://localhost:5000 для проверки работоспособности приложения.
* Откройте Grafana в браузере http://localhost:3000 и введите логин и пароль по умолчанию (admin и admin).
* Используйте endpoint http://localhost:5000/metrics для получения метрик приложения в формате Prometheus.

