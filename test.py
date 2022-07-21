import requests
import json
import jsonpath

def __handle_header(token=None):
    """
    处理请求头。加上项目当中必带的请求头。如果有token，加上token。
    :param token: token值
    :return: 处理之后headers字典
    """
    headers = {"token":"94c9f84510f4443893b9648fa1699748"}
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


def CreatOrder():
    print("--------开始自动创建预约单流程--------")
    # 获取个默认车辆用于创建预约单
    get_car_info = "http://store.test.dstcar.com/dst-partner-apis/api-store/store/car/bindList"
    datas = {"limit":1,"page":1,"total":10}
    resp = send_requests("POST", get_car_info, datas)
    car_brand = jsonpath.jsonpath(resp.json(), "$.data.list[0].car_brand")[0]
    car_brand_id = jsonpath.jsonpath(resp.json(), "$.data.list[0].car_brand_id")[0]
    car_brand_id = jsonpath.jsonpath(resp.json(), "$.data.list[0].car_brand_id")[0]
    car_id = jsonpath.jsonpath(resp.json(), "$.data.list[0].car_id")[0]
    car_type = jsonpath.jsonpath(resp.json(), "$.data.list[0].car_type")[0]
    car_type_id = jsonpath.jsonpath(resp.json(), "$.data.list[0].car_type_id")[0]
    car_type_name = jsonpath.jsonpath(resp.json(), "$.data.list[0].car_type_name")[0]
    car_year = jsonpath.jsonpath(resp.json(), "$.data.list[0].car_year")[0]
    customer_type = jsonpath.jsonpath(resp.json(), "$.data.list[0].type")[0]
    name = jsonpath.jsonpath(resp.json(), "$.data.list[0].name")[0]
    phone = jsonpath.jsonpath(resp.json(), "$.data.list[0].phone")[0]
    user_id = jsonpath.jsonpath(resp.json(), "$.data.list[0].user_id")[0]
    plate_number = jsonpath.jsonpath(resp.json(), "$.data.list[0].plate_number")[0]
    vin_code = jsonpath.jsonpath(resp.json(), "$.data.list[0].vin_code")[0]

    print("当前使用车辆车牌号:{}\n车架号:{}\n用户名称:{}".format(plate_number,vin_code,name))

if __name__ == '__main__':
    CreatOrder()