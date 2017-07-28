# -*- coding: utf8 -*-

import MySQLdb
import pandas as pd
import threading
import requests
import urllib
import re
import traceback
import random
import datetime
import time
import json
import hashlib
import lxml.html
import sys
reload(sys)
import chardet
sys.setdefaultencoding("utf-8")


# 连接数据库
def connect_database(db_nick='yuqing'):
    conn = ''
    if db_nick == 'zhangrz':
        try:
            conn = MySQLdb.connect(host='192.168.8.195', user='wdzj_many', passwd='wdzj_many',
                                   db='zhangrz', port=3306, charset='utf8')
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    elif db_nick == 'yuqing':
        try:
            conn = MySQLdb.connect(host='192.168.11.140', user='wdzj_many', passwd='wdzj_many',
                                   db='yuqing', port=3306, charset='utf8')
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    elif db_nick == 'yuqing_b':
        try:
            conn = MySQLdb.connect(host='192.168.11.140', user='wdzj_many', passwd='wdzj_many',
                                   db='yuqing_b', port=3306, charset='utf8')
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    elif db_nick == 'wdzj_website_2':
        try:
            conn = MySQLdb.connect(host='192.168.15.200', user='root', passwd='root',
                                   db='wdzj_website_2', port=3309, charset='utf8')
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    elif db_nick == 'wdzj_website_21':
        while True:
            try:
                conn = MySQLdb.connect(host='', user='', passwd='',
                                       db='', port=13307, charset='utf8')
            except MySQLdb.Error, e:
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            if isinstance(conn, MySQLdb.connections.Connection):
                break
    else:
        print 'No such database!!!'
    return conn


def insert_WDZJ_PLAT_COMPANY_IC_DATA(conn, cur, COMPANY_NAME, IC_DATA, SHAREHOLDER_DATA, PRINCIPAL_DATA, INVESTMENT_ABROAD, SOURCE_URL):
    UPDATE_DATE = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    insert_sql = "INSERT INTO WDZJ_PLAT_COMPANY_IC_DATA ( COMPANY_NAME, IC_DATA, SHAREHOLDER_DATA," \
                 " PRINCIPAL_DATA, INVESTMENT_ABROAD, SOURCE_URL, UPDATE_DATE) VALUES ('" + COMPANY_NAME + "','" +\
                 IC_DATA + "','" + SHAREHOLDER_DATA + "','" + PRINCIPAL_DATA + "','" + INVESTMENT_ABROAD + "','" +\
                 SOURCE_URL + "','" + UPDATE_DATE + "')"
    try:
        cur.execute(insert_sql)
        conn.commit()
    except:
        traceback.print_exc()
        pass


def insert_WDZJ_PLAT_COMPANY_IC_DATA21(conn21, cur21, COMPANY_NAME, IC_DATA, SHAREHOLDER_DATA, PRINCIPAL_DATA, INVESTMENT_ABROAD, SOURCE_URL):
    UPDATE_DATE = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    insert_sql = "INSERT INTO WDZJ_PLAT_COMPANY_IC_DATA ( COMPANY_NAME, IC_DATA, SHAREHOLDER_DATA," \
                 " PRINCIPAL_DATA, INVESTMENT_ABROAD, SOURCE_URL, UPDATE_DATE) VALUES ('" + COMPANY_NAME + "','" +\
                 IC_DATA + "','" + SHAREHOLDER_DATA + "','" + PRINCIPAL_DATA + "','" + INVESTMENT_ABROAD + "','" +\
                 SOURCE_URL + "','" + UPDATE_DATE + "')"
    try:
        cur21.execute(insert_sql)
        conn21.commit()
    except:
        traceback.print_exc()
        pass


def insert_business_info(conn, cur, credit_code, name, tax_no, no, org_no, oper_name, regist_capi, status,
                         start_date, econ_kind, bus_people, term, belong_org, check_date, eng_name, belong_area,
                         belong_industry, address, scope):
    day_date = str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    create_time = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    insert_sql = "INSERT INTO yuqing.business_info (credit_code, name, tax_no, no, org_no, oper_name, regist_capi," \
                 " status, start_date, econ_kind, bus_people, term, belong_org, check_date, eng_name, belong_area," \
                 " belong_industry, address, scope) VALUES ('" + credit_code + "','" + name + "','" + tax_no + "','" +\
                 no + "','" + org_no + "','" + oper_name + "','" + regist_capi + "','" + status + "','" + start_date +\
                 "','" + econ_kind + "','" + bus_people + "','" + term + "','" + belong_org + "','" + check_date +\
                 "','" + eng_name + "','" + belong_area + "','" + belong_industry + "','" + address + "','" + scope\
                 + "')"
    cur.execute(insert_sql)
    conn.commit()


def insert_business_shareholder(conn, cur, credit_code, stock_name, stock_percent, should_capi, should_date, stock_type):
    insert_sql = "INSERT INTO yuqing.business_shareholder (credit_code, stock_name, stock_percent, should_capi, " \
                 "should_date, stock_type) VALUES ('" + credit_code + "','" + stock_name + "','" + stock_percent +\
                 "','" + str(should_capi) + "','" + str(should_date) + "','" + str(stock_type) + "')"
    cur.execute(insert_sql)
    conn.commit()


def insert_business_managers(conn, cur, credit_code, name, post):
    insert_sql = "INSERT INTO yuqing.business_managers (credit_code, name, post) VALUES ('" + credit_code +\
                 "','" + str(name) + "','" + str(post) + "')"
    cur.execute(insert_sql)
    conn.commit()


def insert_business_judgementdoc(conn, cur, credit_code, case_name, pub_date, case_no, case_identity, court):
    insert_sql = "INSERT INTO yuqing.business_judgementdoc (credit_code, case_name, pub_date, case_no, case_identity, " \
                 "court) VALUES ('" + credit_code + "','" + case_name + "','" + pub_date + "','" + case_no + "','" +\
                 str(case_identity) + "','" + str(court) + "')"
    cur.execute(insert_sql)
    conn.commit()


def insert_business_court_announcement(conn, cur, credit_code, publish_date, type, party, content):
    insert_sql = "INSERT INTO yuqing.business_managers (credit_code, publish_date, type, party, content) VALUES ('" +\
                 credit_code + "','" +publish_date + "','" + type + "','" + party + "','" + content + "')"
    cur.execute(insert_sql)
    conn.commit()


def insert_business_enforced(conn, cur, credit_code, name, register_date, court, subject):
    insert_sql = "INSERT INTO yuqing.business_managers (credit_code, name, register_date, court, subject) VALUES ('" +\
                 credit_code + "','" + name + "','" + register_date + "','" + court + "','" + subject + "')"
    cur.execute(insert_sql)
    conn.commit()


def insert_begincourt_announcement(conn, cur, credit_code, begin_date, cause, accuser, accused, case_no, area,
                                   schedule_date, department, judge, court, court_ting):
    insert_sql = "INSERT INTO yuqing.business_managers (credit_code, begin_date, cause, accuser, accused, case_no, " \
                 "area, schedule_date, department, judge, court, court_ting) VALUES ('" + credit_code + "','" +\
                 begin_date + "','" + cause + "','" + accuser + "','" + accused + "','" + case_no + "','" + area +\
                 "','" + schedule_date + "','" + department + "','" + judge + "','" + court + "','" + court_ting + "')"
    cur.execute(insert_sql)
    conn.commit()


def insert_penalty_industry(conn, cur, credit_code, reference_no, type, content, decision_org, decision_date):
    insert_sql = "INSERT INTO yuqing.business_managers (credit_code, reference_no, type, content, decision_org," \
                 " decision_date) VALUES ('" + credit_code + "','" +  reference_no, type, content +\
                 "','" + decision_org + "','" + decision_date + "')"
    cur.execute(insert_sql)
    conn.commit()


def insert_penalty_china(conn, cur, credit_code, name, area, decision_date):
    insert_sql = "INSERT INTO yuqing.business_managers (credit_code, name, area, decision_date) VALUES ('" +\
                 credit_code + "','" +  name + "','" +  area + "','" + decision_date + "')"
    cur.execute(insert_sql)
    conn.commit()


def insert_abnormal(conn, cur, credit_code, in_date, out_date, decision_org, out_org, in_cause, out_cause):
    insert_sql = "INSERT INTO yuqing.business_managers (credit_code, in_date, out_date, decision_org, out_org," \
                 " in_cause, out_cause) VALUES ('" + credit_code + "','" + in_date + "','" + out_date + "','" +\
                 decision_org + "','" + out_org + "','" + in_cause + "','" + out_cause + "')"
    cur.execute(insert_sql)
    conn.commit()


def climb_info(conn_yuqing, cur, content, r):
    try:
        credit_code = re.findall("统一信用代码：<span><span.*?class=\"c8\"></span>(.+?)<", content)[0].strip().replace("未公开", "-")
        print credit_code
        tax_no = re.findall("纳税人识别号：.*?<span>(.+?)<", content)[0].strip().replace("未公开", "-")
        no = re.findall("工商注册号：<span>(.+?)<", content)[0].strip().replace("未公开", "-")
        org_no = re.findall("组织机构代码：<span>(.+?)<", content)[0].strip().replace("未公开", "-")
        oper_name = re.findall("onclick=\"common\.stopPropagation\(event\)\">\s*(.*?)<", content)[0].strip().replace("未公开", "-")
        regist_capi = re.findall("company.regCapital\)}}\".*?class=\"baseinfo-module-content-value\">\s*(.*?)<", content)[0].strip().replace("未公开", "-")
        status = re.findall("baseinfo-module-content-value statusType.*?>\s*(.*?)\s*<", content)[0].strip().replace("未公开", "-")
        start_date = re.findall("注册时间</div>.*?<div class=\"pb10\">.*?<div.*?title=\"([未公开|\d-]+)", content)[0].strip().replace("未公开", "-")
        econ_kind = re.findall("企业类型：<span>\s*(.+?)\s*<", content)[0].strip().replace("未公开", "-")
        # bus_people = re.findall("人员规模：</td> <td class=\"ma_left\">\s*([\d-]+)", content)[0].strip()
        term = re.findall("营业期限：.*?>\s*(.+?)\s*<", content)[0].strip().replace(" ", "").replace("未公开", "-")
        belong_org = re.findall("登记机关：<span>\s*(.+?)\s*<", content)[0].strip().replace("未公开", "-")
        check_date = re.findall("核准日期：.*?<span>\s*(.+?)\s*<", content)[0].strip().replace("未公开", "-")
        # eng_name = re.findall("英文名：</td> <td class=\"ma_left\" style=\"max-width:301px;\">\s*(.+?)\s*?", content)[0].strip()
        # belong_area = re.findall("所属地区\s*</td> <td class=\"ma_left\">\s*(.+?)\s*<", content)[0].strip()
        belong_industry = re.findall("行业：<span>\s*(.+?)\s*<", content)[0].strip().replace("未公开", "-")
        address = re.findall("注册地址：<span>\s*(.+?)\s*<", content)[0].strip().replace("查看地图", "").replace("未公开", "-")
        scope = re.findall("<span ng-if=\"!showDetail\" ng-bind-html=\"perContent\|splitNum\" class=\"js-full-container.*?>\s*(.+?)\s*<", content)[0].strip().replace("未公开", "-")
        # try:
        #     before_name = re.findall("企业地址：</td> <td class=\"ma_left\" colspan=\"3\">\s*(.+?)\s*<", content)[0].strip()
        # except:
        #     traceback.print_exc()
        #     pass
        try:
            # print chardet.detect(json.dumps({"统一社会信誉代码：": credit_code,"注册号：": no,"组织机构代码：": org_no,
            #                      "经营状态：":status,"法定代表人：":oper_name,"注册资本：":regist_capi,"公司类型：":econ_kind,"成立日期：":start_date,"营业期限：":term,\
            #  "登记机关：":belong_org,"发照日期：":check_date,"公司规模：":bus_people,"所属行业：":belong_industry,"英文名：":eng_name,"曾用名：":before_name,"企业地址：":address,"经营范围：":scope}, ensure_ascii=False).encode('utf-8')), chardet.detect(before_name)
            # print credit_code, name, tax_no, no, org_no, oper_name, regist_capi, status,start_date, econ_kind, bus_people, term, belong_org, check_date, eng_name, belong_area, belong_industry, address, scope
            return credit_code, {"统一社会信誉代码：": credit_code,"注册号：": no,"组织机构代码：": org_no,
                                 "经营状态：":status,"法定代表人：":oper_name,"注册资本：":regist_capi,"公司类型：":econ_kind,"成立日期：":start_date,"营业期限：":term,\
             "登记机关：":belong_org,"发照日期：":check_date,"所属行业：":belong_industry,"企业地址：":address,"经营范围：":scope}
            # insert_business_info(conn_yuqing, cur, credit_code, name, tax_no, no, org_no, oper_name, regist_capi, status,
            #                      start_date, econ_kind, bus_people, term, belong_org, check_date, eng_name, belong_area,
            #                      belong_industry, address, scope)
        except:
            traceback.print_exc()
            return False
    except:
        traceback.print_exc()
        return False


