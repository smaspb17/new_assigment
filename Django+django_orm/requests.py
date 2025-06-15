from django.db.models import Count, F, Q, Avg

# БАЗОВЫЕ ФИЛЬТРЫ

from new_app.models import Author, Book, Review
from datetime import date, time

# =============================================================================================================
# Найди всех авторов с именем «John».

Author.objects.filter(first_name='John')
# SELECT "new_app_author"."id",
#        "new_app_author"."first_name",
#        "new_app_author"."last_name",
#        "new_app_author"."email",
#        "new_app_author"."is_active"
#   FROM "new_app_author"
#  WHERE "new_app_author"."first_name" = 'John'
#  LIMIT 21
# Execution time: 0.001833s [Database: default]
# <QuerySet []>


# =============================================================================================================
# Найди всех авторов, кроме тех, у кого фамилия «Doe».
Author.objects.filter(last_name='Doe')
# SELECT "new_app_author"."id",
#        "new_app_author"."first_name",
#        "new_app_author"."last_name",
#        "new_app_author"."email",
#        "new_app_author"."is_active"
#   FROM "new_app_author"
#  WHERE "new_app_author"."last_name" = 'Doe'
#  LIMIT 21
# Execution time: 0.004408s [Database: default]
# <QuerySet []>


# =============================================================================================================
# ЧИСЛОВЫЕ ЗНАЧЕНИЯ
# Найди все книги, цена которых меньше 500.

Book.objects.filter(price__lt=500)
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE "new_app_book"."price" < '500'
#  LIMIT 21
# Execution time: 0.002269s [Database: default]
# <QuerySet [<Book: Book object (1)>, <Book: Book object (2)>, <Book: Book object (3)>, <Book: Book object (4)>, <Book: Book object (5)>, <Book: Book object (6)>, <Book: Book object (7)>, <Book: Book object (8)>, <Book: Book objec
# t (9)>, <Book: Book object (10)>, <Book: Book object (11)>, <Book: Book object (12)>, <Book: Book object (13)>, <Book: Book object (14)>, <Book: Book object (15)>, <Book: Book object (16)>, <Book: Book object (17)>, <Book: Book object (18)>, <Book: Book object (19)>, <Book: Book object (20)>, '...(remaining elements truncated)...']>


# =============================================================================================================

# Найди все книги с ценой не более 300.
Book.objects.filter(price__lte=300)
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE "new_app_book"."price" <= '300'
#  LIMIT 21
# Execution time: 0.002026s [Database: default]
# <QuerySet [<Book: Book object (1)>, <Book: Book object (2)>, <Book: Book object (3)>, <Book: Book object (4)>, <Book: Book object (5)>, <Book: Book object (6)>, <Book: Book object (7)>, <Book: Book object (8)>, <Book: Book objec
# t (9)>, <Book: Book object (10)>, <Book: Book object (11)>, <Book: Book object (12)>, <Book: Book object (13)>, <Book: Book object (14)>, <Book: Book object (15)>, <Book: Book object (16)>, <Book: Book object (17)>, <Book: Book object (18)>, <Book: Book object (19)>, <Book: Book object (20)>, '...(remaining elements truncated)...']>

# =============================================================================================================

# найди все книги дороже 1000.

Book.objects.filter(price__gt=1000)
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE "new_app_book"."price" > '1000'
#  LIMIT 21
# Execution time: 0.006983s [Database: default]
# <QuerySet []>


# =============================================================================================================

# Найди все книги с ценой от 750 и выше.

Book.objects.filter(price__gte=750)
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE "new_app_book"."price" >= '750'
#  LIMIT 21
# Execution time: 0.002023s [Database: default]
# <QuerySet []>


# =============================================================================================================

# ПОИСК ТЕКСТА

# Найди все книги, содержащие слово «django» в названии.

Book.objects.filter(title__contains='django')
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE "new_app_book"."title" LIKE '%django%' ESCAPE '\'
#  LIMIT 21
# Execution time: 0.002252s [Database: default]
# <QuerySet []>


# =============================================================================================================

# Найди книги, в названии которых есть «python» (без учёта регистра).

Book.objects.filter(title__icontains='python')
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE "new_app_book"."title" LIKE '%python%' ESCAPE '\'
#  LIMIT 21
# Execution time: 0.002449s [Database: default]
# <QuerySet []>


