import pymysql


book = {}

while True:
    print("="*30)
    print("欢迎来到通讯录：")
    print("1.查询联系人资料\n" + "2.新增或修改联系人资料\n" + "3.删除联系人\n" + "4.查看所有联系人\n" + "5.退出")
    b = int(input("请选择业务："))

    if b == 1:
        search_name = input("请输入姓名：")
        try:
            con = pymysql.connect(host="192.168.174.128", user="root", password="123456", db="mydatabase", port=3306)
            cursorl = con.cursor()
            cursorl.execute("select name,phone from test_you where name = %s ", (search_name, ))
            fetch = cursorl.fetchall()
            print(fetch)
            con.commit()
            cursorl.close()
            con.close()
        except Exception as e:
            print(e)
        # if search_name in book.keys():
        #     print("姓名：{}\t 电话：{}".format(search_name, book[search_name][0]))
        # else:
        #     print("未找到联系人！")

    elif b == 2:
        name, phone = [input("请输入{}：".format(key)) for key in ("姓名", "电话")]
        book[name] = phone
        print("添加成功！")
        try:
            con = pymysql.connect(host="192.168.174.128", user="root", password="123456", db="mydatabase", port=3306)
            cursorl = con.cursor()
            cursorl.execute("INSERT INTO test_you (name, phone) VALUES (%s, %s)", (str(name), phone))
            # sql = "INSERT INTO test_you (name, phone) VALUES (\"%s\", \"%s\")", (str(name), str(phone))
            # cursorl.execute(sql)
            con.commit()
            cursorl.close()
            con.close()
        except Exception as e:
            print(e)

    elif b == 3:
        del_name = input("请输入姓名：")
        try:
            con = pymysql.connect(host="192.168.174.128", user="root", password="123456", db="mydatabase", port=3306)
            cursorl = con.cursor()
            cursorl.execute("delete from test_you where name = %s ", (del_name, ))
            print("删除成功！")
            con.commit()
            cursorl.close()
            con.close()
        except Exception as e:
            print(e)

        # if del_name in book.keys():
        #     book.pop(del_name)
        #     print("删除成功！")
        # else:
        #     print("未找到联系人！")

    elif b == 4:
        try:
            con = pymysql.connect(host="192.168.174.128", user="root", password="123456", db="mydatabase", port=3306)
            cursorl = con.cursor()
            cursorl.execute("select name,phone from test_you ")
            all = cursorl.fetchall()
            print(all)
            con.commit()
            cursorl.close()
            con.close()
        except Exception as e:
            print(e)
        # print("当前的全部联系人：")
        # for name, phone in book.items():
        #     print("姓名：{}\t电话：{}".format(name, phone[0]))

    elif b == 5:
        print("已退出！")

    else:
        print("请在1-4中选择！")