def climb_shareholder(conn_yuqing, cur, content, r):
    stock_name = re.findall("class=\"in-block vertival-middle overflow-width\" title=\"(.+?)\"", content)
    # should_capi = re.findall("([\d.-]+)\s*<br/> </td> <td class=\"text-center\">", content)
    # should_date = re.findall("<br/> </td> <td class=\"text-center\">\s*(.*?)\s*<", content)
    stock_percent = re.findall("<div\s*>\s*<span class=\"c-money-y\">\s*(.+?)\s*<", content)
    capi_date = re.findall("<span class=\"\">[(人民币)]*([\d.,]+)[万|万元|万\s*人民币|万元\s*人民币]*\s*</span>.*?<span\s*>时间：([\d-]+)</span\s*>", content)
    capi = re.findall("<div\s*>\s*<span class=\"\">[(人民币)]*([\d.,]+)[万|万元|万\s*人民币|万元\s*人民币]*</span\s*>\s*</div\s*>", content)
    # stock_type = re.findall("</td> <td class=\"text-center\">(.*?)</td> </tr> <tr>", content)
    if len(capi) == 0:        # capi = re.findall("<div >\s*<span class=\"\">([\d.,]+)万元*</span>\s*</div>", content)
        if len(stock_percent) > len(capi_date):
            for i in range(0, len(stock_percent) - len(capi_date)):
                capi_date.append(("-", "-"))
    elif len(stock_percent) > len(capi):
        for i in range(0, len(stock_percent) - len(capi)):
            capi.append("-")
    if len(capi) != 0 and len(capi_date) != 0:
        for i in capi:
            capi_date.append((i.replace(",", "").replace("未公开", "-"), ""))
    re_dic = {}
    for nu, i in enumerate(stock_name):
        try:
            if len(capi_date) == 0:
                re_dic[stock_name[nu]] = capi[nu].replace(",", "").replace("未公开", "-") + "万元人民币" + "|-|" + stock_percent[nu].replace("未公开", "-")
            elif capi_date[nu][0].replace(" ", "") != "未公开":
                re_dic[stock_name[nu]] = capi_date[nu][0].replace(",", "") + "万元人民币" + "|" + capi_date[nu][1].replace("未公开", "-") + "|" + stock_percent[nu].replace("未公开", "-")
            else:
                re_dic[stock_name[nu]] = capi_date[nu][0].replace(",", "").replace("未公开", "-") + "|" + capi_date[nu][1].replace("未公开", "-") + "|" + stock_percent[nu].replace("未公开", "-")
            re_dic[stock_name[nu]] = re_dic[stock_name[nu]].replace("-万元人民币", "-")
            # insert_business_shareholder(conn_yuqing, cur, credit_code, stock_name[nu], stock_percent[nu], should_capi[nu], should_date[nu], stock_type[nu])
        except:
            traceback.print_exc()
            continue
    return re_dic


def climb_managers(conn_yuqing, cur, content, r):
    try:
        name = re.findall("href=\"/human/[\w-]+\" target=\"_blank\" >\s*(.*?)\s*<", content)
        post = re.findall("solid #E2E7E8\">.*?<span >(.+?)</div>", content)
        re_list = []
        for nu, i in enumerate(name):
            try:
                # print credit_code, name[nu], post[nu]
                re_list.append({post[nu].replace(" ", "").replace("<span>", "").replace("</span>", "").replace("未公开", "-").replace("未知, 未知", "-").replace("未知", "-"): name[nu].replace("未公开", "-")})
                # insert_business_managers(conn_yuqing, cur, credit_code, name[nu], post[nu])
            except:
                traceback.print_exc()
                continue
        return re_list
    except:
        print url
        traceback.print_exc()
        return False


def climb_judgementdoc(conn_yuqing, cur, credit_code, plat_name, url, r):
    unique = re.findall("_([A-Za-z0-9]{10,40})", url)
    try:
        url_susong = "http://www.qichacha.com/company_getinfos?unique=" + unique[0] + "&companyname=" + urllib.quote(plat_name) + "&tab=susong"
        total_page = re.findall("susong\",\"wenshu\"\)'.*?([\d]+?)<", r.get(url_susong).content)
        if len(total_page) == 0:
            total_page = ["1"]
        for i in range(1, int(total_page[-1]) + 1):
            content = r.get(url_susong + "&box=wenshu&p=" + str(i)).content
            # id = re.findall("onclick='wsView\(\"(\w+?)\"\)", content)
            # content = r.post("http://www.qichacha.com/company_wenshuView", data={"id": "498bc1eeb1944bfae5b125ca842df512"}).content #裁判文书详细信息
            case_name = re.findall("\"\)'>(.+?)</a></td> ", content)
            pub_date = re.findall("<td width=\"13%\">([\d-]+?)<", content)
            case_no = re.findall("<td width=\"15%\">(.*?)<", content)
            case_identity = re.findall("<td width=\"24%\">(.*?)</td>", content)
            court = re.findall("</div> </td> <td width=\"15%\">(.*?)</td> </tr>", content)
            for nu, i in enumerate(case_identity):
                case_identity[nu] = "".join(re.findall("[^\u4e00-\u9fa5]", check_illegal(case_identity[nu])))
            if len(case_name):
                for nu, i in enumerate(case_name):
                    # print i, pub_date[nu], case_no[nu], court[nu]
                    try:
                        insert_business_judgementdoc(conn_yuqing, cur, credit_code, case_name[nu], pub_date[nu], case_no[nu], case_identity[nu], court[nu])
                    except:
                        continue
            else:
                print "暂无数据,裁判文书"
                break
        return True
    except:
        traceback.print_exc()
        return False


def climb_court_announcement(conn_yuqing, cur, credit_code, plat_name, url, r):
    unique = re.findall("_([A-Za-z0-9]{10,40})", url)
    try:
        url_susong = "http://www.qichacha.com/company_getinfos?unique=" + unique[0] + "&companyname=" + urllib.quote(plat_name) + "&tab=susong"
        total_page = re.findall("susong\",\"gonggao\"\)'.*?([\d]+?)<", r.get(url_susong).content)
        if len(total_page) == 0:
            total_page = ["1"]
        for i in range(1, int(total_page[-1]) + 1):
            content = r.get(url_susong + "&box=gonggao&p=" + str(i)).content
            publish_date = re.findall("<td width=\"15%\">([\d-]+?)<", content)
            type = re.findall("<td width=\"15%\">([\D]+?)</td> <td width=\"20%\">", content)
            party = re.findall("</td> <td width=\"20%\">(.*?)</td> <td width=\"40%\">", content)
            bis_content = re.findall("<span class=\"ma_court\">(.*?)</td> </tr>", content.replace("\n", ""))
            if len(publish_date):
                for nu, i in enumerate(publish_date):
                    print publish_date[nu], type[nu], party[nu], bis_content[nu]
                    try:
                        insert_business_court_announcement(conn_yuqing, cur, credit_code, publish_date[nu], type[nu], party[nu], bis_content[nu])
                    except:
                        continue
            else:
                print "暂无数据,法院公告"
                break
        return True
    except:
        traceback.print_exc()
        return False


def climb_enforced(conn_yuqing, cur, credit_code, plat_name, url, r):
    unique = re.findall("_([A-Za-z0-9]{10,40})", url)
    try:
        url_susong = "http://www.qichacha.com/company_getinfos?unique=" + unique[0] + "&companyname=" + urllib.quote(plat_name) + "&tab=susong"
        total_page = re.findall("susong\",\"zhixing\"\)'.*?([\d]+?)<", r.get(url_susong).content)
        if len(total_page) == 0:
            total_page = ["1"]
        for i in range(1, int(total_page[-1]) + 1):
            content = r.get(url_susong + "&box=zhixing&p=" + str(i)).content
            name = re.findall("</td><td>(.+?)<", content)
            register_date = re.findall("</td> <td>([\d-]+?)</td> <td>", content)
            court= re.findall("</td> <td>([\D]*?)</td> <td>", content)
            subject = re.findall("</td> <td>([\d]*?)</td> </tr>", content)
            if len(name):
                for nu, i in enumerate(name):
                    # print name[nu], register_date[nu], court[nu], subject[nu]
                    try:
                        insert_business_enforced(conn_yuqing, cur, credit_code, name[nu], register_date[nu], court[nu], subject[nu])
                    except:
                        continuev
            else:
                print "暂无数据,被执行人信息"
                break
        return True
    except:
        traceback.print_exc()
        return False


def climb_begincourt_announcement(conn_yuqing, cur, credit_code, plat_name, url, r):
    unique = re.findall("_([A-Za-z0-9]{10,40})", url)
    try:
        url_susong = "http://www.qichacha.com/company_getinfos?unique=" + unique[0] + "&companyname=" + urllib.quote(plat_name) + "&tab=susong"
        total_page = re.findall("susong\",\"notice\"\)'.*?([\d]+?)<", r.get(url_susong).content)
        if len(total_page) == 0:
            total_page = ["1"]
        for i in range(1, int(total_page[-1])+1):
            url_notice = url_susong + "&box=notice&p=" + str(i)
            ktnoticeView = re.findall("ktnoticeView\(\"([\w]+?)\"\)", r.get(url_notice).content)
            if len(ktnoticeView) == 0:
                print "暂无数据,开庭公告"
                return True
            for j in ktnoticeView:
                notice_json = json.loads(r.post("https://www.qichacha.com/company_ktnoticeView", data={"id": j}).content)
                begin_date = notice_json["data"]["open_time"]
                cause = notice_json["data"]["case_reason"]
                accuser = accused = ""
                for k in notice_json["data"]["prosecutor"]:
                    accuser += "," + k["name"]
                for k in notice_json["data"]["defendant"]:
                    accused += "," + k["name"]
                case_no = notice_json["data"]["case_no"]
                area = notice_json["data"]["province"]
                schedule_date = notice_json["data"]["schedule_time"]
                department = notice_json["data"]["undertake_department"]
                judge = notice_json["data"]["chief_judge"]
                court = notice_json["data"]["execute_gov"]
                court_ting = notice_json["data"]["execute_unite"]
                # print begin_date, cause, accuser, accused, case_no, area, schedule_date, department, judge, court, court_ting
                try:
                    insert_begincourt_announcement(conn, cur, credit_code, begin_date, cause, accuser, accused, case_no, area, schedule_date, department, judge, court, court_ting)
                except:
                    continue
            break
        return True
    except:
        traceback.print_exc()
        return False


