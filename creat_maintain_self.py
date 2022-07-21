import requests
import json
import jsonpath
import time
from faker import Faker

global now_time
now_time = time.strftime('%Y-%m-%d %H:%M:%S')
fk = Faker(locale="zh-CN")
now_data = time.strftime('%Y-%m-%d')
handle_img = [{
                "display_url": "https://dst-m-oss.oss-cn-shenzhen.dstzc.com/maintain/165838575062d8f556230d1.jpg?OSSAccessKeyId=LTAIXxxrBjucl7GJ&Expires=1658389350&Signature=yz06FLkcS1I6uPTlFpvMMdpPIqU%3D",
                "save_url": "maintain/165838575062d8f556230d1.jpg",
                "file_name": "微信图片_20220701093049.jpg"
                }]



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


#
# #class Maintain:
#     def __init__(self):


def Login_Case():        #进行登录流程，获取登录信息
    global token, store_id, staff_id, team_id
    # 获取登录验证码
    login_phone = input("---------请输入你的账号：---------")
    url = "http://store.test.dstcar.com/dst-partner-apis/api-store/public/verifyCode"
    datas = {"phone": login_phone}
    send_requests("POST", url, datas)
    #登录获取token
    loging_url = "http://store.test.dstcar.com/dst-partner-apis/api-store/public/login"
    datas = {"phone": login_phone, "verifyCode": "999999"}
    resp = send_requests("POST", loging_url, datas)
    token = resp.json()["data"]["token"]
    print("--------获取token成功--------当前token为：",token)
    #获取当前登录门店
    get_now_url = "http://store.test.dstcar.com/dst-partner-apis/api-store/store/user/getUserInfo"
    datas = {}
    resp = send_requests("POST", get_now_url, datas, token)
    now_store_name = jsonpath.jsonpath(resp.json(),"$.data.current_store_info.store_name")[0]
    store_id = jsonpath.jsonpath(resp.json(),"$.data.current_store_info.store_id")[0]
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
    return team_id,store_id,staff_id,token


def ChooseFun():        #选择要进行的功能
    choose_id = int(input("想要进行的功能：自动创建预约单（10），自动接车（20），自动进行入库操作（30），自动创建财务结算单（40），退出（00）"))
    if choose_id == 10:
        CreatOrder()
    elif choose_id == 20:
        print("进行自动接车操作")
    elif choose_id == 30:
        print("自动进行入库操作")
    elif choose_id == 40:
        print("自动进行创建财务结算单")
    else:
        print("退出当前程序")



def CreatOrder():
    print("--------开始自动创建预约单流程--------")
    # print(token)
    # 获取个默认车辆用于创建预约单
    get_car_info = "http://store.test.dstcar.com/dst-partner-apis/api-store/store/car/bindList"
    datas = {"limit":1,"page":1,"total":10}
    resp = send_requests("POST", get_car_info, datas, token)
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
    print("--------当前使用车辆车牌号:{}--------\n--------车架号:{}--------\n--------用户名称:{}--------".format(plate_number,vin_code,name))
    #创建预约单
    add_reservation = "http://store.test.dstcar.com/dst-partner-apis/api-store/store/reservation/add"
    datas = {"user_name":name,"fault_type":["135"],"isAccidentOrder":False,"user_phone":phone,
             "plate_number":plate_number,"vin_code":vin_code,"car_brand":car_brand,
             "car_type":car_type,"service":["service_maintain","service_repair","service_rescue"],
             "car_year":car_year,"fault":"","reservation_content":"预约内容","reservation_time":now_time,
             "is_accident_order":"0","car_id":car_id,"car_brand_id":car_brand_id,"car_type_id":car_type_id,
             "name":name,"phone":phone,"user_id":user_id,"type":customer_type,
             "car_type_name":car_type_name,"customer_type":customer_type}
    resp = send_requests("POST", add_reservation, datas, token)
    if (resp.json())["code"] == 200:
        print("--------创建预约单成功----------")
    else:
        print("--------创建预约单失败---------")
        print(resp.json())
    #获取刚创建的预约单id
    get_reservations_id = "http://store.test.dstcar.com/dst-partner-apis/api-store/store/reservation/index"
    datas = {"limit": 1, "page": 1}
    resp = send_requests("POST", get_reservations_id, datas, token)
    reservations_sn = jsonpath.jsonpath(resp.json(), "$.data.list[0].reservation_sn")[0]
    #进行确认预约单操作，并选择服务顾问
    confirm_reservations = "http://store.test.dstcar.com/dst-partner-apis/api-store/store/reservation/confirm"
    datas = {"service_consultant":staff_id,"reservation_sn":reservations_sn}
    resp = send_requests("POST", confirm_reservations, datas, token)
    if (resp.json())["code"] == 200:
        print("--------确认预约成功----------")
    else:
        print("--------确认预约失败---------")
        print(resp.json())
    # 获取创建的检修单内容
    get_repair_id = "http://store.test.dstcar.com/dst-partner-apis/api-store/store/repair/index"
    datas = {"reservation_sn": reservations_sn, "limit": 1, "page": 1, "total": 1}
    resp = send_requests("POST", get_repair_id, datas, token)
    repair_id = jsonpath.jsonpath(resp.json(), "$.data.list[0].repair_id")[0]
    repair_sn = jsonpath.jsonpath(resp.json(), "$.data.list[0].repair_sn")[0]
    source = jsonpath.jsonpath(resp.json(), "$.data.list[0].source")[0]
    reservation_order_type = jsonpath.jsonpath(resp.json(), "$.data.list[0].reservation_order_type")[0]
    print("--------对应检修单单号为：--------", repair_sn)

    #进行预约单接车操作
    pick_car = "http://store.test.dstcar.com/dst-partner-apis/api-store/store/repair/pickCar"
    datas = {"maintenance_name":name,"maintenance_phone":phone,"maintenance_time":now_time,"oil_mass":fk.random_int(min=1, max=99),
             "driving_mileage":fk.random_int(min=1, max=99999),"pick_up_time":now_data,"vin_code":vin_code,
             "pre_detect_dispatch_name":"",
             "dashboard_img":handle_img,
             "enter_factory_img":{
                 "car_front_imgs":handle_img,
                 "car_back_imgs":handle_img,
                 "car_left_imgs":handle_img,
                 "car_right_imgs":handle_img
             },
             "chassis_img":{
                 "front_imgs":handle_img,
                 "back_imgs":handle_img},
             "car_damage_img":[],
             "other_img":[],
             "remark":"脚本自动创建",
             "repair_id":repair_id,"repair_sn":repair_sn,"status":1,"modified_time":now_time,
             "reservation_sn":reservations_sn,"reservation_confirm_time":now_time,
             "pick_car_time":'',"customer_type":customer_type,"source":source,"detailed_list":[],
             "plate_number":plate_number,"car_brand":car_brand,"car_type":car_type,"status_name":"待接车",
             "reservation_channel":"门店代客预约","reservation_order_type":reservation_order_type,
             "order_goods_amount":"0.00","is_dst_car":'',"edit_maintain_phone":"",
             "is_accident_order":0,"is_have_count":1,"is_show_button":1,"companies_name":name,
             "type":customer_type,"type_name":"个人客户","source_name":"","pre_detect_dispatch":[]}
    resp = send_requests("POST", pick_car, datas, token)
    print(datas)
    print(resp.json())
    ChooseFun()


if __name__ == '__main__':

    print(now_time)
    Login_Case()
    ChooseFun()