# =============================================================================================================

# Найди книги, название которых начинается со слова «Advanced».

Book.objects.filter(title__startswith='Advanced')
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE "new_app_book"."title" LIKE 'Advanced%' ESCAPE '\'
#  LIMIT 21
# Execution time: 0.002069s [Database: default]
# <QuerySet []>


# =============================================================================================================


# Найди книги, название которых начинается с «pro» (игнорируя регистр).

Book.objects.filter(title__istartswith='pro')
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE "new_app_book"."title" LIKE 'pro%' ESCAPE '\'
#  LIMIT 21
# Execution time: 0.001818s [Database: default]
# <QuerySet [<Book: Book object (881)>]>


# =============================================================================================================

# Найди книги, название которых заканчивается на слово «Guide».

Book.objects.filter(title__endswith='Guide')
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE "new_app_book"."title" LIKE '%Guide' ESCAPE '\'
#  LIMIT 21
# Execution time: 0.002260s [Database: default]
# <QuerySet []>



# =============================================================================================================


# Найди книги, название которых заканчивается на «tutorial» (без учёта регистра).

Book.objects.filter(title__iendswith='tutorial')
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE "new_app_book"."title" LIKE '%tutorial' ESCAPE '\'
#  LIMIT 21
# Execution time: 0.002230s [Database: default]
# <QuerySet []>



# =============================================================================================================

# Проверка на null
# Найди все отзывы без комментариев.

Review.objects.filter(comment__isnull=True)
# SELECT "new_app_review"."id",
#        "new_app_review"."book_id",
#        "new_app_review"."rating",
#        "new_app_review"."comment",
#        "new_app_review"."created_at"
#   FROM "new_app_review"
#  WHERE "new_app_review"."comment" IS NULL
#  LIMIT 21
# Execution time: 0.002141s [Database: default]
# <QuerySet []>


# =============================================================================================================

# Найди все отзывы, у которых есть комментарий.

Review.objects.filter(comment__isnull=False)
# SELECT "new_app_review"."id",
#        "new_app_review"."book_id",
#        "new_app_review"."rating",
#        "new_app_review"."comment",
#        "new_app_review"."created_at"
#   FROM "new_app_review"
#  WHERE "new_app_review"."comment" IS NOT NULL
#  LIMIT 21
# Execution time: 0.002212s [Database: default]
# <QuerySet [<Review: Review object (1)>, <Review: Review object (2)>, <Review: Review object (3)>, <Review: Review object (4)>, <Review: Review object (5)>, <Review: Review object (6)>, <Review: Review object (7)>, <Review: Revie
# w object (8)>, <Review: Review object (9)>, <Review: Review object (10)>, <Review: Review object (11)>, <Review: Review object (12)>, <Review: Review object (13)>, <Review: Review object (14)>, <Review: Review object (15)>, <Review: Review object (16)>, <Review: Review object (17)>, <Review: Review object (18)>, <Review: Review object (19)>, <Review: Review object (20)>, '...(remaining elements truncated)...']>


# =============================================================================================================

# IN И RANGE
# Найди авторов с идентификаторами 1, 3 и 5.

Author.objects.filter(id__in=[1, 3, 5])
# SELECT "new_app_author"."id",
#        "new_app_author"."first_name",
#        "new_app_author"."last_name",
#        "new_app_author"."email",
#        "new_app_author"."is_active"
#   FROM "new_app_author"
#  WHERE "new_app_author"."id" IN (1, 3, 5)
#  LIMIT 21
# Execution time: 0.003951s [Database: default]
# <QuerySet [<Author: Author object (1)>, <Author: Author object (3)>, <Author: Author object (5)>]>


# =============================================================================================================

# Найди книги, опубликованные с 1 января по 31 декабря 2023 года.

Book.objects.filter(published_date__range=['2023-01-01', '2023-12-31'])
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE "new_app_book"."published_date" BETWEEN '2023-01-01 00:00:00' AND '2023-12-31 00:00:00'
#  LIMIT 21
# Execution time: 0.008652s [Database: default]
# <QuerySet []>


# =============================================================================================================

# РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ
# Найди книги, название которых начинается со слова «Python».

Book.objects.filter(title__regex=r'^\bPython\b')
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE "new_app_book"."title" REGEXP '^\bPython\b'
#  LIMIT 21
# Execution time: 0.005574s [Database: default]
# <QuerySet []>