def climb_penalty(conn_yuqing, cur, credit_code, plat_name, url, r):
    unique = re.findall("_([A-Za-z0-9]{10,40})", url)
    url_run = "http://www.qichacha.com/company_getinfos?unique=" + unique[0] + "&companyname=" + urllib.quote(plat_name) + "&tab=run"
    try:  # 工商局处罚
        url_penalty_industry = url_run + "&box=penalty&source=1"
        content = r.get(url_penalty_industry).content
        if len(re.findall("暂无数据", content)):
            print "暂无数据,工商局处罚"
        else:
            reference_no = re.findall("<tr><td class=\"ma_twoword\">\d*</td> <td>(.+?)<", content)
            type = re.findall("<tr><td class=\"ma_twoword\">\d*</td> <td>.*?</td> <td>(.+?)<", content)
            bis_content = re.findall("<tr><td class=\"ma_twoword\">\d*</td> <td>.*?</td> <td>.*?</td> <td>(.+?)<", content.replace("\n", ""))
            decision_org = re.findall("<tr><td class=\"ma_twoword\">\d*</td> <td>.*?</td> <td>.*?</td> <td>.*?</td> <td>(.+?)<", content.replace("\n", ""))
            decision_date = re.findall("<tr><td class=\"ma_twoword\">\d*</td> <td>.*?</td> <td>.*?</td> <td>.*?</td> <td>.*?</td> <td style=\"width:100px;\">(.+?)<", content.replace("\n", ""))
            for nu, i in enumerate(reference_no):
                # print reference_no[nu], type[nu], bis_content[nu], decision_org[nu], decision_date[nu]
                try:
                    insert_penalty_industry(conn_yuqing, cur, credit_code, reference_no[nu], type[nu], content[nu], decision_org[nu], decision_date[nu])
                except:
                    continue
    except:
        traceback.print_exc()
        print "工商局处罚获取失败"
    try:  # 信用中国处罚
        url_penalty_china = url_run + "&box=penalty&source=2"
        content = r.get(url_penalty_china).content
        if len(re.findall("暂无数据", content)):
            print "暂无数据,信用中国处罚"
        else:
            name = re.findall("<tr><td class=\"ma_twoword\">.*?</td><td>(.*?)<", content)
            area = re.findall("<tr><td class=\"ma_twoword\">.*?</td><td>.*?</td><td widtd=\"10%\">.*?<", content)
            decision_date = re.findall("<tr><td class=\"ma_twoword\">.*?</td><td>.*?</td><td widtd=\"10%\">.*?</td><td widtd=\"15%\">(.+?)<", content)
            for nu, i in enumerate(name):
                # print name, area, decision_date
                try:
                    insert_penalty_china(conn, cur, credit_code, name[nu], area[nu], decision_date[nu])
                except:
                    continue
        return True
    except:
        traceback.print_exc()
        return False


def climb_abnormal(conn_yuqing, cur, credit_code, plat_name, url, r):
    unique = re.findall("_([A-Za-z0-9]{10,40})", url)
    try:
        url = "http://www.qichacha.com/company_getinfos?unique=" + unique[0] + "&companyname=" + urllib.quote(plat_name) + "&tab=run"
        content = r.get(url).content
        in_date = re.findall("列入日期：\s*<span class=\"black-6\">(.+?)<", content.replace("\n", ""))
        out_date = re.findall("移出日期：\s*<span class=\"black-6\">(.+?)<", content.replace("\n", ""))
        decision_org = re.findall("作出决定机关：\s*<span class=\"black-6\">(.+?)<", content.replace("\n", ""))
        out_org = re.findall("移除决定机关：\s*<span class=\"black-6\">(.+?)<", content.replace("\n", ""))
        in_cause = re.findall("列入经营异常名录原因：\s*<span class=\"black-6\">(.+?)<", content.replace("\n", ""))
        out_cause = re.findall("移出经营异常名录原因：\s*<span class=\"black-6\">(.+?)<", content.replace("\n", ""))
        if len(in_date):
            for nu, i in enumerate(in_date):
                # print in_date[nu], out_date[nu], decision_org[nu], out_org[nu], in_cause[nu], out_cause[nu]
                try:
                    insert_abnormal(conn, cur, credit_code, in_date[nu], out_date[nu], decision_org[nu], out_org[nu], in_cause[nu], out_cause[nu])
                except:
                    continue
        else:
            print "暂无数据,经营异常"
        return True
    except:
        traceback.print_exc()
        return False


def climb_invest(conn_yuqing, cur, content, r):
    try:
        company_name = re.findall("style=\"word-break: break-all;\">\s*<span\s*class=\"text-click-color\">(.+?)<", content)
        oper_name = re.findall("point new-c4\" target=\"_blank\"\s*title=\"(.+?)\"", content)
        capi = re.findall("</a>\s*?</span>\s*?</span>.*?</td>\s*?<td>\s*?<span class=\"\">(.*?)</span>", content)
        if len(company_name) > len(oper_name):
            for i in range(0, len(company_name) - len(oper_name)):
                oper_name.append("-")
        if len(company_name) > len(capi):
            for i in range(0, len(company_name) - len(capi)):
                capi.append("-")
        status = re.findall("[\d-]+\s*?</span>\s*?</td>\s*?<td>\s*?<span class=\"\">(.*?)<", content)
        if len(company_name) > len(status):
            for i in range(0, len(company_name) - len(status)):
                status.append("-")
        # percent = re.findall("</td> <td class=\"text-center\">\s*[\d%]+?\s*<", content)
        # capi_inve_per_date_status = re.findall("</a>\s*?</span>\s*?</span>\s*?</td>\s*?<td>\s*?<span class=\"\">(.*?)</span>\s*?</td>\s*?<td>\s*?<span class=\"\">(.*?)\s*?</span>\s*?</td>\s*?<td>" \
        #                             "\s*?<span class=\".*?\">(.*?)\s*?</span>\s*?</td>\s*?<td>\s*?<span class=\"\">([\d-]+)\s*?</span>\s*?</td>\s*?<td>\s*?<span class=\"\">(.*?)\s*?<", content)

        if len(company_name):
            re_dic = {"state": "ok", "message": "", "data": {"total": len(company_name), "result": []}}
            for nu, i in enumerate(company_name):
                try:
                    # print company_name[nu], status[nu], oper_name[nu], capi[nu].rstrip("人民币").rstrip("元") + "元人民币"
                    dic_invest = {"name": company_name[nu].replace("未公开", "-"),
                                  "regStatus": status[nu].strip().replace("未公开", "-"),
                                  "legalPersonName": oper_name[nu].strip().replace("未公开", "-"),
                                    "regCapital": capi[nu].strip().lstrip("(人民币)").rstrip("万元").rstrip("万").rstrip("万元人民币") + "万元人民币".replace("未公开", "-")
                                  # "regDate": capi_inve_per_date_status[nu][3].strip(),
                                  # "invest_amount": capi_inve_per_date_status[nu][1].strip(),
                                  # "invest_percent": capi_inve_per_date_status[nu][2].strip()
                    }
                    re_dic["data"]["result"].append(dic_invest)
                    # "name": "上海图辰企业信用征信有限公司", "base": "sh", "regStatus": "存续（在营、开业、在册）",
                    # "estiblishTime": 1461859200000, "type": 1, "legalPersonName": "朱畑宇",
                    # "pencertileScore": 5839
                except:
                    print capi, status
                    traceback.print_exc()
                    continue
            return re_dic
        else:
            print "暂无数据,无投资"
            return {"state":"warn","message":"无数据","data":"null"}
    except:
        print url
        traceback.print_exc()
        return False


def get_info(conn_yuqing, cur, conn_yuqing_be, cur_be, r, conn_yuqing_21, cur_21, name_url, index):
    global url
    for nu, n_u in enumerate(name_url.iterrows()):  # 从测试库里查询所有公司
        if nu < index:
            continue
        plat_name = n_u[1]['company_name'].strip().encode("utf-8")
        url = n_u[1]['source_url']
        # if plat_name == "上海诺诺镑客金融信息服务有限公司":
        #     continue
        # plat_name = "合力贷（北京）科技有限公司"
        # plat_name = "开鑫贷融资服务江苏有限公司"
        # plat_name = "温州三信融民间融资信息服务有限公司"
        # plat_name = "深圳市前海好彩金融服务有限公司"
        # plat_name = "贵州合石电子商务有限公司"
        # plat_name = "北京恒昌利通投资管理有限公司"
        # plat_name = "北京秒贷网电子商务股份有限公司"
        r.proxies = get_proxies()
        # try:
        #     search_result = r.get("http://www.tianyancha.com/search?key=" + urllib.quote(plat_name) + "&checkFrom=searchBox").content.replace("\n", "")
        # except:
        #     print plat_name
        #     traceback.print_exc()
        #     return plat_name
            # continue
        # try:
        #     # url = re.findall(plat_name + ".*?" + plat_name + ".*?(http[s]*://www.tianyancha.com/company/\w+)", search_result)[0]
        #
        # except:
        #     print "URL有误或请求错误: " + plat_name
        #     traceback.print_exc()
        #     continue
        if url is None:
            continue
        credit_code = ""
        try:
            content = r.get(url).content.replace("\n", "")
            # print content
            credit_code, dic_IC_DATA= climb_info(conn_yuqing, cur, content, r)
            # credit_code = dic_IC_DATA = {}
            if len(re.findall("change-type=\"holder\"", content)):  # 股东多页
                url_holder = "http://www.tianyancha.com/pagination/holder.xhtml?ps=30&id=" + re.findall("\d+", url)[0] + "&pn="
                for i in range(2, int(re.findall("change-type=\"holder\">.*?<span>共</span>\s*(\d)\s*<span>页</span>", content)[0])+1):
                    content += r.get(url_holder + str(i)).content.replace("\n", "")
            list_SHAREHOLDER_DATA = climb_shareholder(conn_yuqing, cur, content, r)
            # list_SHAREHOLDER_DATA = {}
            if len(re.findall("change-type=\"staff\"", content)):  # 主要成员多页
                url_staff = "http://www.tianyancha.com/pagination/staff.xhtml?ps=30&id=" + re.findall("\d+", url)[0] + "&pn="
                for i in range(2, int(re.findall("change-type=\"staff\">.*?<span>共</span>\s*(\d)\s*<span>页</span>", content)[0])+1):
                    content += r.get(url_staff + str(i)).content.replace("\n", "")
            list_PRINCIPAL_DATA = climb_managers(conn_yuqing, cur, content, r)
            # list_PRINCIPAL_DATA = {}change-type="holder"
            if len(re.findall("change-type=\"invest\"", content)):  # 投资多页
                url_invest = "http://www.tianyancha.com/pagination/invest.xhtml?ps=30&id=" + re.findall("\d+", url)[0] + "&pn="
                for i in range(2, int(re.findall("change-type=\"invest\">.*?<span>共</span>\s*(\d)\s*<span>页</span>", content)[0])+1):
                    content += r.get(url_invest + str(i)).content.replace("\n", "")
            # if "北京恒昌利通投资管理有限公司" == plat_name or "宜信惠民投资管理（北京）有限公司" == plat_name:
            #     content = r.get(url).text.replace("\n", "")
            #     if len(re.findall("change-type=\"invest\"", content)):  # 投资多页
            #         url_invest = "http://www.tianyancha.com/pagination/invest.xhtml?ps=30&id=" + re.findall("\d+", url)[0] + "&pn="
            #         for i in range(2, int(re.findall(u"change-type=\"invest\">.*?<span>共</span>\s*(\d)\s*<span>页</span>", content)[0]) + 1):
            #                 content += r.get(url_invest + str(i)).text.replace("\n", "")
            dic_INVESTMENT_ABROAD = climb_invest(conn_yuqing, cur, content, r)
            # dic_INVESTMENT_ABROAD = {}
            print plat_name
            print url
            print json.dumps(dic_IC_DATA, encoding="UTF-8", ensure_ascii=False)
            print json.dumps(list_SHAREHOLDER_DATA, encoding="UTF-8", ensure_ascii=False)
            print json.dumps(list_PRINCIPAL_DATA, encoding="UTF-8", ensure_ascii=False)
            try:
                print json.dumps(dic_INVESTMENT_ABROAD, encoding="UTF-8", ensure_ascii=False)
            except:  # 投资页出现非utf-8编码格式
                content = r.get(url).text.replace("\n", "")
                if len(re.findall("change-type=\"invest\"", content)):  # 投资多页
                    url_invest = "http://www.tianyancha.com/pagination/invest.xhtml?ps=30&id=" + re.findall("\d+", url)[0] + "&pn="
                    for i in range(2, int(re.findall(u"change-type=\"invest\">.*?<span>共</span>\s*(\d)\s*<span>页</span>", content)[0]) + 1):
                        content += r.get(url_invest + str(i)).text.replace("\n", "")
                dic_INVESTMENT_ABROAD = climb_invest(conn_yuqing, cur, content, r)
                print json.dumps(dic_INVESTMENT_ABROAD, encoding="UTF-8", ensure_ascii=False)
            # insert_WDZJ_PLAT_COMPANY_IC_DATA(conn_yuqing, cur, plat_name,
            #                                  str(json.dumps(dic_IC_DATA, encoding="UTF-8", ensure_ascii=False)),
            #                                  str(json.dumps(list_SHAREHOLDER_DATA, encoding="UTF-8", ensure_ascii=False)),
            #                                  str(json.dumps(list_PRINCIPAL_DATA, encoding="UTF-8", ensure_ascii=False)),
            #                                  str(json.dumps(dic_INVESTMENT_ABROAD, encoding="UTF-8", ensure_ascii=False)),
            #                                     url)
            # insert_WDZJ_PLAT_COMPANY_IC_DATA21(conn_yuqing_be, cur_be, plat_name,
            #                                    str(json.dumps(dic_IC_DATA, encoding="UTF-8", ensure_ascii=False)),
            #                                    str(json.dumps(list_SHAREHOLDER_DATA, encoding="UTF-8",
            #                                                   ensure_ascii=False)),
            #                                    str(json.dumps(list_PRINCIPAL_DATA, encoding="UTF-8",
            #                                                   ensure_ascii=False)),
            #                                    str(json.dumps(dic_INVESTMENT_ABROAD, encoding="UTF-8",
            #                                                   ensure_ascii=False)),
            #                                    url)
            # insert_WDZJ_PLAT_COMPANY_IC_DATA21(conn_yuqing_21, cur_21, plat_name,
            #                                  str(json.dumps(dic_IC_DATA, encoding="UTF-8", ensure_ascii=False)),
            #                                  str(json.dumps(list_SHAREHOLDER_DATA, encoding="UTF-8", ensure_ascii=False)),
            #                                  str(json.dumps(list_PRINCIPAL_DATA, encoding="UTF-8", ensure_ascii=False)),
            #                                  str(json.dumps(dic_INVESTMENT_ABROAD, encoding="UTF-8", ensure_ascii=False)),
            #                                  url)
            # return ""  # 仅仅爬取一条时，立即返回
        except:
            print plat_name, url
            traceback.print_exc()
            return plat_name
        # time.sleep(300)  # 每五分钟采一条
        if (nu - index + 1) % 20 == 0:  # 每三十分钟采二十条
            time.sleep(1800)
    return ""
        # climb_judgementdoc(conn_yuqing, cur, credit_code, plat_name, url, r)
        # climb_court_announcement(conn_yuqing, cur, credit_code, plat_name, url, r)
        # climb_enforced(conn_yuqing, cur, credit_code, plat_name, url, r)
        # climb_begincourt_announcement(conn_yuqing, cur, credit_code, plat_name, url, r)
        # climb_penalty(conn_yuqing, cur, credit_code, plat_name, url, r)
        # climb_abnormal(conn_yuqing, cur, credit_code, plat_name, url, r)
        # insert_WDZJ_PLAT_COMPANY_IC_DATA(conn, cur, i, str(IC_DATA), str(SHAREHOLDER_DATA), PRINCIPAL_DATA,
        #                                  INVESTMENT_ABROAD, url)
        # break


