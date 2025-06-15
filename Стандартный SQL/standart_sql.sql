
-- Этап Стандартный SQL: Создание структуры базы данных

create database new_issue;

create table customers
(
    id    bigserial primary key,
    name  varchar(128),
    email varchar(129) unique
);

create table orders (
    id bigserial primary key,
    customer_id int references customers(id),
    order_date date
);

create table order_items (
    id bigserial primary key,
    order_id int references orders(id),
    product_name varchar(128),
    quantity int,
    price decimal(10, 2)
);

-- ===========================================================================================================================================

-- Этап 2: Наполнение тестовыми данными


insert into customers(name, email) values ('Customer1', 'email1@mail.ru');
insert into customers(name, email) values ('Customer2', 'email2@mail.ru');
insert into customers(name, email) values ('Customer3', 'email3@mail.ru');

insert into orders(customer_id, order_date) values (1, '2025-01-01');
insert into orders(customer_id, order_date) values (1, '2025-01-02');
insert into orders(customer_id, order_date) values (2, '2025-01-03');
insert into orders(customer_id, order_date) values (2, '2025-01-04');
insert into orders(customer_id, order_date) values (3, '2025-01-05');
insert into orders(customer_id, order_date) values (3, '2025-01-06');

insert into order_items(order_id, product_name, quantity, price) values (1, 'Product1', 4, 10000);
insert into order_items(order_id, product_name, quantity, price) values (1, 'Product1', 6, 7000);
insert into order_items(order_id, product_name, quantity, price) values (2, 'Product1', 8, 4000);
insert into order_items(order_id, product_name, quantity, price) values (2, 'Product1', 10, 8000);
insert into order_items(order_id, product_name, quantity, price) values (3, 'Product1', 3, 9000);
insert into order_items(order_id, product_name, quantity, price) values (3, 'Product1', 5, 10000);

-- ===========================================================================================================================================

-- Этап 3: Запросы на чтение

-- Задание Стандартный SQL: Простая фильтрация
select o.id, o.order_date
from orders as o
join customers as s on o.customer_id = s.id
where s.name = 'Customer1';

-- Задание 2: Фильтрация + сортировка
select product_name, quantity, price
from order_items
where order_id = 3
order by price desc;

-- Задание 3: Группировка + фильтрация
select c.name, sum(oi.price * oi.quantity) as total_spent
from customers as c
join orders as o on c.id = o.customer_id
join order_items as oi on o.id = oi.order_id
group by c.id, c.name
having sum(oi.price * oi.quantity) > 5000;