# =============================================================================================================

# Найди авторов, чья фамилия начинается на «Mc» (игнорируя регистр).

Author.objects.filter(last_name__iregex=r'^Mc')
# SELECT "new_app_author"."id",
#        "new_app_author"."first_name",
#        "new_app_author"."last_name",
#        "new_app_author"."email",
#        "new_app_author"."is_active"
#   FROM "new_app_author"
#  WHERE "new_app_author"."last_name" REGEXP '(?i)' || '^Mc'
#  LIMIT 21
# Execution time: 0.002074s [Database: default]
# <QuerySet [<Author: Author object (42)>, <Author: Author object (69)>, <Author: Author object (305)>, <Auth
# or: Author object (311)>, <Author: Author object (340)>, <Author: Author object (403)>, <Author: Author obj
# ect (470)>, <Author: Author object (618)>, <Author: Author object (711)>, <Author: Author object (762)>, <A
# uthor: Author object (782)>, <Author: Author object (843)>, <Author: Author object (879)>, <Author: Author object (906)>]>


# =============================================================================================================

# ДАТЫ И ВРЕМЯ
# Найди книги, опубликованные в 2024 году.

Book.objects.filter(published_date__year=2024)
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE "new_app_book"."published_date" BETWEEN '2024-01-01 00:00:00' AND '2024-12-31 23:59:59.999999'
#  LIMIT 21
# Execution time: 0.001758s [Database: default]
# <QuerySet [<Book: Book object (2)>, <Book: Book object (5)>, <Book: Book object (6)>, <Book: Book object (8
# )>, <Book: Book object (10)>, <Book: Book object (11)>, <Book: Book object (13)>, <Book: Book object (15)>,
#  <Book: Book object (16)>, <Book: Book object (19)>, <Book: Book object (21)>, <Book: Book object (22)>, <B
# ook: Book object (23)>, <Book: Book object (24)>, <Book: Book object (25)>, <Book: Book object (26)>, <Book
# : Book object (27)>, <Book: Book object (29)>, <Book: Book object (35)>, <Book: Book object (36)>, '...(remaining elements truncated)...']>


# =============================================================================================================

# Найди книги, опубликованные в июне.

Book.objects.filter(published_date__month=6)
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE django_datetime_extract('month', "new_app_book"."published_date", NULL, NULL) = 6
#  LIMIT 21
# Execution time: 0.002109s [Database: default]
# <QuerySet [<Book: Book object (19)>, <Book: Book object (32)>, <Book: Book object (36)>, <Book: Book object
#  (44)>, <Book: Book object (53)>, <Book: Book object (62)>, <Book: Book object (83)>, <Book: Book object (9
# 4)>, <Book: Book object (117)>, <Book: Book object (202)>, <Book: Book object (245)>, <Book: Book object (2
# 48)>, <Book: Book object (274)>, <Book: Book object (275)>, <Book: Book object (292)>, <Book: Book object (
# 299)>, <Book: Book object (304)>, <Book: Book object (307)>, <Book: Book object (309)>, <Book: Book object (317)>, '...(remaining elements truncated)...']>


# =============================================================================================================

# Найди отзывы, оставленные 11-го числа любого месяца.

Book.objects.filter(published_date__day=11)
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE django_datetime_extract('day', "new_app_book"."published_date", NULL, NULL) = 11
#  LIMIT 21
# Execution time: 0.001733s [Database: default]
# <QuerySet [<Book: Book object (1)>, <Book: Book object (24)>, <Book: Book object (37)>, <Book: Book object
# (41)>, <Book: Book object (43)>, <Book: Book object (138)>, <Book: Book object (185)>, <Book: Book object (
# 214)>, <Book: Book object (217)>, <Book: Book object (255)>, <Book: Book object (283)>, <Book: Book object
# (347)>, <Book: Book object (444)>, <Book: Book object (448)>, <Book: Book object (494)>, <Book: Book object
#  (561)>, <Book: Book object (680)>, <Book: Book object (745)>, <Book: Book object (843)>, <Book: Book object (850)>, '...(remaining elements truncated)...']>


# =============================================================================================================

# Найди книги, опубликованные на 23-й неделе года.

