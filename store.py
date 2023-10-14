import sqlite3
import hashlib


def create_database():
    conn = sqlite3.connect('user_data.db')  # 创建一个名为user_data.db的数据库
    c = conn.cursor()

    # 创建一个名为users的表，如果它不存在的话
    c.execute('''  
              CREATE TABLE IF NOT EXISTS users(  
              username TEXT NOT NULL,  
              password TEXT NOT NULL);  
              ''')
    conn.commit()
    conn.close()


def check_user(username, password): #查找密码
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()

    # 在users表中查找用户名
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()

    if user is None:                #第一次登录即注册
        # 如果找不到用户，将用户名和密码关联起来存入数据库并返回1
        password = password_md5(password)       #将密码加密
        c.execute("INSERT INTO users VALUES (?,?)", (username, password))
        conn.commit()
        return 1
    else:
        # 如果找到用户，判断收到的密码与储存的密码是否相同，相同则返回2，不相同则返回3
        password = password_md5(password)  # 将密码加密
        if user[1] == password:
            return 2
        else:
            return 3


def password_md5(password):#密码加密
    # 创建一个md5对象
    md5 = hashlib.md5()

    # 给md5对象提供要加密的数据，需要先将其转换为字节
    md5.update(password.encode('utf-8'))

    # 获取哈希值并以16进制字符串的形式返回
    result = md5.hexdigest()
    return result

def shuchu():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    results = c.fetchall()
    for row in results:
        print(row)
    conn.close()


#shuchu()
