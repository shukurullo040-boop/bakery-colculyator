import streamlit as st

# 1. ТИЛЛАР БАЗАСИ
LANGUAGES = {
    "O'zbekcha": {
        "title": "💰 Нонвойхона Молиявий Калкулятори (Кирим / Чиқим)",
        "currency_select": "Ҳисоб-китоб валютасини танланг:",
        "tab_expenses": "📉 Чиқимлар (Расходы)",
        "tab_revenues": "📈 Киримлар (Доходы)",
        "tab_report": "📊 Якуний Ҳисобот ва Фойда",
        "fixed_section": "🏢 Доимий ойлик харажатлар",
        "variable_section": "🌾 Кунлик хомашё харажатлари",
        "land_rent": "Бино / Ер учун ойлик ижара ҳақи",
        "salary": "Ишчиларнинг ойлик маоши",
        "utility": "Коммунал хизматлар (свет, газ, сув)",
        "flour_price": "1 кг уннинг нархи",
        "flour_qty": "Бир кунда ишлатиладиган ун ҳажми (кг)",
        "other_ingredients": "Бошқа кунлик маҳсулотлар (туз, хамиртуруш, ёғ)",
        "equipment_section": "⚙️ Улкуналар Савдоси (Бир марталик харажат)",
        "oven": "Печ ёки Тандир тури",
        "mixer": "Хамир қориш машинаси (Тестомес)",
        "shifter": "Ун элагич ускунаси",
        "production_section": "🍞 Ишлаб чиқариш ва Савдо",
        "bread_qty": "Бир кунда пишириладиган нон сони (шт)",
        "bread_price": "1 дона ноннинг сотилиш нархи",
        "report_fixed": "Доимий ойлик харажатлар (Ижара, Ойлик, Коммуналка)",
        "report_variable": "Ойлик хомашё харажатлари",
        "report_equip": "Ускуналарнинг умумий нархи (Инвестиция)",
        "report_total_revenue": "Умумий ойлик кирим (Выручка)",
        "report_total_expense": "Умумий ойлик чиқим (Расходы)",
        "report_net_profit": "🔥 Бир ойлик соф фойда",
        "cost_per_bread": "📐 1 дона ноннинг асл таннархи (Себестоимость)"
    },
    "Русский": {
        "title": "💰 Финансовый Калькулятор Пекарни (Кирим / Чиким)",
        "currency_select": "Выберите валюту расчета:",
        "tab_expenses": "📉 Расходы (Чиким)",
        "tab_revenues": "📈 Доходы (Кирим)",
        "tab_report": "📊 Итоговый Отчет и Прибыль",
        "fixed_section": "🏢 Фиксированные расходы в месяц",
        "variable_section": "🌾 Переменные расходы (Сырьё в день)",
        "land_rent": "Ежемесячная аренда помещения / земли",
        "salary": "Зарплата персонала (в месяц)",
        "utility": "Коммунальные услуги (свет, газ, вода)",
        "flour_price": "Цена 1 кг муки",
        "flour_qty": "Расход муки в день (кг)",
        "other_ingredients": "Другие ингредиенты в день (соль, дрожжи)",
        "equipment_section": "⚙️ Выбор Оборудования (Разовые расходы)",
        "oven": "Тип печи / тандыра",
        "mixer": "Тестомесильная машина",
        "shifter": "Мукопросеиватель",
        "production_section": "🍞 Production и Продажи",
        "bread_qty": "Количество выпекаемого хлеба в день (шт)",
        "bread_price": "Цена продажи 1 шт хлеба",
        "report_fixed": "Фиксированные расходы (Аренда, Зарплата, Коммуналка)",
        "report_variable": "Переменные расходы в месяц (Сырьё)",
        "report_equip": "Стоимость оборудования (Инвестиции)",
        "report_total_revenue": "Общая выручка в месяц",
        "report_total_expense": "Общие расходы в месяц",
        "report_net_profit": "🔥 Чистая прибыль в месяц",
        "cost_per_bread": "📐 Себестоимость 1 шт хлеба"
    }
}

# 2. РЕАЛ ВАЛЮТА КУРСЛАРИ БАЗАСИ (ДОЛЛАРГА НИСБАТАН КУРСЛАР)
EXCHANGE_RATES = {
    "UZS (сум)": 12800.0,
    "RUB (рубль)": 92.0,
    "TJS (сомони)": 10.6,
    "USD ($)": 1.0,
    "EUR (€)": 0.92
}

# Тепа панел: Тил ва Валюта танлови
col_lang, col_curr = st.columns(2)
with col_lang:
    sel_lang = st.selectbox("Language / Тил", list(LANGUAGES.keys()), index=0)
    lang = LANGUAGES[sel_lang]
with col_curr:
    sel_curr = st.selectbox(lang["currency_select"], list(EXCHANGE_RATES.keys()), index=0)
    rate = EXCHANGE_RATES[sel_curr]