Book.objects.filter(published_date__week=23)
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE django_datetime_extract('week', "new_app_book"."published_date", NULL, NULL) = 23
#  LIMIT 21
# Execution time: 0.002465s [Database: default]
# <QuerySet [<Book: Book object (83)>, <Book: Book object (202)>, <Book: Book object (245)>, <Book: Book obje
# ct (304)>, <Book: Book object (307)>, <Book: Book object (338)>, <Book: Book object (367)>, <Book: Book obj
# ect (372)>, <Book: Book object (406)>, <Book: Book object (472)>, <Book: Book object (572)>, <Book: Book ob
# ject (613)>, <Book: Book object (781)>, <Book: Book object (849)>, <Book: Book object (868)>, <Book: Book object (919)>, <Book: Book object (943)>, <Book: Book object (988)>]>


# =============================================================================================================

# Найди отзывы, оставленные во вторник.

Book.objects.filter(published_date__week_day=3)
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE django_datetime_extract('week_day', "new_app_book"."published_date", NULL, NULL) = 3
#  LIMIT 21
# Execution time: 0.001951s [Database: default]
# <QuerySet [<Book: Book object (20)>, <Book: Book object (32)>, <Book: Book object (38)>, <Book: Book object
#  (47)>, <Book: Book object (48)>, <Book: Book object (49)>, <Book: Book object (58)>, <Book: Book object (5
# 9)>, <Book: Book object (60)>, <Book: Book object (72)>, <Book: Book object (80)>, <Book: Book object (82)>
# , <Book: Book object (96)>, <Book: Book object (97)>, <Book: Book object (106)>, <Book: Book object (111)>,
#  <Book: Book object (119)>, <Book: Book object (129)>, <Book: Book object (135)>, <Book: Book object (146)>, '...(remaining elements truncated)...']>


# =============================================================================================================


# Найди книги, опубликованные во втором квартале года.

Book.objects.filter(published_date__month__in=[4,5,6])
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE django_datetime_extract('month', "new_app_book"."published_date", NULL, NULL) IN (4, 5, 6)
#  LIMIT 21
# Execution time: 0.002125s [Database: default]
# <QuerySet [<Book: Book object (1)>, <Book: Book object (7)>, <Book: Book object (14)>, <Book: Book object (
# 18)>, <Book: Book object (19)>, <Book: Book object (20)>, <Book: Book object (30)>, <Book: Book object (32)
# >, <Book: Book object (34)>, <Book: Book object (36)>, <Book: Book object (37)>, <Book: Book object (44)>,
# <Book: Book object (46)>, <Book: Book object (53)>, <Book: Book object (62)>, <Book: Book object (64)>, <Bo
# ok: Book object (66)>, <Book: Book object (69)>, <Book: Book object (74)>, <Book: Book object (77)>, '...(remaining elements truncated)...']>


# =============================================================================================================

# Найди отзывы, сделанные в определённую дату.

Review.objects.filter(created_at__date=date(2024, 6, 28))
# SELECT "new_app_review"."id",
#        "new_app_review"."book_id",
#        "new_app_review"."rating",
#        "new_app_review"."comment",
#        "new_app_review"."created_at"
#   FROM "new_app_review"
#  WHERE django_datetime_cast_date("new_app_review"."created_at", 'UTC', 'UTC') = '2024-06-28'
#  LIMIT 21
# Execution time: 0.003817s [Database: default]
# <QuerySet [<Review: Review object (12)>, <Review: Review object (233)>, <Review: Review object (577)>, <Review: Review object (900)>]>



# =============================================================================================================


# Найди отзывы, сделанные ровно в 15:30.

Review.objects.filter(created_at__time=time(16, 20))
# SELECT "new_app_review"."id",
#        "new_app_review"."book_id",
#        "new_app_review"."rating",
#        "new_app_review"."comment",
#        "new_app_review"."created_at"
#   FROM "new_app_review"
#  WHERE django_datetime_cast_time("new_app_review"."created_at", 'UTC', 'UTC') = '16:20:00'
#  LIMIT 21
# Execution time: 0.001880s [Database: default]
# <QuerySet [<Review: Review object (5)>]>


# =============================================================================================================

# Найди отзывы, сделанные в 15 часов.