def get_proxies():
    ip = json.loads(requests.get(
        "http://dps.kuaidaili.com/api/getdps/?orderid=958964320330191&num=50&ut=1&format=json&sep=1").content)
    proxies = {  # 每次请求从代理ip中随机产生一个地址
        "http": "http://8283891:ojonvhe8@" + ip["data"]["proxy_list"][random.randint(0, len(ip) - 1)]
    }
    return proxies


def get_cookie():
    # 天眼
    # 186
    # return "TYCID=524bcc5065d811e7b9c29dc37630003d; uccid=d28748c439794182559b00c010374433; ssuid=8589801555; Qs_lvt_117460=1499766091%2C1499823015%2C1499853576%2C1499913460%2C1500021205; Qs_pv_117460=2272283127989564700%2C3340376594904068600%2C2898491103211486000%2C2578886036208478700%2C3441978495829755400; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNjI3NjEyOSIsImlhdCI6MTUwMDYxNTk5MSwiZXhwIjoxNTE2MTY3OTkxfQ.MsCnRzAAc1xVvl0NAabKNMJVAUUStZsD9gicke8Qjmdeybdq3ldQQZymHzvuJftrVeHTGSwF8qHY2PVgiAWlYQ%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218616276129%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNjI3NjEyOSIsImlhdCI6MTUwMDYxNTk5MSwiZXhwIjoxNTE2MTY3OTkxfQ.MsCnRzAAc1xVvl0NAabKNMJVAUUStZsD9gicke8Qjmdeybdq3ldQQZymHzvuJftrVeHTGSwF8qHY2PVgiAWlYQ; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1500021206,1500258035,1500344269,1500601018; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1500616734; _csrf=o8z9t+WqHWiF39cHAhGZLg==; OA=3Cx6VruE2kuSVPV+1TE4DTAc7tflzyPIT47DnLghto8=; _csrf_bk=3ef680caabecf3c632f5568b1175ba1b"
    # return "aliyungf_tc=AQAAAEpceBjKBAgAmjPOjMpK8S3gcp5Y; csrfToken=P4EQk1XfLy_QKodS4xmZJwrF; TYCID=524bcc5065d811e7b9c29dc37630003d; uccid=d28748c439794182559b00c010374433; Qs_lvt_117460=1499736539; ssuid=8589801555; bannerFlag=true; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNjI3NjEyOSIsImlhdCI6MTQ5OTc1NTUyNCwiZXhwIjoxNTE1MzA3NTI0fQ.bR4jMjs1GYVvRTrq1CArVu83zBaHEU5dvamkNIHucoEOz27NV5NqcCbSbQdTGRApBc5DMAb6G0keJ9-3oADf1A; tyc-user-info=eyJuZXciOiIxIiwidG9rZW4iOiJleUpoYkdjaU9pSklVelV4TWlKOS5leUp6ZFdJaU9pSXhPRFl4TmpJM05qRXlPU0lzSW1saGRDSTZNVFE1T1RjMU5UVXlOQ3dpWlhod0lqb3hOVEUxTXpBM05USTBmUS5iUjRqTWpzMUdZVnZSVHJxMUNBclZ1ODN6QmFIRVU1ZHZhbWtOSUh1Y29FT3oyN05WNU5xY0NiU2JRZFRHUkFwQmM1RE1BYjZHMGtlSjktM29BRGYxQSIsInN0YXRlIjoiMCIsInZudW0iOiIwIiwib251bSI6IjAiLCJtb2JpbGUiOiIxODYxNjI3NjEyOSJ9; _csrf=Je+JfhIUqLyTIBtp0aWEZQ==; OA=3Cx6VruE2kuSVPV+1TE4DaJ9O+wMFTIyG1GhDtBEDVE=; _csrf_bk=5f9bdc862f924e83124ea3d6bec3ecc1; Qs_pv_117460=3145285219619399700%2C2104179738042492700%2C4325340420087389000%2C1788485526523481000%2C2866283175686035000; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1499736540; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1499755520"
    # return "TYCID=524bcc5065d811e7b9c29dc37630003d; uccid=d28748c439794182559b00c010374433; ssuid=8589801555; Qs_lvt_117460=1499766091%2C1499823015%2C1499853576%2C1499913460%2C1500021205; Qs_pv_117460=2272283127989564700%2C3340376594904068600%2C2898491103211486000%2C2578886036208478700%2C3441978495829755400; aliyungf_tc=AQAAAITssFi5xAQAmjPOjE7ZurHyaTMy; csrfToken=SXCdvh6JHsojPITX2lZsXaHW; RTYCID=0cebe72293e8477f8851bee4e5419b3b; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNjI3NjEyOSIsImlhdCI6MTUwMDM0NTQ5MSwiZXhwIjoxNTE1ODk3NDkxfQ.Bqpuicwf-eU7uLUJO7cuv-W8Mhj8JlhB3SypgPzIdLyiLhs5VtXNLIoSgR9f84jd7Avw6CN4U51tMYzzi7OQcA%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218616276129%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNjI3NjEyOSIsImlhdCI6MTUwMDM0NTQ5MSwiZXhwIjoxNTE1ODk3NDkxfQ.Bqpuicwf-eU7uLUJO7cuv-W8Mhj8JlhB3SypgPzIdLyiLhs5VtXNLIoSgR9f84jd7Avw6CN4U51tMYzzi7OQcA; _csrf=8uwbdogIDcLFs92GfVc36g==; OA=3Cx6VruE2kuSVPV+1TE4DT2QGtmqUJN41cbZoXiw/Zc=; _csrf_bk=72e8ca7c6f4441a88b70e6a75dca0e83; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1499913461,1500021206,1500258035,1500344269; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1500345488"
    # return "TYCID=524bcc5065d811e7b9c29dc37630003d; uccid=d28748c439794182559b00c010374433; ssuid=8589801555; Qs_lvt_117460=1499766091%2C1499823015%2C1499853576%2C1499913460%2C1500021205; Qs_pv_117460=2272283127989564700%2C3340376594904068600%2C2898491103211486000%2C2578886036208478700%2C3441978495829755400; aliyungf_tc=AQAAAITssFi5xAQAmjPOjE7ZurHyaTMy; csrfToken=SXCdvh6JHsojPITX2lZsXaHW; RTYCID=0cebe72293e8477f8851bee4e5419b3b; bannerFlag=true; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNjI3NjEyOSIsImlhdCI6MTUwMDM3MjM3NSwiZXhwIjoxNTE1OTI0Mzc1fQ.sHqmwu76jod9hcUSVnxEjKtadK8Igd8-XC01CE5X8aJjGt52cFcPaKzQKm2ZedJhV-0S4m3bsRuvH0Z1Q4qQJg%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218616276129%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNjI3NjEyOSIsImlhdCI6MTUwMDM3MjM3NSwiZXhwIjoxNTE1OTI0Mzc1fQ.sHqmwu76jod9hcUSVnxEjKtadK8Igd8-XC01CE5X8aJjGt52cFcPaKzQKm2ZedJhV-0S4m3bsRuvH0Z1Q4qQJg; _csrf=TcX/Z0sVELnzR1ycnZR29A==; OA=3Cx6VruE2kuSVPV+1TE4DSP6XBft4+F5uyKcgkNIjjHx6u0fUGqJ0aRiV2b7dB83; _csrf_bk=80294d83005d61960b9fb26afff32ba6; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1499913461,1500021206,1500258035,1500344269; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1500372386"
    # return "TYCID=524bcc5065d811e7b9c29dc37630003d; uccid=d28748c439794182559b00c010374433; ssuid=8589801555; Qs_lvt_117460=1499766091%2C1499823015%2C1499853576%2C1499913460%2C1500021205; Qs_pv_117460=2272283127989564700%2C3340376594904068600%2C2898491103211486000%2C2578886036208478700%2C3441978495829755400; aliyungf_tc=AQAAAHxcpw9MhAMAmjPOjJGubkAUCklI; csrfToken=n_8l_YQxo7FtMATJLbG1oWgn; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNjI3NjEyOSIsImlhdCI6MTUwMDk0NTk0MCwiZXhwIjoxNTE2NDk3OTQwfQ.PF4KnLXqEEJEh8Ajw8ezgbWvBFqD5aKFHOG24dFvSg7b7IirZeJFfGMpZ_SPiI3ae3s9OpOI0hI03ztgmavMKg%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218616276129%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNjI3NjEyOSIsImlhdCI6MTUwMDk0NTk0MCwiZXhwIjoxNTE2NDk3OTQwfQ.PF4KnLXqEEJEh8Ajw8ezgbWvBFqD5aKFHOG24dFvSg7b7IirZeJFfGMpZ_SPiI3ae3s9OpOI0hI03ztgmavMKg; _csrf=BcroGUPlGUos580LM0y3Tg==; OA=3Cx6VruE2kuSVPV+1TE4DT4YHxH4Cxo5NZeWWMV/Uv8B5nTQM/5+KMDLCbteA3hm; _csrf_bk=31df31200f6de6cf7069c3e0df2b65fd; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1500258035,1500344269,1500601018,1500945896; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1500948422"
    # return "TYCID=524bcc5065d811e7b9c29dc37630003d; uccid=d28748c439794182559b00c010374433; ssuid=8589801555; Qs_lvt_117460=1499766091%2C1499823015%2C1499853576%2C1499913460%2C1500021205; Qs_pv_117460=2272283127989564700%2C3340376594904068600%2C2898491103211486000%2C2578886036208478700%2C3441978495829755400; aliyungf_tc=AQAAAAHJdh5EtA0AmjPOjOmWXLjr5XCI; csrfToken=XAxdungISDg3CKKPx37fytNF; _csrf=qX9qiqZvo+ucmPWDtNf4iA==; OA=3Cx6VruE2kuSVPV+1TE4De7le3vl5QWBNvN8kk/dQtM=; _csrf_bk=5ce20ab8bf85e69d6d08b7505a9fdaa2; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1500964934,1501034544; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1501039210; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNjI3NjEyOSIsImlhdCI6MTUwMTAzOTMyNywiZXhwIjoxNTE2NTkxMzI3fQ.dv-FrctxhMaCXrekzabOVsY5bIVEOEaWC4VMTWAjLGezzajrEx_aqtHg3fehZhPCopvGKUZ-8tBVjbRfbhubvg%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218616276129%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNjI3NjEyOSIsImlhdCI6MTUwMTAzOTMyNywiZXhwIjoxNTE2NTkxMzI3fQ.dv-FrctxhMaCXrekzabOVsY5bIVEOEaWC4VMTWAjLGezzajrEx_aqtHg3fehZhPCopvGKUZ-8tBVjbRfbhubvg"
    # 188
    # return "TYCID=524bcc5065d811e7b9c29dc37630003d; uccid=d28748c439794182559b00c010374433; ssuid=8589801555; RTYCID=d925d0a530e84408a4d45e57ecf79f1b; aliyungf_tc=AQAAAC7MpnO0OAAAmjPOjMRwC/1tI8MW; csrfToken=7lmLyA_aGUWQW152QGuUYUt3; Qs_lvt_117460=1499736539%2C1499766091%2C1499823015; bannerFlag=true; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNjI3NjEyOSIsImlhdCI6MTQ5OTg0NzcwNiwiZXhwIjoxNTE1Mzk5NzA2fQ.Kv8ale2yr9phufBQn6HM-abg17cozr_84Xp8cazUOqJCXwOUOBuZWU_MVOewueHmA_BulTKnX-NzvNnj_YJuwQ; tyc-user-info=eyJ0b2tlbiI6ImV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE9EWXhOakkzTmpFeU9TSXNJbWxoZENJNk1UUTVPVGcwTnpjd05pd2laWGh3SWpveE5URTFNems1TnpBMmZRLkt2OGFsZTJ5cjlwaHVmQlFuNkhNLWFiZzE3Y296cl84NFhwOGNhelVPcUpDWHdPVU9CdVpXVV9NVk9ld3VlSG1BX0J1bFRLblgtTnp2Tm5qX1lKdXdRIiwic3RhdGUiOiIwIiwidm51bSI6IjAiLCJvbnVtIjoiMCIsIm1vYmlsZSI6IjE4NjE2Mjc2MTI5In0=; _csrf=gF+WMxu+EVuZy3CTNwAr6g==; OA=3Cx6VruE2kuSVPV+1TE4DT2QGtmqUJN41cbZoXiw/Zc=; _csrf_bk=72e8ca7c6f4441a88b70e6a75dca0e83; Qs_pv_117460=1892496352197804300%2C4195451213875873300%2C2215184993117022700%2C2579755517977410600%2C3877098265130537000; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1499736540,1499823016; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1499847710"
    # return "TYCID=524bcc5065d811e7b9c29dc37630003d; uccid=d28748c439794182559b00c010374433; ssuid=8589801555; Qs_lvt_117460=1499766091%2C1499823015%2C1499853576%2C1499913460%2C1500021205; Qs_pv_117460=2272283127989564700%2C3340376594904068600%2C2898491103211486000%2C2578886036208478700%2C3441978495829755400; aliyungf_tc=AQAAAKArwVUpogUAmjPOjIZHFdwrb8X7; csrfToken=Z2Sb7N3Yz2roq-lI2_2oJN3i; bannerFlag=true; tyc-user-info=%257B%2522new%2522%253A%25221%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODg2MjAwMjk2MiIsImlhdCI6MTUwMDI2Mzk2NywiZXhwIjoxNTE1ODE1OTY3fQ.sOCUgYZ5FLGy3ynNRZJ6lGAm67HxnZgR4df06XDExu7oGQqjCxlEzvTDneiPQ2-XweHWXGM6VmHhmWWHBMfDTQ%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218862002962%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODg2MjAwMjk2MiIsImlhdCI6MTUwMDI2Mzk2NywiZXhwIjoxNTE1ODE1OTY3fQ.sOCUgYZ5FLGy3ynNRZJ6lGAm67HxnZgR4df06XDExu7oGQqjCxlEzvTDneiPQ2-XweHWXGM6VmHhmWWHBMfDTQ; _csrf=InK5isx3flC3tIm1HCATxw==; OA=3Cx6VruE2kuSVPV+1TE4DT2QGtmqUJN41cbZoXiw/Zc=; _csrf_bk=72e8ca7c6f4441a88b70e6a75dca0e83; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1499823016,1499913461,1500021206,1500258035; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1500263964"
    # return "TYCID=524bcc5065d811e7b9c29dc37630003d; uccid=d28748c439794182559b00c010374433; ssuid=8589801555; Qs_lvt_117460=1499766091%2C1499823015%2C1499853576%2C1499913460%2C1500021205; Qs_pv_117460=2272283127989564700%2C3340376594904068600%2C2898491103211486000%2C2578886036208478700%2C3441978495829755400; aliyungf_tc=AQAAAITssFi5xAQAmjPOjE7ZurHyaTMy; csrfToken=SXCdvh6JHsojPITX2lZsXaHW; RTYCID=0cebe72293e8477f8851bee4e5419b3b; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODg2MjAwMjk2MiIsImlhdCI6MTUwMDM0NTIyOSwiZXhwIjoxNTE1ODk3MjI5fQ.Zc4XGIA9Ee5XUCjox9s-FWz1QpNRuRWycFEuEDELSIfVqRs-tyg1tyKEdTJ_niB-QSiiK-MaYPAVyqf0H_7pMA%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218862002962%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODg2MjAwMjk2MiIsImlhdCI6MTUwMDM0NTIyOSwiZXhwIjoxNTE1ODk3MjI5fQ.Zc4XGIA9Ee5XUCjox9s-FWz1QpNRuRWycFEuEDELSIfVqRs-tyg1tyKEdTJ_niB-QSiiK-MaYPAVyqf0H_7pMA; _csrf=ziKMwH4YIlpCSeVpo2MroA==; OA=3Cx6VruE2kuSVPV+1TE4Dc8jjHb3E3ftfIe9rQ3iqBo06mMAuzsVf9suFXpviLlvhUDKAx8W7fgDdGmu8vBVV1897muD/tFZX9diNj2uSGuzdn11EXZCDikKv+oIXFg8rhZrcHe+b7W5sbohvO2IHz0QSDdotoIaK9SeICCDCUSd/FQQJ2/aBhL4Q0+ZnokQ; _csrf_bk=9dc20e9317b9bfde55b1e98e11e99c01; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1499913461,1500021206,1500258035,1500344269; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1500345286"
    # return "TYCID=524bcc5065d811e7b9c29dc37630003d; uccid=d28748c439794182559b00c010374433; ssuid=8589801555; Qs_lvt_117460=1499766091%2C1499823015%2C1499853576%2C1499913460%2C1500021205; Qs_pv_117460=2272283127989564700%2C3340376594904068600%2C2898491103211486000%2C2578886036208478700%2C3441978495829755400; aliyungf_tc=AQAAAITssFi5xAQAmjPOjE7ZurHyaTMy; csrfToken=SXCdvh6JHsojPITX2lZsXaHW; RTYCID=0cebe72293e8477f8851bee4e5419b3b; bannerFlag=true; _csrf=IM7yknrYJEhDqVKUDiSfyw==; OA=3Cx6VruE2kuSVPV+1TE4Dc8jjHb3E3ftfIe9rQ3iqBo06mMAuzsVf9suFXpviLlv4yCIa1dpNOnMS4qRmwLgIt3CYOTE28lb5c9+f9KpaVP0ENsXqbZalmQ/6Br6kUoUNo4GjdFfOl8o5QmE+aR8mFQ4Zd0wIGZ+9InaZ7o0BaFrgLDCSOqHqej083SA9HNuCh8Z/IPK2zggyDNXxXy8Dq92/+qe1lIKWs7ANtSapQaj3/c9XF4AAq8gieioht4p; _csrf_bk=03e620e4d959ca105dcf147c2bb7f879; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1499913461,1500021206,1500258035,1500344269; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1500370994"
    # return "TYCID=524bcc5065d811e7b9c29dc37630003d; uccid=d28748c439794182559b00c010374433; ssuid=8589801555; Qs_lvt_117460=1499766091%2C1499823015%2C1499853576%2C1499913460%2C1500021205; Qs_pv_117460=2272283127989564700%2C3340376594904068600%2C2898491103211486000%2C2578886036208478700%2C3441978495829755400; aliyungf_tc=AQAAAAHJdh5EtA0AmjPOjOmWXLjr5XCI; csrfToken=XAxdungISDg3CKKPx37fytNF; _csrf=hO6Krax2J6pkw+pUJxxzeQ==; OA=3Cx6VruE2kuSVPV+1TE4De7le3vl5QWBNvN8kk/dQtM=; _csrf_bk=5ce20ab8bf85e69d6d08b7505a9fdaa2; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1500964934,1501034544; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1501041204; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODg2MjAwMjk2MiIsImlhdCI6MTUwMTA0MTIzNywiZXhwIjoxNTE2NTkzMjM3fQ.sOIlQbu21FgLbNY681D4A3UbnfF3N-wM5jTLnT9S6uhOkfmN4zlLmEO1bdoB3tAl79TwySX6o3-xLwGPTHaU_A%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218862002962%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODg2MjAwMjk2MiIsImlhdCI6MTUwMTA0MTIzNywiZXhwIjoxNTE2NTkzMjM3fQ.sOIlQbu21FgLbNY681D4A3UbnfF3N-wM5jTLnT9S6uhOkfmN4zlLmEO1bdoB3tAl79TwySX6o3-xLwGPTHaU_A"
    #185
    return "TYCID=524bcc5065d811e7b9c29dc37630003d; uccid=d28748c439794182559b00c010374433; ssuid=8589801555; Qs_lvt_117460=1499766091%2C1499823015%2C1499853576%2C1499913460%2C1500021205; Qs_pv_117460=2272283127989564700%2C3340376594904068600%2C2898491103211486000%2C2578886036208478700%2C3441978495829755400; RTYCID=bbe929ad14d5496ba8530600afc13fa6; aliyungf_tc=AQAAACYInkOFGg8AmjPOjBeTzz9Kwit9; csrfToken=f9KQoF_ylC19c7zu1yr80x5b; bannerFlag=true; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODUyMTcwNjU5MSIsImlhdCI6MTUwMTE0NDUxNywiZXhwIjoxNTE2Njk2NTE3fQ.Ryi6qYV4HX01UmI9fItjazBnOPYPEYBnIbBJtXtbJsruTCXAJPPVk0a75p0-tk92e1sF65Nh0wjXJowhS7OBeg%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218521706591%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODUyMTcwNjU5MSIsImlhdCI6MTUwMTE0NDUxNywiZXhwIjoxNTE2Njk2NTE3fQ.Ryi6qYV4HX01UmI9fItjazBnOPYPEYBnIbBJtXtbJsruTCXAJPPVk0a75p0-tk92e1sF65Nh0wjXJowhS7OBeg; _csrf=0aTEgZ2Zh+k4YGrKDR4Reg==; OA=3Cx6VruE2kuSVPV+1TE4DaJ9O+wMFTIyG1GhDtBEDVE=; _csrf_bk=5f9bdc862f924e83124ea3d6bec3ecc1; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1500964934,1501034544,1501119247; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1501144518"
        # "TYCID=524bcc5065d811e7b9c29dc37630003d; uccid=d28748c439794182559b00c010374433; ssuid=8589801555; Qs_lvt_117460=1499766091%2C1499823015%2C1499853576%2C1499913460%2C1500021205; Qs_pv_117460=2272283127989564700%2C3340376594904068600%2C2898491103211486000%2C2578886036208478700%2C3441978495829755400; aliyungf_tc=AQAAAAHJdh5EtA0AmjPOjOmWXLjr5XCI; csrfToken=XAxdungISDg3CKKPx37fytNF; RTYCID=bbe929ad14d5496ba8530600afc13fa6; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODUyMTcwNjU5MSIsImlhdCI6MTUwMTA2MjAwMywiZXhwIjoxNTE2NjE0MDAzfQ.obbPwEenE2Xh_A2UA7ui1EcuCcZtR5ZdFfJ22wos4br01nDPaPjoOUlc8Yh_MUZp8LNThtUCxRBIOrKFdcPlAg%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218521706591%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODUyMTcwNjU5MSIsImlhdCI6MTUwMTA2MjAwMywiZXhwIjoxNTE2NjE0MDAzfQ.obbPwEenE2Xh_A2UA7ui1EcuCcZtR5ZdFfJ22wos4br01nDPaPjoOUlc8Yh_MUZp8LNThtUCxRBIOrKFdcPlAg; _csrf=MBDtPjZ2yfb0ZE4aN6evFw==; OA=3Cx6VruE2kuSVPV+1TE4DT2QGtmqUJN41cbZoXiw/Zc=; _csrf_bk=72e8ca7c6f4441a88b70e6a75dca0e83; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1500964934,1501034544; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1501062005"
        # "TYCID=524bcc5065d811e7b9c29dc37630003d; uccid=d28748c439794182559b00c010374433; ssuid=8589801555; Qs_lvt_117460=1499766091%2C1499823015%2C1499853576%2C1499913460%2C1500021205; Qs_pv_117460=2272283127989564700%2C3340376594904068600%2C2898491103211486000%2C2578886036208478700%2C3441978495829755400; aliyungf_tc=AQAAAAHJdh5EtA0AmjPOjOmWXLjr5XCI; csrfToken=XAxdungISDg3CKKPx37fytNF; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODUyMTcwODA3NSIsImlhdCI6MTUwMTA0NzgzMywiZXhwIjoxNTE2NTk5ODMzfQ.5b5ACAoO3oGbMlFSKeMWtf-VboEE1v1t2IdrRtf9YLgtp68jokK0KNx3AiVCFPS5IK_QP1nIjwaDFNzTpQMnDg%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218521708075%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODUyMTcwODA3NSIsImlhdCI6MTUwMTA0NzgzMywiZXhwIjoxNTE2NTk5ODMzfQ.5b5ACAoO3oGbMlFSKeMWtf-VboEE1v1t2IdrRtf9YLgtp68jokK0KNx3AiVCFPS5IK_QP1nIjwaDFNzTpQMnDg; _csrf=IcS8mSAOwUwjXKjjvfWRog==; OA=3Cx6VruE2kuSVPV+1TE4DT2QGtmqUJN41cbZoXiw/Zc=; _csrf_bk=72e8ca7c6f4441a88b70e6a75dca0e83; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1500964934,1501034544; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1501047833"


