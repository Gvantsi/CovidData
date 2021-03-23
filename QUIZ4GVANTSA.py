# import sqlite3
#
# conn = sqlite3.connect("covid_dataset.sqlite")
# cursor = conn.cursor()
#
# result = cursor.execute("SELECT total_cases FROM covid WHERE location='France' and date ='2020-05-31' ")
# for i in result:
#     print(f'საფრანგეთში 31 მაისს ინფიცირებულთა ჯამური რაოდენობაა:{i[0]}')
#
#
# def new_cases(date, iso_code):
#     result = cursor.execute(f"SELECT new_cases FROM covid WHERE iso_code='{iso_code}' and date ='{date}'")
#     for case in result:
#         print(f'{iso_code} , {date} - ში ახალ დაინფიცირებულთა რაოდენობაა:{case[0]}')
#
#
# new_cases('2020-05-31', "FRANCE")
#
#
# def top5():
#     top5 = cursor.execute("SELECT distinct total_deaths_per_million "
#                           "from covid"
#                           "WHERE date='2020-06-02'"
#                           "order by 1 desc ").fetchmany(5)
#     for each in top5:
#         print(each[0])
#
#
# top5()
# x = cursor.execute(" Select distinct total_cases from covid where location = 'China' order by total_cases desc ").fetchmany(20)
# xx = []
# for i in x:
#     xx.append(i[0])
# y = cursor.execute("Select distinct date from covid where location = 'China' order by total_cases desc ").fetchmany(20)
# yy = []
# for j in y:
#     yy.append(j[0])
# plt.plot(xx,yy,marker="o",ls="-",color="g",label='სულ შემთხვევები')
# plt.xlabel("ინფიცირებულები")
# plt.ylabel("თარიღი")
# plt.legend()
# plt.show()
#
# '''მოკლედ მე გავაკეთე ჰისტოგრამა და გადავწყვიტე გამომეყენებინა ქვეყანა ჩინეთი '''
#
# conn.close()