Review.objects.filter(created_at__hour=15)
# SELECT "new_app_review"."id",
#        "new_app_review"."book_id",
#        "new_app_review"."rating",
#        "new_app_review"."comment",
#        "new_app_review"."created_at"
#   FROM "new_app_review"
#  WHERE django_datetime_extract('hour', "new_app_review"."created_at", 'UTC', 'UTC') = 15
#  LIMIT 21
# Execution time: 0.003198s [Database: default]
# <QuerySet [<Review: Review object (66)>, <Review: Review object (69)>, <Review: Review object (85)>, <Revie
# w: Review object (92)>, <Review: Review object (164)>, <Review: Review object (167)>, <Review: Review objec
# t (193)>, <Review: Review object (247)>, <Review: Review object (257)>, <Review: Review object (306)>, <Rev
# iew: Review object (319)>, <Review: Review object (376)>, <Review: Review object (384)>, <Review: Review ob
# ject (389)>, <Review: Review object (407)>, <Review: Review object (466)>, <Review: Review object (472)>, <
# Review: Review object (486)>, <Review: Review object (505)>, <Review: Review object (537)>, '...(remaining elements truncated)...']>

# =============================================================================================================

# Найди отзывы, сделанные в 30 минут любого часа.

Review.objects.filter(created_at__minute=30)
# SELECT "new_app_review"."id",
#        "new_app_review"."book_id",
#        "new_app_review"."rating",
#        "new_app_review"."comment",
#        "new_app_review"."created_at"
#   FROM "new_app_review"
#  WHERE django_datetime_extract('minute', "new_app_review"."created_at", 'UTC', 'UTC') = 30
#  LIMIT 21
# Execution time: 0.003164s [Database: default]
# <QuerySet [<Review: Review object (63)>, <Review: Review object (215)>, <Review: Review object (309)>, <Rev
# iew: Review object (319)>, <Review: Review object (459)>, <Review: Review object (516)>, <Review: Review ob
# ject (626)>, <Review: Review object (660)>, <Review: Review object (751)>, <Review: Review object (878)>, <Review: Review object (884)>, <Review: Review object (898)>, <Review: Review object (967)>]>


# =============================================================================================================


# Найди отзывы, созданные в момент, когда секунды были равны 0.

Review.objects.filter(created_at__second=0)
# SELECT "new_app_review"."id",
#        "new_app_review"."book_id",
#        "new_app_review"."rating",
#        "new_app_review"."comment",
#        "new_app_review"."created_at"
#   FROM "new_app_review"
#  WHERE django_datetime_extract('second', "new_app_review"."created_at", 'UTC', 'UTC') = 0
#  LIMIT 21
# Execution time: 0.002013s [Database: default]
# <QuerySet [<Review: Review object (5)>, <Review: Review object (61)>, <Review: Review object (130)>, <Revie
# w: Review object (229)>, <Review: Review object (322)>, <Review: Review object (328)>, <Review: Review obje
# ct (593)>, <Review: Review object (596)>, <Review: Review object (660)>, <Review: Review object (709)>, <Re
# view: Review object (746)>, <Review: Review object (793)>, <Review: Review object (865)>, <Review: Review object (891)>, <Review: Review object (942)>, <Review: Review object (959)>]>


# =============================================================================================================

# СВЯЗАННЫЕ ПОЛЯ
# Найди книги, написанные автором с почтой «author@example.com».

Book.objects.filter(author__email='kaldind@opensource.org')
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  INNER JOIN "new_app_author"
#     ON ("new_app_book"."author_id" = "new_app_author"."id")
#  WHERE "new_app_author"."email" = 'kaldind@opensource.org'
#  LIMIT 21
# Execution time: 0.003719s [Database: default]
# <QuerySet [<Book: Book object (373)>, <Book: Book object (520)>]>


# =============================================================================================================

# Найди книги авторов, чья фамилия содержит «smith» (без учёта регистра).
Book.objects.filter(author__last_name__icontains='arrabl')
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  INNER JOIN "new_app_author"
#     ON ("new_app_book"."author_id" = "new_app_author"."id")
#  WHERE "new_app_author"."last_name" LIKE '%arrabl%' ESCAPE '\'
#  LIMIT 21
# Execution time: 0.002135s [Database: default]
# <QuerySet [<Book: Book object (356)>]>


# =============================================================================================================

# Найди авторов, написавших более пяти книг.

