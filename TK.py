
# Example_1:
# برنامه بنویسید که اسم و فامیل رو بگیره و جابه جا کنه با فاصله بینش

# name = input('name:')
# family = input('family:')
# print(family +' '+ name )

#........................................................................
# Example_2
# کلمه ایی که از کاربر میگیره به صورت های زیر نمایش بده
# upper case , lower case

# word = input('what is ur word:')
# print(word.lower())
# print(word.upper())
# #or 
# word = input('what is ur word:')
# print(f'your word is {word}')
#........................................................................
# Example_3
# برنامه ایی بنویسی که ۳ عدد از کاربر بگیره و در خروجی مرتب بشه
# با توابع max , min

# a = int(input('a:'))
# b = int(input('b:'))
# c = int(input('c:'))
# ma = max(a,b,c)
# mi = min(a,b,c)
# middle = (a+b+c)-ma-mi
# print(f'number is sorted {ma, middle, mi}')
#........................................................................
# Example_4
# برنامه ایی بنویسید که عدد دریافتی رو از کاربربگیره و بگه زوج یا فرد

# num = int(input('enter number: '))
# mod = num % 2
# if mod == 0:
#     print('adad zoj ast')
# else:
#     print('adad fard ast')
#........................................................................
# Example_5
# برنامه ایی بنویسید که ۴ کاراکتر اول یک استرینگ رو حروف کوچک کنه

# string = input('strin:')
# print(string[:4].lower()+string[4:])
#........................................................................
# Example_5
# تابعی بنویسید که استرینگ دریافت کنه و کاراکتر اول و آخر رو جابهجا کنه

# str_1 = input('enter ur str_1:') # =====> جای خالی برای زیباییه؟
# s = str_1[0]                      # چرا روش اول جواب نمیده
# e = str_1[-1]
# try:
#     print(e+(str_1-s-e)+s)
# except Exception as e:
#     print(e)

#or
#salam
#malas

# str_1 = input('enter ur str_1: ') 
# s = str_1[0]
# e = str_1[-1]
# main = str_1[1:-1]
# print(e+main+s)

# function input output
# def replacing(string_):
#     s = string_[0]
#     e = string_[-1]
#     main = string_[1:-1]
#     return (e+main+s)


# x = input('enter ur str_1: ') 
# x = replacing(x)
# print(x)


# def sum_1(a,b):
#     c = a+b
#     return (c)

# a = 4
# b = 5
# print(sum_1(a,b))







#........................................................................
# Example_6
# تابعی که جمع ۳ تاعدد روبده ولی اگر دوتاشون یکی بودند صفر برگردونه

# def sum(x,y,z):
#     if x == y or y == z or x == z:
#         sum = 0
#     else:
#         sum = x + y + z
#     return sum
# print(sum(6,3,1))
# print(sum(6,3,3))
#........................................................................
# Example_7                                              ========> بلد نیستم
# تابعی که اگر متن دادیم بگه هر کلمه چند بار تکرار شده
# x =  "the quick brown for jums over the lazy dog."


# 1) entekhab yek esm baraye tabe 
# 2) vorodi tabe anjam shava. masalan baraye jame do adad bayad do argoman dashte bashim
# 3)mavaredi ke mikhahim dar badane functione neveshte shavad
# 4)haaaaatman bayad return dashte bashim. khoroji
# 5) ta inja kar ba sakhtar tabe tamam ast 
# 1-1)farakhani function bayad esme tabe neveshte shavad. argoman be haman meghdar ersal shavad
# 1-2) barabar ye moteghaye shavad
# 1-3)print shavad
# def counter_1(x):
#     list_1 = x.split(" ")
#     counter = 0
#     for y in list_1:
#         if y == 'the':
#             counter += 1
#     return counter
# a = counter_1(x)
# print(a )

#........................................................................
# Example_8                                              
# تابعی که کلیه حروف رو بزرگ کنه
# به شرطی که حداقل ۲ کاراکتربا جروف بزرگ باشد ولی در ۴ کاراکتر اول


# =====> تابع رو باید خوب بخونم بعد حل کنم



