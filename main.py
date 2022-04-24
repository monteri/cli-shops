import sqlite3
import datetime

DB_NAME = 'db.sqlite'
# Assuming this date is current date
CURRENT_DATE = datetime.datetime(2020, 7, 10)


def fetch_shops_current_month(cursor, current_month):
    cursor.execute(f"select a_id, a_name, a_online, a_budget_amount, a_amount_spent"
                   f" from t_shops inner join t_budgets on t_shops.a_id = t_budgets.a_shop_id"
                   f" where t_budgets.a_month = '{current_month}'")
    return cursor.fetchall()


def turn_shops_offline(cursor, connection, shops):
    cursor.execute(f"update t_shops set a_online = 0 where a_id in ({','.join(shops)})")
    connection.commit()


def notification_message(shop_id, budget, spent, threshold):
    percentage = spent / budget * 100
    return f"[{CURRENT_DATE.date()}] SHOP_ID - {shop_id} (budget: {budget}," \
           f" spent: {spent}) \t\t {threshold} of budget exceeded ({round(percentage, 2)}%)"


if __name__ == "__main__":
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    # Replacing day to match records date
    current_month = CURRENT_DATE.replace(day=1)
    shops = fetch_shops_current_month(cursor, current_month.date())
    shops_to_go_offline = []
    for shop in shops:
        id, shop_name, is_online, budget_amount, budget_spent = shop
        if budget_spent >= budget_amount:
            print(notification_message(id, budget_amount, budget_spent, '100%'))
            if is_online:
                shops_to_go_offline.append(str(id))
        elif budget_spent >= budget_amount / 2:
            print(notification_message(id, budget_amount, budget_spent, '50%'))

    if shops_to_go_offline:
        turn_shops_offline(cursor, connection, shops_to_go_offline)

    cursor.close()
