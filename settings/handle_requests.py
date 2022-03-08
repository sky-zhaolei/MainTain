import requests
import settings
from settings.setting import loading


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

if __name__ == '__main__':
    datas = loading()
    userphone = datas["maintain"]["maintain_phone"]
    url = "http://store.test.dstcar.com/dst-partner-apis/api-store/public/verifyCode"
    datas = {"phone":"15070720246"}
    resp = send_requests("POST",url,datas)

    loging_url = "http://store.test.dstcar.com/dst-partner-apis/api-store/public/login"
    datas = {"phone":"15070720246","verifyCode":"999999"}
    resp = send_requests("POST",loging_url,datas)
    toekn = resp.json()["data"]["token"]
    print(toekn)