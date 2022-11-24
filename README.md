# Тестовое задание на позицию Python Backend Developer (Django)

Реализовано приложение, моделирующее процесс оплаты отдельных товаров, а также товаров, сгруппированных в заказы, про помощи Django
и библиотеки платежных функций Stripe (https://stripe.com/docs).


# Функционал
Django-модели Item (отдельный товар), Order (заказ), Discount (скидка), Tax (налог). Присутствуют возможности выбора валюты заказа 
и товара, назначения заказу налога или скидки. В модели товара также реализован метод, приводящий цену в формат, 
удобный для отображения, в модели заказа - методы расчета стоимости группы товаров и общей стоимости заказа. 

В приложении реализованы следующие эндпойнты:
1. GET /buy/{id} - возвращает Stripe Session Id для оплаты выбранного Item;
2. GET /item/{id} - возвращает простую HTML-страницу с информацией о выбранном Item и кнопкой Buy. 
При нажатии на Buy происходит запрос на /buy/{id}, получение session_id и далее перенаправление 
на форму оплаты Stripe;
3. GET /buy/order/{id} - возвращает Stripe Session Id для оплаты выбранного Order;
4. GET /order/{id} - возвращает простую HTML-страницу с информацией о выбранном Order, в т.ч. информацию
о входящих в заказ товарах, их количестве и стоимости, а также общей стоимости заказа, и кнопкой Buy. 
При нажатии на Buy происходит запрос на /buy/order/{id}, получение session_id и далее перенаправление 
на форму оплаты Stripe;
5.GET /success - выводит сообщение об успешном платеже. Запрос перенаправляется на эту страницу в случае успешного платежа;
6. GET /cancelled - выводит сообщение о прерванном платеже. Запрос перенаправляется на эту страницу в случае, если
платеж был прерван;
7. GET /admin - панель администратора Django. Доступны для редактирования и создания новых записей модели Item, Order, Discount, Tax. 
Для удобства тестирования создан суперпользователь (данные для входа - admin: admin);
8. GET /config - служебный эндпойнт, возвращающий публичный ключ Stripe.

# Запуск проекта
1. git clone https://github.com/artemyev1003/payments-test-assignment.git - клонируем репозиторий проекта;
2. cd payments_backend - переходим в корневую директорию проекта;
3. docker-compose up -- build - собираем и запускаем проект. Формируются 2 контейнера - с Django-приложением и с БД PostreSQL. 
Для удобства тестирования в проект включены файлы БД: уже создано несколько объектов моделей, а также суперпользователь. 