Author.objects.annotate(book_count=Count('books')).filter(book_count__gt=3)
# SELECT "new_app_author"."id",
#        "new_app_author"."first_name",
#        "new_app_author"."last_name",
#        "new_app_author"."email",
#        "new_app_author"."is_active",
#        COUNT("new_app_book"."id") AS "book_count"
#   FROM "new_app_author"
#   LEFT OUTER JOIN "new_app_book"
#     ON ("new_app_author"."id" = "new_app_book"."author_id")
#  GROUP BY "new_app_author"."id",
#           "new_app_author"."first_name",
#           "new_app_author"."last_name",
#           "new_app_author"."email",
#           "new_app_author"."is_active"
# HAVING COUNT("new_app_book"."id") > 3
#  LIMIT 21
# Execution time: 0.001776s [Database: default]
# <QuerySet [<Author: Author object (554)>, <Author: Author object (847)>, <Author: Author object (174)>, <Au
# thor: Author object (641)>, <Author: Author object (776)>, <Author: Author object (20)>, <Author: Author ob
# ject (139)>, <Author: Author object (189)>, <Author: Author object (945)>, <Author: Author object (405)>, <
# Author: Author object (920)>, <Author: Author object (700)>, <Author: Author object (563)>, <Author: Author object (835)>, <Author: Author object (348)>]>


# =============================================================================================================

# JSON-ПОЛЯ
# Найди книги, у которых значение ключа «origin» равно «green».

