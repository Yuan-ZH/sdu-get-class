import Users
import time

User = Users.Users()
User.changeuser("201705130120", "Wangzixi")

r = User.login()
time.sleep(2.5)
while "正选结束" in str(r):
    r = User.login()
    print(r)
    time.sleep(2.5)


def searc(kch):
    User.pre_search(kch=kch)
    r = User.do_search()
    try:
        if "object" in r:
            if "resultList" in r["object"]:
                if len(r["object"]["resultList"]) > 0:
                    if "KCM" in r["object"]["resultList"][0]:
                        print(r["object"]["resultList"][0]["KCM"], end=" ")
                        kyl = User.get_rest_num(r, "600")
                        return kyl
    except:
        return -10

    return -100


def tuixuan(kch, kxh, kchx, kxhx):
    # User.delclass(kch, kxh)
    # time.sleep(2)
    r=User.choose(kchx, kxhx)
    print(r)

xk_kxh = ["sd07517120", "sd07510310", "sd07510010"]
while True:
    for x in xk_kxh:
        time.sleep(0.1)
        kyl = searc(x)
        print("课余量=" + str(kyl))
        if int(kyl) > 0:
            for i in range(0, 3):
                tuixuan("sd07510710", "600", x, "600")
                time.sleep(2)
                print("尝试选课")
            # for i in range(100000):
            #     time.sleep(10)
            #     print("ojbk")
