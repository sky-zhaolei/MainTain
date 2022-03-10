import yaml

def loading():
    with open("../Conf/sets.yaml", encoding="utf-8") as fs:
        datas = yaml.load(fs,yaml.FullLoader)
    return datas

datas = loading()

if __name__ == '__main__':
    print(datas["maintain"]["maintain_phone"])
    print(datas["maintain"]["url"])
