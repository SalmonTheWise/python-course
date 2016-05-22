--1. Всю информацию о всех пользователях (все колонки в любом порядке)
SELECT * FROM Users;


--2. Количество всех пользователей (число)
SELECT users.name, count(*) FROM Users;


--3. Количество пользователей 40 лет или старше (число). 
SELECT count(*) FROM Users 
WHERE birth_date <= date("1976-05-22");


--4. Страна + количество пользователей из данной страны (страна|количество)
SELECT country, count(*) FROM Users 
GROUP BY country;


--5. Придумайте, как проверить, есть ли люди с одинаковым именем (в любом удобном формате)
SELECT users.name, count(*) AS nms FROM Users 
GROUP BY name 
ORDER BY nms desc limit 1;


--6. Количество заказов в 2016 году (число)
SELECT count(*) FROM Orders 
WHERE created >= date("2016-01-01");


--7. День, когда совершили наибольшее число заказов (день|число заказов)
SELECT date(created), count(*) AS dt FROM Orders 
GROUP BY date(created) 
ORDER BY dt desc limit 1; 


--8. Процент неоплаченных заказов (число)
SELECT 100 - sum(paid)*100.0/count(*) FROM Orders;


--9. Всю информацию о хлебе среди товаров. 
SELECT * FROM Goods WHERE name like "%bread%";


--10. Десять самых популярных товаров (встречаемость в GoodsInOrders) (id|name|количество)
SELECT Goods.id, Goods.name, count(*) AS gds FROM GoodsInOrders
INNER JOIN Goods ON good_id = id 
GROUP BY good_id 
ORDER BY gds desc limit 10;


--11. Чистая выручка в 2016 году. Нужно учитывать только оплаченные заказы (число)
SELECT sum(price) FROM Goods 
INNER JOIN Orders ON Orders.id = order_id 
INNER JOIN GoodsInOrders ON Goods.id = good_id 
WHERE paid = 1;


--12. Самые 10 популярных товаров среди женщин (id|название)
SELECT Goods.id, Goods.name FROM Goods 
INNER JOIN Users ON Users.id = user_id 
INNER JOIN Orders ON order_id = Orders.id 
INNER JOIN GoodsInOrders ON Goods.id = good_id 
WHERE Users.gender = "F" 
GROUP BY Goods.name 
ORDER BY count(*) desc limit 10;


--13. Пользователь, который купил больше всего килограмм (id|имя)
SELECT Users.id, Users.name FROM Users 
INNER JOIN Orders ON Users.id = user_id 
INNER JOIN GoodsInOrders ON Orders.id = order_id 
INNER JOIN Goods ON Goods.id = good_id 
WHERE Goods.units = "KG" 
GROUP BY user_id 
ORDER BY sum(quantity) desc limit 1;




