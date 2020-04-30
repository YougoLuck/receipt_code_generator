import random
import csv
import os

def generate_rc_code(base, cnt):
    result = []
    for _ in range(cnt):
        rndAdd = random.randint(10, 99)
        base = base + rndAdd
        result.append(base)
    return result


def generate_ck_code(cnt):
    result = []
    for _ in range(cnt):
        ck = str(random.randint(40000, 99999))
        for i in range(3):
            ck += ' ' + str(random.randint(10000, 99999))
        result.append(ck)
    return result


def generate_pw(cnt):
    code = {10:'/', 11:'*', 12:'-', 13:'+', 14:'<', 15:'>'}
    result = []
    for _ in range(cnt):
        ck = ''
        for _ in range(27 * 4):
            tem = random.randint(0, 15)
            if tem < 10:
                ck += str(tem)
            else:
                ck += code[tem]
        result.append(ck)
    return result


def conver_path(path):
    return path.replace('\\', '/')


def write_csv(path, data):
    csvfile = open(os.path.join(path, 'output.csv'), 'w', encoding='utf-8-sig', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(['rc_code', 'check_code', 'password'])
    writer.writerows(data)
    csvfile.close()

def generate_html_text(text):
    return "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"\
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"\
            "p, li { white-space: pre-wrap; }\n"\
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.86555pt; font-weight:400; font-style:normal;\">\n"\
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.86555pt;\">" + text + '</span></p></body></html>'
