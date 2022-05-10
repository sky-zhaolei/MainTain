import requests
import json
import jsonpath


def __handle_header(token=None):
    """
    处理请求头。加上项目当中必带的请求头。如果有token，加上token。
    :param token: token值
    :return: 处理之后headers字典
    """
    headers = {}
    if token:
        headers["token"] = token
    return headers

def send_requests(method,url,data=None,token=None):
    headers = __handle_header(token)
    method = method.upper
    if method == "GET":
        resp = requests.get(url,data,headers=headers)
    else:
        resp = requests.post(url,json=data,headers=headers)
    return resp

def login_case():
    # 获取登录验证码
    login_phone = input()
    url = "http://store.test.dstcar.com/dst-partner-apis/api-store/public/verifyCode"
    datas = {"phone": login_phone}
    send_requests("POST", url, datas)
    #登录获取token
    loging_url = "http://store.test.dstcar.com/dst-partner-apis/api-store/public/login"
    datas = {"phone": login_phone, "verifyCode": "999999"}
    resp = send_requests("POST", loging_url, datas)
    token = resp.json()["data"]["token"]
    print("------获取token成功------当前token为：",token)
    #获取当前登录门店
    get_now_url = "http://store.test.dstcar.com/dst-partner-apis/api-store/store/user/getUserInfo"
    datas = {}
    resp = send_requests("POST", get_now_url, datas, token)
    now_store_name = jsonpath.jsonpath(resp.json(),"$.data.current_store_info.store_name")[0]
    print("--------当前登录门店为--------",now_store_name)
    #获取默认员工名称及id
    get_now_staff = "http://store.test.dstcar.com/dst-partner-apis/api-store/store/staff/index"
    datas = {"limit":5,"page":1}
    resp = send_requests("POST", get_now_staff, datas, token)
    staff_name = jsonpath.jsonpath(resp.json(),"$.data.list[0].user_name")[0]
    staff_id = jsonpath.jsonpath(resp.json(),"$.data.list[0].staff_id")[0]
    print("--------当前默认员工为--------",staff_name)
    #获取默认班组及id
    get_now_staff = "http://store.test.dstcar.com/dst-partner-apis/api-store/store/team/index"
    datas = {"limit": 5, "page": 1}
    resp = send_requests("POST", get_now_staff, datas, token)
    team_name = jsonpath.jsonpath(resp.json(), "$.data.list[0].team_name")[0]
    team_id = jsonpath.jsonpath(resp.json(), "$.data.list[0].team_id")[0]
    print("--------当前默认班组为--------", team_name)

if __name__ == '__main__':
    print("---------请输入你所登录的账号----------")
    login_case()



