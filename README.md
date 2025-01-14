![2023-03-29_191705](https://user-images.githubusercontent.com/108303572/228615897-8bd00bcd-cd95-4a56-9783-34211fdf2780.jpg)

# Виртуальная стажировка 
## Pereval REST API

Федерации спортивного туризма России [pereval.online](https://pereval.online) (далее - ФСТР) заказала студентам SkillFactory разработать мобильное приложение для Android и IOS, которое упростило бы туристам задачу по отправке данных о перевале и сократило время обработки запроса до трёх дней.

Пользоваться мобильным приложением будут туристы. В горах они будут вносить данные о перевале в приложение и отправлять их в ФСТР, как только появится доступ в Интернет.

Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.

___

*Турист с помощью мобильного приложения будет передавать в ФСТР следующие данные о перевале:*
+ ***Информацию о себе:***
  + ***Фамилия;***
  + ***Имя;***
  + ***Отчество;***
  + ***Электронная почта;***
  + ***Номер телефона.***
+ ***Название объекта;***
+ ***Координаты объекта и его высоту;***
+ ***Уровень сложности в зависимости от времени года;***
+ ***Несколько фотографий.***
*После этого турист нажимает кнопку «Отправить» в мобильном приложении. Мобильное приложение вызовет метод **Pereval**.*

+ ***Метод:***
 
```
POST/api/Pereval/
```

 *принимает JSON в теле запроса с информацией о перевале. Пример JSON-а:*
```
{
  "beauty_title": "пер. ",
  "title": "Пхия",
  "other_titles": "Триев",
  "connect": "", //что соединяет, текстовое поле
 
  "add_time": "2021-09-22 13:18:13",
  "user": {"email": "qwerty@mail.ru", 		
        "fam": "Пупкин",
		 "name": "Василий",
		 "otc": "Иванович",
        "phone": "+7 555 55 55"}, 
 
   "coords":{
  "latitude": "45.3842",
  "longitude": "7.1525",
  "height": "1200"}
 
 
  level:{"winter": "", //Категория трудности. В разное время года перевал может иметь разную сложность
  "summer": "1А",
  "autumn": "1А",
  "spring": ""},
 
   images: [{data:"<картинка1>", title:"Седловина"}, {data:"<картинка>", title:"Подъём"}]
}
```
***Результат метода: JSON***
+ *status — код HTTP, целое число:*
 
    *500 — ошибка при выполнении операции;*
    
    *400 — Bad Request (при нехватке полей);*
    
    *200 — успех.*


*После того, как турист добавит в базу данных информацию о новом перевале, сотрудники ФСТР проведут модерацию для каждого нового объекта и поменяют поле status.*
***Допустимые значения поля status:***
+ *'new';*
+ *'pending' — модератор взял в работу;*
+ *'accepted'  — модерация прошла успешно;*
+ *'rejected' — модерация прошла, информация не принята.*
______
 ***Метод:*** 
```
GET /api/Pereval/<id>
```
*получает одну запись (перевал) по её id с выведением всей информацию об перевале, в том числе статус модерации.*
____
***Метод:***
```
PATCH /api/Pereval/<id>
```
*позволяет отредактировать существующую запись (замена), при условии что она в статусе "new". При этом редактировать можно все поля, кроме тех, что содержат ФИО, адрес почты и номер телефона. В качестве результата изменения приходит ответ содержащий следующие данные:*
 *state:*
     *1 — если успешно удалось отредактировать запись в базе данных.*
     *0 — в отредактировать запись не удалось.*
    
 *message: сообщение о причине неудачного обновления записи.*

 
_____
***Метод:***
   
```
GET /api/Pereval/?user__email=<email>
```
*позволяет получить данные всех объектов, отправленных на сервер пользователем с почтой.* 
В качестве реализации использована фильтрация по адресу электронной почты пользователя с помощью пакета **django-filter**
______