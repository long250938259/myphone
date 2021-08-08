import flask, json
import pymysql
from flask_cors import *

from flask_basicauth import *

server = flask.Flask(__name__)
CORS(server, supports_credentials=True)


@server.route("/search", methods=['get'])
def search():
    name = flask.request.values.get('name')
    if name:
        try:
            con = pymysql.connect(host="192.168.174.128", user="root", password="123456", db="mydatabase", port=3306, charset="utf8")
            cursorl = con.cursor()
            cursorl.execute("select name,phone from test_you where name = %s", (name,))
            d = cursorl.fetchall()
            print(d)
            con.commit()
            cursorl.close()
            con.close()
            res = {
                "code": 200,
                "msg": d
            }
            return json.dumps(res, ensure_ascii=False)
        except Exception as e:
            print(e)
    else:
        res = {"msg": "失败"}
        return json.dumps(res, ensure_ascii=False)


@server.route("/all", methods=['get'])
def all():
    try:
        con = pymysql.connect(host="192.168.174.128", user="root", password="123456", db="mydatabase", port=3306,
                              charset="utf8")
        cursorl = con.cursor()
        cursorl.execute("select name,phone from test_you")
        d = cursorl.fetchall()
        print(d)
        con.commit()
        cursorl.close()
        con.close()
        res = {
            # "code": 200,
            "msg": d
        }
        return json.dumps(res, ensure_ascii=False)
    except Exception as e:
        print(e)
    else:
        res = {"msg": "失败"}
        return json.dumps(res, ensure_ascii=False)

@server.route('/add', methods=['post'])
def add():
    add_name = flask.request.values.get('name')
    add_num = flask.request.values.get('num')
    if add_num and add_name:
        try:
            con = pymysql.connect(host="192.168.174.128", user="root", password="123456", db="mydatabase", port=3306,
                              charset="utf8")
            cursorl = con.cursor()
            cursorl.execute("insert into test_you(name, phone) values (%s, %s)", (add_name, add_num))
            con.commit()
            cursorl.close()
            con.close()
        except Exception as e:
            print(e)
        res = {
            "code": 200,
            "msg": "新增成功！"
        }
        return json.dumps(res, ensure_ascii=False)
    else:
        res = {
            "msg": "请输入姓名和手机号"
        }
        return json.dumps(res, ensure_ascii=False)

@server.route('/delete', methods=['delete',])
def delete():
    del_name = flask.request.values.get('name')
    if del_name:
        try:
            con = pymysql.connect(host="192.168.174.128", user="root", password="123456", db="mydatabase", port=3306,
                              charset="utf8")
            cursorl = con.cursor()
            cursorl.execute("delete from test_you where name = %s", (del_name,))
            con.commit()
            cursorl.close()
            con.close()
        except Exception as e:
            print(e)
        res = {"msg": '删除成功！'}
        return json.dumps(res, ensure_ascii=False)
    else:
        res = {'msg': "请输入姓名！"}
        return json.dumps(res, ensure_ascii=False)







#     res = {
#         'code': 200,
#         'msg': "龙龙真是太帅了！"
#     }
#     return json.dumps(res, ensure_ascii=False)
#
#


server.run(port=8888, debug=True, host="127.0.0.1")



