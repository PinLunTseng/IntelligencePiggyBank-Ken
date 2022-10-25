from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from django.db import connection


def home(request):
    return render(request, 'portfolio/index.html', locals())


def methodology(request):
    return render(request, 'portfolio/methodology.html', locals())


def about_us(request):
    return render(request, 'portfolio/about_us.html', locals())


def models(request):
    price = get_prices()
    weight_mv = get_weight_MV()
    amount_mv = {0: 1_000_000}
    allocate_mv = {}
    shares_mv = {}
    period = len(weight_mv)
    assets = len(weight_mv[0])
    for i in range(period):
        allocate_mv[i] = [0 for x in range(assets)]
        shares_mv[i] = [0 for x in range(assets)]

        if i != 0:
            amount_mv[i] = sum(price[i][j] * shares_mv[i - 1][j] for j in range(assets))

        for j in range(assets):
            allocate_mv[i][j] = amount_mv[i] * weight_mv[i][j]
            shares_mv[i][j] = allocate_mv[i][j] / price[i][j]

    periods = [date.strftime("%Y/%m/%d") for date in get_period_date()]

    # ROI
    roi_mv = {0: 0.0}
    for i in range(1, period):
        roi_mv[i] = (amount_mv[i] - amount_mv[0]) / amount_mv[0]

    # Annual Return
    amount_mv_response = ["{:.2f}".format(v) for k, v in amount_mv.items()]

    # pie chart
    latest_weight_mv_response = {asset: weight for weight, asset in zip(weight_mv[-1], get_assets())}
    latest_weight_mv_after_sorted = sorted(latest_weight_mv_response.items(), key=lambda x: x[1], reverse=True)
    top_10_assets_name = [x[0] for x in latest_weight_mv_after_sorted[:10]]
    top_10_assets_name.append('Others')
    top_10_assets_weight = [x[1]*100 for x in latest_weight_mv_after_sorted[:10]]
    top_10_assets_weight.append(sum([x[1]*100 for x in latest_weight_mv_after_sorted[10:]]))
    top_10_assets_weight_format = ["%.2f" % x for x in top_10_assets_weight]
    top_10_assets_weight_and_name = zip(top_10_assets_name, top_10_assets_weight_format)
    
    return render(request, 'portfolio/models.html', locals())


def create_assets():
    open_df = pd.read_excel("model_result/Omega.xlsx", sheet_name="weight").iloc[:, 1:]
    with connection.cursor() as cursor:
        for assets_name in open_df.columns:
            cursor.execute("insert into portfolio_assets (name) values (%s);", [assets_name])


def get_assets():
    with connection.cursor() as cursor:
        cursor.execute("SELECT name from portfolio_assets;")
        row = cursor.fetchall()
        assets = [x[0] for x in row]
        return assets


def create_index():
    open_df = pd.read_excel("model_result/Omega.xlsx", sheet_name="weight").iloc[:, :]
    with connection.cursor() as cursor:
        for i in open_df.iloc[:, 0]:
            cursor.execute("insert into portfolio_index ('index', period_id) values (%s, %s);", [i + 1, 20 * i + 1])


def create_period():
    open_df = pd.read_excel("model_result/result.xlsx", sheet_name="open").iloc[160:, :]
    with connection.cursor() as cursor:
        for i in open_df.loc[:2000, 'Date'].iloc[:]:
            cursor.execute("insert into portfolio_period (date) values (%s);", [str(i)])


def create_price():
    open_df = pd.read_excel("model_result/result.xlsx", sheet_name="open").iloc[160:, 2:]

    for i in range(93):
        for j in range(466):
            with connection.cursor() as cursor:
                open_df.iloc[20 * i, j]
                cursor.execute("insert into portfolio_price ('price', 'assets_id', 'index_id') values (%s, %s, %s);",
                               [open_df.iloc[20 * i, j], j + 1, i + 1])


def get_period_date():
    with connection.cursor() as cursor:
        cursor.execute("select portfolio_period.date from portfolio_index inner join portfolio_period on portfolio_index.period_id=portfolio_period.id;")
        row = cursor.fetchall()
        period_date = [date[0] for date in row]
        return period_date


def get_prices():
    with connection.cursor() as cursor:
        price_list = []
        for i in range(93):
            cursor.execute("select price from portfolio_price where index_id=%s;", [i + 1])
            row = cursor.fetchall()
            price_list.append([x[0] for x in row])
        return price_list


def get_weight_MV():
    with connection.cursor() as cursor:
        weight_list = []
        for i in range(93):
            cursor.execute("select weight from portfolio_weightmv where index_id=%s;", [i + 1])
            row = cursor.fetchall()
            weight_list.append([x[0] for x in row])
        return weight_list


def get_weight_CVaR():
    with connection.cursor() as cursor:
        weight_list = []
        for i in range(93):
            cursor.execute("select weight from portfolio_weightcvar where index_id=%s;", [i + 1])
            row = cursor.fetchall()
            weight_list.append([x[0] for x in row])
        return weight_list


def get_weight_Omega():
    with connection.cursor() as cursor:
        weight_list = []
        for i in range(93):
            cursor.execute("select weight from portfolio_weightwomega where index_id=%s;", [i + 1])
            row = cursor.fetchall()
            weight_list.append([x[0] for x in row])
        return weight_list


def create_MV_weight():

    open_df = pd.read_excel("model_result/MV.xlsx", sheet_name="weight").iloc[:, 1:]
    for i in range(93):
        for j in range(466):
            with connection.cursor() as cursor:
                cursor.execute("insert into portfolio_weightmv ('weight', 'assets_id', 'index_id') values (%s, %s, %s);",
                               [float(open_df.iloc[i, j]), j + 1, i + 1])


def create_CVaR_weight():
    open_df = pd.read_excel("model_result/CVaR.xlsx", sheet_name="weight").iloc[:, 1:]
    for i in range(93):
        for j in range(466):
            with connection.cursor() as cursor:
                cursor.execute(
                    "insert into portfolio_weightcvar ('weight', 'assets_id', 'index_id') values (%s, %s, %s);",
                    [float(open_df.iloc[i, j]), j + 1, i + 1])


def create_WOmega_weight():
    open_df = pd.read_excel("model_result/Omega.xlsx", sheet_name="weight").iloc[:, 1:]
    for i in range(93):
        for j in range(466):
            with connection.cursor() as cursor:
                cursor.execute(
                    "insert into portfolio_weightwomega ('weight', 'assets_id', 'index_id') values (%s, %s, %s);",
                    [float(open_df.iloc[i, j]), j + 1, i + 1])


def init_db(request):
    create_assets()
    create_period()
    create_index()
    create_price()
    create_MV_weight()
    create_CVaR_weight()
    create_WOmega_weight()
    return HttpResponse('Complete create all data.')