curr_symbol = sel_curr.split(" ")[0]

# БАЗАВИЙ ҚИЙМАТЛАРНИ ТАНЛАНГАН ВАЛЮТАГА КУРС БЎЙИЧА ЎГИРИШ (АВТОМАТИК КОНВЕРТАЦИЯ)
def from_usd(usd_val):
    return float(usd_val * rate)

def fmt(val):
    return f"{val:,.2f} {curr_symbol}"

st.title(lang["title"])
st.write("---")

tab1, tab2, tab3 = st.tabs([lang["tab_expenses"], lang["tab_revenues"], lang["tab_report"]])

# --- 1-БЎЛИМ: ЧИҚИМЛАР (РАСХОДЫ) ---
with tab1:
    st.subheader(lang["fixed_section"])
    # Энди қийматлар валюта ўзгарганда курс бўйича автоматик равишда кичраяди ёки каттаради!
    rent = st.number_input(f"{lang['land_rent']} ({curr_symbol})", min_value=0.0, value=from_usd(400)) # $400 бошланғич
    salary = st.number_input(f"{lang['salary']} ({curr_symbol})", min_value=0.0, value=from_usd(800)) # $800 бошланғич
    utility = st.number_input(f"{lang['utility']} ({curr_symbol})", min_value=0.0, value=from_usd(150)) # $150 бошланғич
    
    st.subheader(lang["variable_section"])
    flour_price = st.number_input(f"{lang['flour_price']} ({curr_symbol} / 1 кг)", min_value=0.0, value=from_usd(0.5)) # $0.5 бошланғич
    flour_qty = st.number_input(lang["flour_qty"], min_value=0, value=150)
    other_ing = st.number_input(f"{lang['other_ingredients']} ({curr_symbol} / кунлик)", min_value=0.0, value=from_usd(12.0)) # $12 бошланғич

    st.subheader(lang["equipment_section"])
    oven_type = st.selectbox(lang["oven"], ["Traditional Tandoor", "Rotary Oven", "Deck Oven"])
    usd_oven_val = 900.0 if "Tandoor" in oven_type else (7500.0 if "Rotary" in oven_type else 4000.0)
    oven_cost = st.number_input(f"{oven_type} {lang['oven'].lower()} нархи ({curr_symbol})", min_value=0.0, value=from_usd(usd_oven_val))
    
    equip_cost = oven_cost
    if st.checkbox(lang["mixer"] + f" ({curr_symbol})", value=True):
        mixer_cost = st.number_input(f"{lang['mixer']} ({curr_symbol})", min_value=0.0, value=from_usd(1400.0))
        equip_cost += mixer_cost
    if st.checkbox(lang["shifter"] + f" ({curr_symbol})"):
        shifter_cost = st.number_input(f"{lang['shifter']} ({curr_symbol})", min_value=0.0, value=from_usd(700.0))
        equip_cost += shifter_cost

# --- 2-БЎЛИМ: КИРИМЛАР (ДОХОДЫ) ---
with tab2:
    st.subheader(lang["production_section"])
    bread_qty_daily = st.number_input(lang["bread_qty"], min_value=0, value=500)
    bread_price = st.number_input(f"{lang['bread_price']} ({curr_symbol})", min_value=0.0, value=from_usd(0.4), step=0.1)

# --- 3-БЎЛИМ: ЯКУНИЙ ҲИСОБОТ ЖАДВАЛИ ---
with tab3:
    monthly_fixed = rent + salary + utility
    daily_variable = (flour_price * flour_qty) + other_ing
    monthly_variable = daily_variable * 30
    total_monthly_expenses = monthly_fixed + monthly_variable
    
    total_monthly_revenue = (bread_qty_daily * bread_price) * 30
    net_monthly_profit = total_monthly_revenue - total_monthly_expenses
    
    total_daily_expense = daily_variable + (monthly_fixed / 30)
    cost_per_piece = total_daily_expense / bread_qty_daily if bread_qty_daily > 0 else 0

    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**{lang['report_fixed']}:**\n\n{fmt(monthly_fixed)}")
        st.info(f"**{lang['report_variable']}:**\n\n{fmt(monthly_variable)}")
        st.warning(f"**{lang['report_equip']}:**\n\n{fmt(equip_cost)}")
    with col2:
        st.success(f"**{lang['report_total_revenue']}:**\n\n{fmt(total_monthly_revenue)}")
        st.error(f"**{lang['report_total_expense']}:**\n\n{fmt(total_monthly_expenses)}")
        
        profit_color = "green" if net_monthly_profit >= 0 else "red"
        st.markdown(f"### <span style='color:{profit_color}'>{lang['report_net_profit']}: {fmt(net_monthly_profit)}</span>", unsafe_allow_html=True)

    st.write("---")
    st.metric(label=lang["cost_per_bread"], value=fmt(cost_per_piece))