books = Book.objects.filter(metadata__origin='green')
# >>> books
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE (CASE WHEN JSON_TYPE("new_app_book"."metadata", '$."origin"') IN ('null','false','true') THEN JSON_T
# YPE("new_app_book"."metadata", '$."origin"') ELSE JSON_EXTRACT("new_app_book"."metadata", '$."origin"') END) = JSON_EXTRACT('"green"', '$')
#  LIMIT 21
# Execution time: 0.001654s [Database: default]


# =============================================================================================================

# Найди книги, где значение ключа «tags» содержит слово «bestseller» (игнорируя регистр).

Book.objects.filter(metadata__tags__icontains="bestseller")
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE (CASE WHEN JSON_TYPE("new_app_book"."metadata", '$."tags"') IN ('null','false','true') THEN JSON_TYP
# E("new_app_book"."metadata", '$."tags"') ELSE JSON_EXTRACT("new_app_book"."metadata", '$."tags"') END) LIKE '%bestseller%' ESCAPE '\'
#  LIMIT 21
# Execution time: 0.003341s [Database: default]
# <QuerySet []>


# =============================================================================================================

# ИСПОЛЬЗОВАНИЕ ВЫРАЖЕНИЙ F И Q
# Найди книги, у которых цена равна скидке.

Book.objects.filter(price=F('discount'))
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE "new_app_book"."price" = ("new_app_book"."discount")
#  LIMIT 21
# Execution time: 0.001673s [Database: default]
# <QuerySet []>



# =============================================================================================================

# Найди книги, у которых цена больше скидки.

Book.objects.filter(price__gt=F('discount'))
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE "new_app_book"."price" > ("new_app_book"."discount")
#  LIMIT 21
# Execution time: 0.001880s [Database: default]


# =============================================================================================================

# Найди авторов с именем «Alice» или с фамилией, не равной «Brown».

Author.objects.filter(Q(first_name='Alice') | ~Q(last_name='Brown'))
# SELECT "new_app_author"."id",
#        "new_app_author"."first_name",
#        "new_app_author"."last_name",
#        "new_app_author"."email",
#        "new_app_author"."is_active"
#   FROM "new_app_author"
#  WHERE ("new_app_author"."first_name" = 'Alice' OR NOT ("new_app_author"."last_name" = 'Brown'))
#  LIMIT 21
# Execution time: 0.002426s [Database: default]
# <QuerySet [<Author: Author object (1)>, <Author: Author object (2)>, <Author: Author object (3)>, <Author:
# Author object (4)>, <Author: Author object (5)>, <Author: Author object (6)>, <Author: Author object (7)>,
# <Author: Author object (8)>, <Author: Author object (9)>, <Author: Author object (10)>, <Author: Author obj
# ect (11)>, <Author: Author object (12)>, <Author: Author object (13)>, <Author: Author object (14)>, <Autho
# r: Author object (15)>, <Author: Author object (16)>, <Author: Author object (17)>, <Author: Author object (18)>, <Author: Author object (19)>, <Author: Author object (20)>, '...(remaining elements truncated)...']>
# >>>


# =============================================================================================================

# ЗАДАНИЯ НА АННОТАЦИИ
# Подсчитай количество книг каждого автора.

authors = Author.objects.annotate(book_count=Count('books'))
for author in authors:
    print(f"{author.first_name} {author.last_name}: {author.book_count} книг")

# SELECT "new_app_author"."id",
#        "new_app_author"."first_name",
#        "new_app_author"."last_name",
#        "new_app_author"."email",
#        "new_app_author"."is_active",
#        COUNT("new_app_book"."id") AS "book_count"
#   FROM "new_app_author"
#   LEFT OUTER JOIN "new_app_book"
#     ON ("new_app_author"."id" = "new_app_book"."author_id")
#  GROUP BY "new_app_author"."id",
#           "new_app_author"."first_name",
#           "new_app_author"."last_name",
#           "new_app_author"."email",
#           "new_app_author"."is_active"
# Execution time: 0.001906s [Database: default]
# Adair Adie: 1 книг
# Alphonse Alred: 3 книг
# Anatola Alwen: 0 книг
# Amalle Barnwall: 2 книг
# Ailee Bexon: 1 книг


# =============================================================================================================

# Подсчитай средний рейтинг каждой книги.

books = Book.objects.annotate(avg_rating=Avg('reviews__rating'))
for book in books:
    print(f"{book.title}: средний рейтинг {book.avg_rating or 'нет оценок'}")

# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata",
#        AVG("new_app_review"."rating") AS "avg_rating"
#   FROM "new_app_book"
#   LEFT OUTER JOIN "new_app_review"
#     ON ("new_app_book"."id" = "new_app_review"."book_id")
#  GROUP BY "new_app_book"."id",
#           "new_app_book"."title",
#           "new_app_book"."author_id",
#           "new_app_book"."published_date",
#           "new_app_book"."price",
#           "new_app_book"."discount",
#           "new_app_book"."metadata"
# Execution time: 0.002585s [Database: default]


# =============================================================================================================

# Посчитай окончательную цену книги (цена минус скидка).

books = Book.objects.annotate(final_price=F('price') - F('discount'))
for book in books:
    print(f"{book.title}: окончательная цена {book.final_price}")
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata",
#        AVG("new_app_review"."rating") AS "avg_rating"
#   FROM "new_app_book"
#   LEFT OUTER JOIN "new_app_review"
#     ON ("new_app_book"."id" = "new_app_review"."book_id")
#  GROUP BY "new_app_book"."id",
#           "new_app_book"."title",
#           "new_app_book"."author_id",
#           "new_app_book"."published_date",
#           "new_app_book"."price",
#           "new_app_book"."discount",
#           "new_app_book"."metadata"
# Execution time: 0.001773s [Database: default]



# =============================================================================================================

# ИСПОЛЬЗОВАНИЕ SELECT_RELATED И PREFETCH_RELATED
# Получи список книг и авторов так, чтобы выполнить всего один SQL-запрос.

Book.objects.select_related('author').all()
# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata",
#        "new_app_author"."id",
#        "new_app_author"."first_name",
#        "new_app_author"."last_name",
#        "new_app_author"."email",
#        "new_app_author"."is_active"
#   FROM "new_app_book"
#  INNER JOIN "new_app_author"
#     ON ("new_app_book"."author_id" = "new_app_author"."id")
#  LIMIT 21
# Execution time: 0.001648s [Database: default]

# =============================================================================================================


# Получи список авторов и всех их книг так, чтобы было выполнено ровно два SQL-запроса.

Author.objects.prefetch_related('books').all()
# SELECT "new_app_author"."id",
#        "new_app_author"."first_name",
#        "new_app_author"."last_name",
#        "new_app_author"."email",
#        "new_app_author"."is_active"
#   FROM "new_app_author"
#  LIMIT 21
# Execution time: 0.001496s [Database: default]

# SELECT "new_app_book"."id",
#        "new_app_book"."title",
#        "new_app_book"."author_id",
#        "new_app_book"."published_date",
#        "new_app_book"."price",
#        "new_app_book"."discount",
#        "new_app_book"."metadata"
#   FROM "new_app_book"
#  WHERE "new_app_book"."author_id" IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)
# Execution time: 0.002501s [Database: default]