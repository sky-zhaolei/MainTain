from settings.handle_requests import *

def loding_case():
    datas = loading()
    userphone = datas["maintain"]["maintain_phone"]
    url = "http://store.test.dstcar.com/dst-partner-apis/api-store/public/verifyCode"
    datas = {"phone": "15070720246"}
    resp = send_requests("POST", url, datas)

    loging_url = "http://store.test.dstcar.com/dst-partner-apis/api-store/public/login"
    datas = {"phone": "15070720246", "verifyCode": "999999"}
    resp = send_requests("POST", loging_url, datas)
    token = resp.json()["data"]["token"]
    print(token)
    return token

def maintain_detial():
    detail_url = "http://store.test.dstcar.com/dst-partner-apis/api-store/store/store/detail"
    datas = {}
    resp = send_requests("POST", detail_url, datas, token = loding_case())
    print(resp.json())

if __name__ == '__main__':
    maintain_detial()