def check_illegal(text):
    illegal = ["v", "-", "x", "y", "%", "\\", "/"]
    for k in illegal:
        if k in text:
            text = text.replace(k, "")
    return text


def get_company_url(conn):
    select_sql = "SELECT company_name,source_url FROM WDZJ_PLAT_COMPANY_SPIDER"
    app_management = pd.read_sql(select_sql, conn)
    # ls_company = app_management.get("company_name")
    name_url = app_management
    return name_url
    # return [
    #         "上海诺诺镑客金融信息服务有限公司",]
#             "泰州市瑞银创投电子商务股份有限公司",
#             "微贷（杭州）金融信息服务有限公司",
#             "上海你我贷互联网金融信息服务有限公司",
#             "上海融斗金融信息服务有限公司",
#             "上海拍拍贷金融信息服务有限公司",
#             "江苏三六五易贷金融信息服务股份有限公司",
#             "人人贷商务顾问（北京）有限公司",   #
#             "上海陆家嘴国际金融资产交易市场股份有限公司",      #
#             "红岭创投电子商务股份有限公司",
#             "恒诚科技发展（北京）有限公司",
#             "东莞团贷网互联网科技服务有限公司",    #
#             "君安信（北京）科技有限公司",
#             "深圳市人人聚财金融信息服务有限公司",
#             "新新贷（上海）金融信息服务有限公司",
#             "深圳投哪金融服务有限公司",
#             "武汉一起好金融信息服务股份有限公司",
#             "银渠金融信息服务（上海）股份有限公司",
#             "温州三信融民间融资信息服务有限公司",
#             "宜宾四达投资有限责任公司",
#             "广州市圈圈贷互联网金融信息服务有限公司",
#             "温州宏信融资担保有限公司",
#             "开鑫贷融资服务江苏有限公司",
#             "深圳市合拍在线互联网金融服务有限公司",
#             "合力贷（北京）科技有限公司",
            # "深圳市感融互联网金融服务有限公司",
            # "深圳融信网金信息科技有限公司",
            # "北京易通贷金融信息服务有限公司",
            # "深圳市信融财富投资管理有限公司",
            # "上海点荣金融信息服务有限责任公司",
            # "湖南满满网络科技有限公司",
            # "北京弘合柏基金融信息服务有限责任公司",
            # "北京同城翼龙网络科技有限公司",
            # "深圳市万家兄弟电子商务有限公司",
            # "深圳宜聚互联网金融服务有限公司",
            # "北京汇聚财富管理咨询有限公司",
            # "广信联合（北京）商务顾问有限公司",
            # "安投融（北京）网络科技有限公司",
            # "上海雪山金融信息服务有限公司",
            # "上海合盘金融信息服务股份有限公司",
            # "宁波宁创金融科技有限公司",
            # "贵州合石电子商务有限公司",
            # "深圳市资本在线金融信息服务有限公司",
            # "深圳前海融金所互联网金融服务有限公司",
            # "江西惠众金融信息服务股份有限公司",
            # "广州达为尊投资管理有限公司",
            # "浙江温商贷互联网金融服务有限公司",
            # "深圳金海贷金融服务有限公司",
            # "深圳市钱爸爸电子商务有限公司",
            # "成都伟品资产管理有限公司",
            # "深圳市广富宝金融信息服务有限公司",
            # "深圳市小牛在线互联网信息咨询有限公司",
            # "宁波平平投资咨询有限公司",
            # "和信电子商务有限公司",
            # "广东新佳联投资管理有限公司",
            # "深圳市诚汇通金融信息有限公司",
            # "武汉玖信普惠金融信息服务有限公司",
            # "安徽皖都金融信息服务有限公司",
            # "北京乐融多源信息技术有限公司",
            # "深圳市赢众通金融信息服务有限责任公司",
            # "福建信和贷金融信息服务有限公司",
            # "信用宝金融信息服务（北京）有限公司",
            # "温州佰卓商务信息咨询有限公司",
            # "上海国诚金融信息服务有限公司",
