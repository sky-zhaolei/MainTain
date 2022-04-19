import yaml
from Common.handle_path import conf_dir

def loading():
    with open(conf_dir+"/sets.yaml", encoding="utf-8") as fs:
        datas = yaml.load(fs,yaml.FullLoader)
    return datas

datas = loading()

if __name__ == '__main__':
    print(datas["maintain"]["login_phone"])
    print(datas["maintain"]["url"])