#........................................................................
# Example_9                                              
# برنامه ایی بنویس که یک تاپل رو به استرینگ تبدیل کنه

# tup = ('d','e','v','l','o','p','e','r')
# str_1 = ''.join(tup)
# print(str_1)

#........................................................................
# Example_10
# یک آیتم رو به تاپل اضافه کن

# آخرش اضافه بشه
# a = (4,6,2,8,3,1)
# a = a + (9,)
# print(a)                                              

# وسطش اضافه بشه
# a = (4,6,2,8,3,1)
# a = a[:2] + (15,80,40) + a[2:]
# print(a)

# یه راه دیکه اینکه به لیست تبدیل کنیم
# a = (4,6,2,8,3,1)
# list_x  = list(a)
# list_x.append(99)
# a = tuple(list_x)
# print(a)

# برای پاک کردن
# a = (4,6,2,8,3,1)
# listx = list(a)
# listx.remove(8)
# a = tuple(listx)
# print(a)    
#........................................................................
# Example_11
# برنامه ایی که چک کنه یک المنت در تاپلی وجود داره یا نه

# a = (4,6,2,8,3,1)
# print(8 in a)
#........................................................................
# Example_12
# تعداد تکرار یک عضو

# a = 2,4,5,6,2,3,4,4,7
# count = a.count(4)
# print(count)
#........................................................................
# Example_13
# برنامه ایی که چهارمین کاراکتراز اول و از آخر رو چاپ کنه

# a = 'helloworld is one of the special word'
# print(a[3],a[-4])
#........................................................................
# Example_14
# تاپل شده یک استرینگ به صورت ریورز

# x = ('pedram')
# y = reversed(x)
# print(tuple(y))
#........................................................................
# Example_15
# تابعی که چک کنه یک کلید داخل دیکشنری هست یا نه

# d = {1: 10, 2:20, 3:30, 4:40, 5:50, 6:60}

# def is_key_present(x):
#     if x in d:
#         print('kilid bood')
#     else:
#         print('kilid nabood')
# is_key_present(60)
#........................................................................
# Example_16
# برنامه ایی که یک کلید رو از دیکشنری پاک کنه

# d = {1: 10, 2:20, 3:30, 4:40, 5:50, 6:60}
# if 2 in d:
#     del d[2]
# print(d)
#........................................................................
# Example_17                                                   ======> بلد نیستم
# برنامه ایی که عضو های داخل دیکشنری رو به شکل زیر دربیاره
# 'a' --> '55

# d = {'a': 10, 'b':20, 'c':30, 'd':40, 'e':50, 'f':60}
# for dict_key, dict_value, in d.items():
#     print(dict_key, '-->', dict_value) 
#........................................................................
# Example_18                                                   ======> بلد نیستم
# برنامه ایی که دوتا دیکشنریرو مرج بکنه

# d1 = {'a':100, 'b':200}
# d2 = {'x': 300, 'y':200}

# d = []

# for x,y in d1.items():
#     d.append({x:y})    

# for x,y in d2.items():
#     d.append({x:y}) 

# print(d)

#........................................................................
# Example_19                                                   ======> بلد نیستم
# دیکشنر که بتوان تمام ولیو ها را باهم جمع کرد

# d = {'a': 10, 'b':20, 'c':30, 'd':40, 'e':50, 'f':60}
# sum_1 = 0
# for x,y in d.items():
#     try:
#         sum_1 = sum_1 + y
#     except:
#         pass

# print(sum_1)


# print(sum([y for x,y in d.items()]))
# استاد:‌میتوان انگونه در یک خط نیز نوشتُ در ظاهر حرفه ایی هست
# اما بهتره استاندارد و زیر هم نوشته بشه که بعدا اگر بخوای دولوپ کنی بتونی بخونیش
# یا اگر کد رو به کس دیگه ایی میدیُ‌بتونه روش کار کنه
#........................................................................















# for
# x = "pedram"
# # p e d r a m

# for a in x:
#     print(a)


# 2) pedram ==> p

# 3) change => def
#x = "salam man robot hastam"
# salam man pedram hastam

# 4) input(time by sec)ex:5s
# print()


sjfnsjdfnksjdfidfghi