#             "上海互信金融信息服务有限公司",
#             "山东丁丁金融信息咨询服务有限公司",
#             "深圳市智融财富电商投资有限公司",
#             "深圳合时代金融服务有限公司",
#             "广州礼德互联网金融信息服务有限公司",
#             "深圳地标金融服务有限公司",
#             "杭州商富商务信息咨询有限公司",
#             "上海爱投金融信息服务有限公司",
#             "四川创融投资有限公司",
#             "北京证大向上金融信息服务有限公司",
#             "南京胜沃投资管理有限公司",
#             "武汉易融恒信金融信息服务有限公司",
#             "江西真鑫贷金融服务有限公司",
#             "云南达煜投资有限公司",
#             "深圳市恒领投资咨询有限公司",
#             "胖毛在线（厦门）金融技术服务股份有限公司",
#             "北京花果信息技术有限公司",
#             "深圳前海斯坦德互联网金融服务有限公司",
#             "深圳市闲钱宝电子商务有限公司",
#             "贵州中小乾信金融信息服务有限公司",
#             "厦门利好贷投资管理有限公司",
#             "上海义帆互联网金融信息服务有限公司",
#             "中微（北京）信用管理有限公司",
#             "深圳市后河网互联网金融服务有限公司",
#             "赣州发展融通资产管理有限公司",
#             "安义县凤凰金融服务有限公司",
#             "温州众人通民间融资信息服务有限公司",
#             "银客金融信息服务（北京）有限公司",
#             "深圳市立业贷互联网金融服务有限公司",
#             "石家庄人文投资咨询有限公司",
#             "上海金银猫金融服务有限公司",
#             "上海永利宝金融信息服务有限公司",
#             "重庆兴农鑫电子商务有限公司",
#             "北京东方财蕴金融信息服务有限公司",
#             "济宁市盛元非融资性担保有限公司",
#             "江西懿懿投资咨询有限公司",
#             "江苏宝贝金融信息服务有限公司",
#             "深圳市共信赢金融信息服务有限公司",
#             "上海旭胜金融信息服务股份有限公司",
#             "深圳前海宜宝金融服务有限公司",
#             "金华佳誉文化传媒有限公司",
#             "鄂汇金融服务（武汉）有限公司",
#             "陕西金开贷金融服务有限公司",
#             "广州鹏誉商务服务有限公司",
#             "上海超爱才金融信息服务有限公司",
#             "万惠投资管理有限公司",
#             "北京网融天下金融信息服务有限公司",
#             "码头益（大连）互联网信息服务有限公司",
#             "杭州鑫合汇互联网金融服务有限公司",
#             "福建中金联合金融服务有限公司",
#             "深圳市首控微金资本管理控股有限公司",
#             "金信金融信息服务（北京）有限公司",
#             "惠州市东门投资股份有限公司",
#             "信和上融网络科技（北京）有限公司",
#             "北京聚融天下信息技术有限公司",
#             "青岛金源投资控股有限公司",
#             "北京普天贷金融信息服务有限公司",
#             "先智创科（北京）科技有限公司",
#             "北京抱财金融信息服务有限公司",
#             "北城贷（北京）资本管理有限公司",
#             "广东嘉友网络科技有限公司",
#             "宁夏宁安贷投资咨询有限公司",
#             "深圳市前海泰丰融通金融服务有限公司",
#             "大同航（北京）网络科技有限公司",
#             "好收益（北京）金融信息服务有限公司",
#             "杭州宝江投资管理有限公司",
#             "深圳钱来网金融信息服务有限公司",
#             "深圳市前海理想金融控股有限公司",
#             "河北安凯投资有限公司",
#             "融通汇信信息科技（北京）有限公司",
#             "上海长久金融信息服务集团有限公司",
#             "四川森淼融联科技有限公司",
#             "北京爱钱帮财富科技有限公司",
#             "惠众商务顾问（北京）有限公司",
#             "龙贷在线投资（北京）有限公司",
#             "武汉小富金融信息服务股份有限公司",
#             "银湖网络科技有限公司",
#             "实投（上海）互联网金融信息服务有限公司",
#             "北京凤凰信用管理有限公司",
#             "河南聚金金融服务有限责任公司",
#             "江西东方融信金融信息服务有限公司",
#             "深圳市财富之家金融网络科技服务有限公司",
#             "安徽德众金融信息服务有限公司",
#             "贵州融信通投融资服务有限责任公司",
#             "深圳前海联金所金融信息服务有限公司",
#             "北京领先创融网络科技有限公司",
#             "久亿恒远（北京）科技有限公司",
#             "宏韶投资管理（上海）有限公司",
#             "菏泽融达金融信息咨询有限公司",
#             "星果时代信息技术有限公司",
#             "北京两只老虎电子商务有限公司",
#             "广东稳贷电子商务有限公司",
#             "上海睿本金融信息服务有限公司",
#             "快快金融信息服务（上海）有限公司",
#             "青岛钱吧金融信息服务有限公司",
#             "成都瑞骐金融服务外包有限公司",
#             "北京恒隆必信科技有限公司",
#             "爱钱进（北京）信息科技有限公司",
#             "北京雍和金融信息服务有限公司",
#             "江苏强业金融信息服务有限公司",
#             "南京易投贷金融信息服务有限公司",
#             "广东壹宝资产管理有限公司",
#             "深圳市收获宝互联网金融服务有限公司",
#             "长沙浩友汇网络科技有限公司",
#             "深圳达人贷互联网金融服务企业(有限合伙)",
#             "浙江惠惠金融信息服务有限公司",
#             "广东天天财富股份有限公司",
#             "深圳前海新富创新金融服务有限公司",
#             "上海合米金融信息服务有限公司",
#             "汇投（北京）金融信息服务有限公司",
#             "深圳融金宝互联网金融服务有限公司",
#             "深圳市前海果树互联网金融服务有限公司",
#             "贵州国信通电子商务有限公司",
#             "阜阳市福利元投资咨询有限公司",
#             "山东乾山元亨商务顾问有限公司",
#             "广州易贷金融信息服务股份有限公司",
#             "上海捷财金融信息服务有限公司",
#             "金联储（北京）金融信息服务有限公司",
#             "江西广裕金融管理有限公司",
#             "广州金控网络金融服务股份有限公司",
#             "广西钱盆科技股份有限公司",
#             "泉州中金在线金融服务有限公司",
#             "北京平安永信投资咨询有限公司",
#             "北京众信金融信息服务有限公司",
#             "湖北中金高科金融服务有限公司",
#             "北京网利科技有限公司",
#             "深圳前海图腾互联网金融服务有限公司",
#             "深圳市珠宝贷互联网金融服务股份有限公司",
#             "江西沃信营销策划股份有限公司",
#             "北京易融德利网络科技有限公司",
#             "湖北口碑金融信息服务有限公司",
#             "广州御泰互联网金融信息服务有限公司",
#             "上海浩禄投资管理有限公司",
#             "微车融投商务顾问（北京）有限公司",
#             "广东安星财富管理有限公司",
#             "厦门四方乾金融技术服务有限公司",
#             "重庆财神在线投资信息服务有限公司",
#             "杭州拓道互联网金融服务有限公司",
#             "深圳小微金融服务有限公司",
#             "深圳市前海中金互联网金融服务有限公司",
#             "深圳市亿钱贷电子商务有限公司",
#             "上海易贷网金融信息服务有限公司",
#             "上海鸿翔银票网互联网金融信息服务有限公司",
#             "安徽步步盈金融信息服务有限公司",
#             "北京海豚隆隆网络科技有限公司",
#             "上海橙旗金融信息服务有限公司",
#             "深圳市钱盒子金融信息服务有限公司",
#             "深圳市喜投金融服务有限公司",
#             "重庆金宝保信息技术服务有限公司",
#             "上海新居金融信息服务有限公司",
#             "云南贷贷网络信息科技有限公司",
#             "深圳市汇联互联网金融服务有限公司",
#             "山东国晟中融宝信息技术有限公司",
#             "山东广博仁义信息管理咨询有限公司",
#             "上海苏融贷金融信息服务有限公司",
#             "北京乾智冠融信息服务有限公司",
#             "永嘉温易贷金融信息服务有限公司",
#             "江苏金票通金融信息服务有限公司",
#             "金华瑞涛投资管理有限公司",
#             "江西美美信息科技有限公司",
#             "河南百融金融服务有限公司",
#             "北京紫貔财富网络科技有限公司",
#             "深圳前海中广核富盈互联网金融服务有限公司",
#             "深圳市前海小猪互联网金融服务有限公司",
#             "浙江小泰科技有限公司",
#             "深圳市腾邦创投有限公司",
#             "口贷网络服务股份有限公司",
#             "上海融道网金融信息服务有限公司",
#             "浙江聚有财金融服务外包有限公司",
#             "山东金谷盛通金融信息服务有限公司",
#             "上海哲珲金融信息服务有限公司",
#             "深圳市智融会金融服务有限公司",
#             "深圳前海金桥梁互联网金融服务有限公司",
#             "投米科技发展（北京）有限公司",
#             "湖北联众智横股权投资基金管理有限公司",
#             "融泰浩元（北京）网络科技有限公司",
#             "深圳钱途互联网金融服务有限公司",
#             "上海凯岸信息科技有限公司",
#             "贵州聚金汇投资管理有限责任公司",
#             "湖南万利民间投融资登记服务中心有限公司",
#             "四川投促金融信息服务有限公司",
#             "深圳市连连贷金融信息服务有限责任公司",
#             "江西省博汇九洲金融服务有限公司",
#             "深圳市鹏鼎创盈金融信息服务股份有限公司",
#             "武汉迅泊达金融服务有限公司",
#             "武汉乐居贷金融信息服务有限公司",
#             "云南鼎弘互联网金融信息服务有限公司",
#             "君融贷（北京）信息技术服务有限公司",
#             "北京百泉金融信息服务有限公司",
#             "江西禾泰财富金融服务有限公司",
#             "广西联银投资有限公司",
#             "深圳市创世佳鸿金融服务有限公司",
#             "深圳大麦理财互联网金融服务有限公司",
#             "浙江连枝互联网金融信息服务股份有限公司",
#             "信广立诚贷（北京）科技有限公司",
#             "青岛久信投资管理有限公司",
#             "成都众可电子商务股份有限公司",
#             "深圳市赢众通金融信息服务有限责任公司",
#             "山东润冠企业管理集团有限公司",
#             "上海荣幸信息科技有限公司",
#             "中投福瑞特（北京）科技有限公司",
#             "武汉引航世纪金融信息服务有限公司",
#             "重庆市亿信天合科技有限公司",
#             "四川众联财商务信息咨询有限公司",
#             "搜易贷（北京）金融信息服务有限公司",
#             "安禾财富（北京）网络科技有限公司",
#             "车能贷（上海）金融科技有限公司",
#             "福建小微时贷科技发展有限公司",
#             "深圳市产融贷金融服务有限公司",
#             "深圳前海网投互联网金融服务有限公司",
#             "深圳前海华人互联网金融服务集团有限公司",
#             "国鼎文化科技产业发展股份有限公司",
#             "京金所（北京）信息技术有限公司",
#             "安徽小马金融咨询服务有限公司",
#             "上海金柜投资管理有限公司",
#             "湖南利聚人普惠投资有限公司",
#             "深圳市拉拉金融信息服务有限公司",
#             "上海晓晟投资管理有限公司",
#             "杭州慧信行网络科技有限公司",
#             "浙江广众金融服务外包有限公司",
#             "宁夏如意财富金融电商信息服务有限公司",
#             "武汉一七八投资管理有限公司",
#             "民加科风信息技术有限公司",
#             "北京大刚信息科技股份有限公司",
#             "宁波易代通网络科技有限公司",
#             "北京恒昌利通投资管理有限公司",
#             "新疆丰汇财富金融信息服务有限公司",
#             "四平民间借贷服务有限公司",
#             "安徽红顶金融信息服务有限公司",
#             "北京荣盛信联信息技术有限公司",
#             "深圳福迈斯科技有限公司",
#             "微积金互联网金融服务（上海）有限公司",
#             "深圳智富圈互联网金融信息服务有限公司",
#             "福建融之家金融信息服务有限公司",
#             "安徽星昊金融信息服务有限公司",
#             "上海财来金融信息服务股份有限公司",
#             "山西天晨千亿投资有限公司",
#             "北京秒贷网电子商务股份有限公司",
#             "海金所（北京）金融信息服务有限公司",
#             "新疆启道资产管理股份有限公司",
#             "湖南省星展投资有限公司",
#             "武汉诚投网络有限公司",
#             "深圳前海中融投金融控股有限公司",
#             "重庆市隆金宝网络科技有限公司",
#             "重庆昕泓投资管理有限公司",
#             "肥城市桃都金融信息服务有限公司",
#             "湖北中兴财富金融信息服务股份有限公司",
#             "福建聚融在线金融技术服务有限公司",
#             "泰安德铢电子商务有限公司",
#             "福建互助金服金融技术服务有限公司",
#             "北京紫马财行投资管理有限公司",
#             "内蒙古钱道信息技术有限公司",
#             "湖北瑞银普惠金融服务有限公司",
#             "浙江九能资产管理有限公司",
#             "糖果（北京）金融信息服务股份有限公司",
#             "福建顺大金融信息服务有限公司",
#             "杭州捷创投资管理有限公司",
#             "杭州浙优民间资本理财服务有限公司",
#             "海宁中国皮革城互联网金融服务有限公司",
#             "浙江佰财金融信息服务有限公司",
#             "山东启腾投资咨询有限公司",
#             "上海米缸互联网金融信息服务有限公司",
#             "天津大友世纪科技有限公司",
#             "深圳大众在线网络科技有限公司",
#             "北京南来北往科技有限公司",
#             "南京万诺金融信息服务有限公司",
#             "上海相诚金融信息服务有限公司",
#             "四川邦宁投资管理有限公司",
#             "青岛汇泉财富金融信息服务有限公司",
#             "胖胖猪信息咨询服务（北京）有限公司",
#             "江苏天雄投资管理有限公司",
#             "宁波合众芸创财富投资管理有限公司",
#             "贵州银盟云商金融大数据有限公司",
#             "天津中正盛达资产管理有限公司",
#             "广东莞贷互联网信息服务有限公司",
#             "大连汇财在线信息技术有限公司",
#             "浙江小融网络科技股份有限公司",
#             "西安方元在线金融信息服务有限公司",
#             "北京融得宝投资管理有限公司",
#             "河南恒元进金融服务有限公司",
#             "深圳前海车富互联网金融服务有限公司",
#             "深圳市合伙人互联网金融服务有限公司",
#             "万富互联网信息科技有限公司",
#             "北京创利投网络科技有限公司",
#             "四川金粒子电子商务有限公司",
#             "重庆光华众投科技有限责任公司",
#             "百利市（北京）科技有限公司",
#             "固金所金融服务（深圳）有限公司",
#             "乾途金融信息服务（北京）有限公司",
#             "安徽福运和资产管理有限公司",
#             "北京道口贷科技有限公司",
#             "深圳前海广深发互联网金融服务有限公司",
#             "东方邦信金融科技（上海）有限公司",
#             "安徽皖乾资产管理有限公司",
#             "深圳前海用友力合金融服务有限公司",
#             "杭州铜米互联网金融服务有限公司",
#             "浙江隆泰高科信息科技有限公司",
#             "汉信互联网金融服务（武汉）股份有限公司",
#             "杭州聚车汇信息技术有限公司",
#             "广州优投互联网金融信息服务有限公司",
#             "深圳财火火金融服务有限公司",
#             "广东融汇商城电子商务有限公司",
#             "上海易办互联网金融信息服务有限公司",
#             "东莞市繁融实业投资有限公司",
#             "北京美锦互联网金融信息有限公司",
#             "上海福银涞互联网金融信息服务有限公司",
#             "智富金融信息服务（上海）有限公司",
#             "深圳市钱海湾金融服务有限公司",
#             "新疆冰川时代互联网金融信息服务有限公司",
#             "杭州首鸿金融信息服务有限公司",
#             "深圳市盛金创富互联网金融服务有限公司",
#             "安徽果儿金融信息服务有限公司",
#             "深圳市前海多赢金融服务有限公司",
#             "厦门睿曾金融信息技术服务有限公司",
#             "东方银谷（北京）投资管理有限公司",
#             "北京亿隆汇诚投资管理有限责任公司",
#             "深圳市同心科创金融服务有限公司",
#             "东莞市快捷资产管理有限公司",
#             "深圳前海惠德金融信息服务有限公司",
#             "金聚鑫（杭州）互联网金融服务有限公司",
#             "深圳杉汇通互联网金融服务有限公司",
#             "北京手投网投资控股有限公司",
#             "深圳市壹佰金融服务有限公司",
#             "武汉盈金所金融信息服务有限公司",
#             "泰安市兴泰创富广告传媒有限公司",
#             "拓天伟业（北京）金融信息服务有限公司",
#             "广州易票宝互联网金融信息服务有限公司",
#             "重庆通隆广电子商务有限公司",
#             "福建好家信息科技有限公司",
#             "深圳市鼎诚创投互联网金融服务有限公司",
#             "深圳前海大众互联网金融服务有限公司",
#             "深圳掌中财富互联网金融服务有限公司",
#             "上海倾信互联网金融信息服务有限公司",
#             "上海牛娃互联网金融信息服务有限公司",
#             "九信投资管理有限公司",
#             "深圳淘淘金互联网金融服务有限公司",
#             "中杰信德（北京）信息科技有限公司",
#             "江西小猪金融信息服务有限公司",
#             "齐鲁票据交易中心有限公司",
#             "上海隆培资产管理有限公司",
#             "江苏投吧金融信息服务有限公司",
#             "聚宝互联科技（深圳）股份有限公司",
#             "杭州稳瞻信息科技有限公司",
#             "四川善金金融服务外包有限公司",
#             "上海宝象金融信息服务有限公司",
#             "北京信融投资管理有限公司",
#             "青岛鲁金所股权投资基金有限公司",
#             "广州市联融互联网金融信息服务有限公司",
#             "安徽艾瑞贷信息技术服务有限公司",
#             "深圳首金誉互联网金融服务有限公司",
#             "深圳万盈互联网金融服务有限公司",
#             "广州知商互联网科技有限公司",
#             "金投手金融信息服务（北京）有限公司",
#             "深圳前海锐盈达互联网金融服务有限公司",
#             "宁波润丰金融科技有限公司",
#             "深圳青鱼金融服务有限公司",
#             "杭州易港诚互联网金融服务有限公司",
#             "深圳前海皓能互联网服务有限公司",
#             "北京易宝金融信息服务有限公司",
#             "吉林省融惠财智金融信息服务有限公司",
#             "杭州投融谱华互联网金融服务有限公司",
#             "潍坊永田电子商务有限公司",
#             "安徽唯源金融信息服务有限公司",
#             "贵州中融通贷投资管理有限公司",
#             "北京银邦客金融信息服务有限公司",
#             "北京诺米时代信息技术股份有限公司",
#             "深圳市前海好彩金融服务有限公司",
#             "车邦（深圳）互联网金融服务有限公司",
#             "宁波旺信投资管理有限公司",
#             "北京稳如泰山金融信息服务有限公司",
#             "北京佛尔斯特金融信息服务有限公司",
#             "上海翼勋互联网金融信息服务有限公司",
#             "深圳天天车财互联网金融服务有限公司",
#             "上海虎袍金融信息服务有限公司",
#             "深圳元亨财富金融信息服务有限公司",
#             "浙江多多互联网金融信息服务有限公司",
#             "北京联储在线金融信息服务有限公司",
#             "深圳合众财富金融投资管理有限公司",
#             "湖北皓添金融信息服务有限公司",
#             "深圳华金财富互联网金融服务有限公司",
#             "浙江人众金融服务股份有限公司",
#             "上海百渊金融信息服务有限公司",
#             "福建富瑞投资有限公司",
#             "深圳市前海领投互联网金融服务有限公司",
#             "深圳汇海易融互联网金融服务有限公司",
#             "上海亦攸金融信息服务有限公司",
#             "上海鱼耀金融信息服务有限公司",
#             "上海隆筹金融信息服务有限公司",
#             "福建陀飞轮网络科技有限公司",
#             "广州市富珉泰投资管理有限公司",
#             "中融金（北京）科技有限公司",
#             "诺远科技发展有限公司",
#             "北京汇聚融达网络科技有限公司",
#             "上海云旌互联网金融信息服务有限公司",
#             "北京融艺投信息科技有限公司",
#             "池州万家金融服务有限公司",
#             "乐享宝（厦门）金融信息服务有限公司",
#             "宁波乾友资产管理有限公司",
#             "武汉好易融互联网信息服务有限公司",
#             "温州金管家金融信息服务有限公司",
#             "深圳农泰金融服务有限公司",
#             "深圳前海小树时代互联网金融服务有限公司",
#             "冠群驰骋投资管理（北京）有限公司",
#             "北京首金中小微企业金融服务有限公司",
#             "杭州华之赢投资管理有限公司",
#             "河南麦如公寓管理有限公司",
#             "青州创智亿融商务咨询有限公司",
#             "淄博盛齐电子商务有限公司",
#             "徐州顺富电子商务有限公司",
#             "安徽悦享互联网金融信息服务有限公司",
#             "福建云朗网络科技有限公司",
#             "河南麦金顿资产管理有限公司",
#             "上海吾悠互联网金融信息服务有限公司",
#             "上海惠民益贷互联网金融信息服务有限公司",
#             "上海企骋金融信息服务有限公司",
#             "深圳汇通财富互联网金融服务有限公司",
#             "杭州小九投资管理有限公司",
#             "上海森昊投资管理有限公司",
#             "浙江投浙家金融服务外包有限公司",
#             "宁波六顺资产管理有限公司",
#             "深圳市小葱互联网金融服务有限公司",
#             "深圳前海易享资本管理有限公司",
#             "北京升值空间信息科技有限公司",
#             "深圳五维微品金融信息服务有限公司",
#             "江西来融金融信息服务有限公司",
#             "安徽四联金融服务有限公司",
#             "南京万金所金融信息服务有限公司",
#             "深圳市阿拉互联网金融服务有限公司",
#             "深圳市有喜资产管理有限公司",
#             "北京信诚时代投资管理有限公司",
#             "深圳市微镇信用支付科技有限公司",
#             "杭州满溢网络科技有限公司",
#             "金诺峰网络科技（北京）有限公司",
#             "甘肃金畅网络科技有限公司",
#             "上海玺鉴金融信息服务有限公司",
#             "深圳前海前沿互联网金融服务有限公司",
#             "山东雷恩丁金融信息技术服务股份有限公司",
#             "浙江银狐网络科技有限公司",
#             "杭州臻诚互联网金融服务有限公司",
#             "上海银砖金融信息服务有限公司",
#             "北京铭萱网络科技有限公司",
#             "浙江万维金融信息服务有限公司",
#             "上海新城金融信息服务有限公司",
#             "上海小虾网络科技有限公司",
#             "金砖财富信息科技有限公司",
#             "北京深蓝动力金融信息服务有限公司",
#             "北京诚易互动信息服务有限公司",
#             "中平瑞发（上海）互联网金融信息服务有限公司",
#             "北京善财信息技术有限公司",
#             "福建省莆商贷互联网金融服务有限公司",
#             "广州银承派互联网金融信息服务有限公司",
#             "小小黛朵（北京）科技有限公司",
#             "深圳智佳网络科技有限公司",
#             "国信财富（北京）信息科技有限公司",
#             "深圳融通聚富投资管理有限公司",
#             "深圳前海银管家互联网金融服务有限公司",
#             "深圳市咏湘鑫鑫科技有限公司",
#             "深圳市中利保投资管理有限公司",
#             "深圳尧舜禹天股权投资管理集团有限公司",
#             "深圳盛天信达投资管理有限公司",
#             "深圳市隆辉兴旺科技有限公司",
#             "深圳市财源众兴网络科技有限公司",
#             "德汇鑫（大连）投资管理有限公司",
#             "深圳市科迅投资有限公司",
#             "安徽嘉骏投资管理有限公司",
#             "深圳前海豆比金融服务有限公司",
#             "众网金融科技（上海）有限公司",
#             "爱康富罗纳金融信息服务（上海）有限公司",
#             "善林（上海）金融信息服务有限公司",
#             "城铁在融（武汉）互联网信息服务有限公司",
#             "上海律金金融信息服务有限公司",
#             "上海虎信金融信息服务有限公司",
#             "深圳市加力加实业发展有限公司",
#             "深圳前海中诚在线资本管理有限公司",
#             "深圳加点信息技术有限公司",
#             "深圳市汇旺宝投资有限公司",
#             "外快（深圳）科技信息有限公司",
#             "深圳市前海钱帮主互联网金融服务有限公司",
#             "深圳念念金融信息服务有限公司",
#             "深圳市互联行电子商务有限公司",
#             "深圳市汇龙电子商务有限公司",
#             "江苏广中投资管理有限公司",
#             "资邦元达（上海）互联网金融信息服务有限公司",
#             "中融金（北京）科技有限公司",
#             "浙江浙里互联网金融信息服务有限公司",
#             "浙江小泰科技有限公司",
#             "浙江草根网络科技有限公司",
#             "宜信惠民投资管理（北京）有限公司",
#             "天津国美互联网资产交易中心有限公司",
#             "深圳市雅堂金融服务股份有限公司",
#             "上海鱼耀金融信息服务有限公司",
#             "上海信而富企业管理有限公司",
#             "上海诺亚易捷网络科技有限公司",
#             "人人行科技股份有限公司",
#             "民加科风信息技术有限公司",
#             "恒大互联网金融服务（深圳）有限公司",
#             "北京玖富时代投资顾问有限公司",
#             "北京凤凰理理它信息技术有限公司",
#             "北京东方联合投资管理有限公司"
#     ]
# def update():
#     for i in ls_url:
#     update_sql = "UPDATE wdzj_website_2.WDZJ_PLAT_COMPANY_IC_DATA SET account_url='" + "" + i +\
#                  "' where account_id='" + i + "'"
#     cur.execute(update_sql)
#     conn.commit()


