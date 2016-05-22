__author__ = 'jack-a-lynn'

import sqlite3 as sqlt


def unpaid(user_id):
    query = "select Users.name, Orders.id, sum(price) from Users " \
        "inner join Orders on Users.id = user_id " \
        "inner join GoodsInOrders on Orders.id = order_id " \
        "inner join Goods on Goods.id = good_id " \
        "where Orders.paid = 0 and Users.id = ? " \
        "group by Orders.id"
    with sqlt.connect("data.sqlite") as food:
        cur = food.cursor()
        answ = cur.execute(query, [user_id]).fetchall()
    return answ

print(unpaid(12))


