## CLI SCRIPT

To run the script use you need

1. `pip install -r requirements.txt`
2. Create SQLite3 database in the root directory with name `db.sqlite`  
Database properties
```DBMS: SQLite (ver. 3.36.0)
Case sensitivity: plain=mixed, delimited=mixed
Driver: SQLite JDBC (ver. 3.36.0.3, JDBC2.1)
```
3. Load data using `db.sql` script.
4. Run `python main.py`

## Details

`db.sql` was changed slightly to be able to load into SQLite3. No changes to the data.  

Also, there are no schema changes.  

For simplicity current date is set as a constant - `2020-07-10`. Day is replaced to `1` so the date is `2020-07-01`. Then we can query by current month according to the task.  
Other things in the code I guess are self-explanatory and don't require description.

## Answers

> Does your solution avoid sending duplicate notifications?

**Answer**:  
If there is only one record for the current month according to one shop, yes, no duplicates then. If more than one budget in the current month for single shop then code should be updated to allow only one notification per shop.

> How does your solution handle a budget change after a notification has already been sent?

**Answer**:  
Probably you meant shops change? Shops are changed in the bulk. So that means one query for all shops that need to go offline.