# 测试函数
def login(r, username, pwd):
    m = hashlib.md5()
    m.update(pwd)
    print m.hexdigest()
    # print r.post('https://www.tianyancha.com/cd/login.json?mobile=' + username + '&cdpassword=' + m.hexdigest() + '&loginway=PL&autoLogin=true').content
    print r.post('https://www.tianyancha.com/cd/login.json', data=json.dumps({'mobile': username, 'cdpassword': str(m.hexdigest()), 'loginway': 'PL', 'autoLogin': True})).content
    return r


if __name__ == "__main__":
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    conn_yuqing = connect_database(db_nick='wdzj_website_2')
    cur = conn_yuqing.cursor()
    conn_yuqing_21 = connect_database(db_nick='wdzj_website_21')
    cur_21 = conn_yuqing_21.cursor()
    conn_yuqing_be = connect_database(db_nick='yuqing')
    cur_be = conn_yuqing_be.cursor()
    r = requests.session()
    r.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0, WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        # "Cookie": get_cookie(),
        'Host': 'www.tianyancha.com',
        # 'Referer': 'https://www.tianyancha.com/',
        # 'X-Requested-With': 'XMLHttpRequest',
        # 'Host': 'www.tianyancha.com',
        'Connection': 'keep-alive',
        'Content-Length': '106',
        'Origin': 'https://www.tianyancha.com',
        'Content-Type': 'application/json; charset=UTF-8',  # x-www-form-urlencoded
        'Accept': '*/*',
        # 'Referer': 'https://www.tianyancha.com/login',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
    # r = login(r, '18616276129', 'wdzj2014')
    # r.headers.pop( "Accept")
    # r.headers.pop('Origin')
    # r.headers.pop('Content-Length')
    # r.headers.pop('Referer')
    # r.headers.pop('X-Requested-With')
    r.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0, WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        # "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'zh-CN,zh;q=0.8',
        # 'Connection': 'keep-alive',
        # 'Host': 'www.tianyancha.com',
        # 'Referer': 'https://www.tianyancha.com/',
        # 'Upgrade-Insecure-Requests': '1',
        "Cookie": get_cookie()
    }
    url = ""
    credit_code = ""
    # update_url(conn_yuqing_be, cur_be, r)
    # compare_url(conn_yuqing_be, cur_be, r)
    # urltoxianshang(conn_yuqing, cur, conn_yuqing_be, cur_be, conn_yuqing_21, cur_21)
    # delete_repeat(conn_yuqing, cur, conn_yuqing_be, cur_be, conn_yuqing_21, cur_21)
    # error_plat = get_info(conn_yuqing, cur, conn_yuqing_be, cur_be, r, conn_yuqing_21, cur_21, name_url).decode("utf-8")

    name_url = get_company_url(conn_yuqing)
    error_plat = u"上海诺诺镑客金融信息服务有限公司"  # 默认从第一条运行
    # error_plat = u"贵州国信通电子商务有限公司"
    nu = 0
    while len(error_plat):
        time.sleep(1)
        index = list(name_url.get('company_name')).index(error_plat)
        error_plat = get_info(conn_yuqing, cur, conn_yuqing_be, cur_be, r, conn_yuqing_21, cur_21, name_url, index).decode("utf-8")
        nu += 1
        if nu % 9 == 0:  # 重复请求10次无果后停止运行
            break
    cur_be.close()
    conn_yuqing_be.close()
    cur_21.close()
    conn_yuqing_21.close()
    cur.close()
    conn_yuqing.close()
    print "climb finish"
