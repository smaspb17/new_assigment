
-- Этап 1: Массовое наполнение базы
-- ограничения в таблице order_items:
--      1) order_id от 1 до 6;
--      2) quantity от 1 до 10;
--      3) price от 1 до 100_000

-- удалить старые данные из таблицы order_items
delete from order_items;

-- в терминале выполнить команду для внесения записей в таблицу order_items
'psql - U postgres -d new_issue -f order_items_1000000.sql'

-- проверка количества записей в таблице order_items. Должно быть 1 млн.
select count(*) from order_items;

-- =======================================================================================

-- Этап 2: Установка индексов

create index idx_orders_customer_id on orders(customer_id);
create index idx_order_items_id_price on order_items(order_id, price);
create index idx_order_items_product_name on order_items(product_name);

-- =======================================================================================

-- Этап 3: Анализ использования индексов

explain analyze select * from order_items
where price > 10000 and id = 1;
--  Index Scan using order_items_pkey on order_items  (cost=0.42..8.45 rows=1 width=45) (actual time=0.016..0.016 rows=0 loops=1)
--    Index Cond: (id = 1)
--    Filter: (price > '10000'::numeric)
--  Planning Time: 0.155 ms
--  Execution Time: 0.037 ms
-- (5 rows)

explain analyze select * from orders
where customer_id = 1;
-- Seq Scan on orders  (cost=0.00..1.07 rows=1 width=16) (actual time=0.011..0.013 rows=2 loops=1)
--    Filter: (customer_id = 1)
--    Rows Removed by Filter: 4
--  Planning Time: 0.068 ms
--  Execution Time: 0.029 ms
-- (5 rows)

-- =======================================================================================

-- Этап 4: Удаление неэффективных индексов

-- индекс на customer_id в таблице orders является излишним,
-- так как планировщик БД его не использует в запросах;
-- в связи с тем что индекс занимает место и замедляет DML запросы,
-- принято решение об удалении индекса у поля customer_id
drop index idx_orders_customer_id;

-- =======================================================================================

-- Этап 5: Бизнес-логика с использованием транзакций

-- проверка количества записей в таблицах
select count(*) from orders;
select count(*) from order_items;
-- ответы: 6 и 1_000_000

-- успешная транзакция
begin transaction isolation level repeatable read;
    insert into orders (id, customer_id, order_date)
        values (7, 1, '2025-02-01');
    insert into order_items (order_id, product_name, quantity, price)
        values (7, 'Что-то там крутое1', 9, 15000.00);
    insert into order_items (order_id, product_name, quantity, price)
        values (7, 'Что-то там крутое2', 6, 13000.00);
    insert into order_items (order_id, product_name, quantity, price)
        values (7, 'Что-то там крутое3', 4, 16000.00);
commit;

-- проверка количества записей в таблицах
select count(*) from orders;
select count(*) from order_items;
-- ответы: 7 и 1_000_003

--неуспешная транзакция = не положили цену в последнюю вставку товара.
begin transaction isolation level repeatable read;
    insert into orders (id, customer_id, order_date)
        values (8, 1, '2025-02-01');
    insert into order_items (order_id, product_name, quantity, price)
        values (8, 'Что-то там крутое1', 6, 15000.00);
    insert into order_items (order_id, product_name, quantity, price)
        values (8, 'Что-то там крутое2', 4, 13000.00);
    insert into order_items (order_id, product_name, quantity, price)
        values (8, 'Что-то там крутое3', 8);
rollback;


-- проверка количества записей в таблицах/
select count(*) from orders;
select count(*) from order_items;
-- ответы: 7 и 1_000_003

-- ИТОГ - все вставки откатились!
