def fy_statements(ticker, analysis_period, analysis_end):
    api_key= "(YOUR SIMFIN API KEY)"
    request_url= "https://simfin.com/api/v2/companies/statements"

    latest_year= {"l_year": analysis_end}

    columns= []
    output= []
    financial_year= latest_year["l_year"]

    i= 0
    while analysis_period> i:
        parameters= {"statement": "pl", "ticker": ticker, "period": "fy", "fyear": financial_year, "api-key": api_key}
        request = requests.get(request_url, parameters)
        all_data= request.json()
        for response_index, data in enumerate(all_data):
            if data['found'] and len(data['data']) > 0:
                if len(columns) == 0:
                    columns = data['columns']
                output += data['data']
        df_pl= pd.DataFrame(output, columns=columns)
    
        i= i+1  
        financial_year= financial_year-1

    df_pl.drop(["SimFinId","Ticker", "Fiscal Period", "Report Date", "Publish Date","Restated Date", "Net Income (Common)", "Source","TTM","Value Check"], axis=1, inplace=True)

    df_pl.dropna(axis= "columns", how="all", inplace= True)
  
    df_pl.fillna(0, inplace= True)
 

    df_pl.iloc[:, 1:]= df_pl.iloc[:, 1:].div(1000000)
 

    df_pl.insert(0, "Income Statement", "")
    df_pl.insert(len(df_pl.columns), " ", " ")


    columns= []
    output= []
    financial_year= latest_year["l_year"]

    i= 0
    while analysis_period> i:
        parameters= {"statement": "bs", "ticker": ticker, "period": "fy", "fyear": financial_year, "api-key": api_key}
        request = requests.get(request_url, parameters)
        all_data= request.json()
        for response_index, data in enumerate(all_data):
            if data['found'] and len(data['data']) > 0:
                if len(columns) == 0:
                    columns = data['columns']
                output += data['data']
        df_bs= pd.DataFrame(output, columns=columns)
    
        i= i+1
        financial_year= financial_year-1
    
    df_bs.drop(["Ticker", "Fiscal Year", "Fiscal Period", "Report Date", "SimFinId","Publish Date","Restated Date","Cash, Cash Equivalents & Short Term Investments", "Payables & Accruals", "Source","TTM","Value Check"], axis=1, inplace=True)

    df_bs.dropna(axis= "columns", how="all", inplace= True)
   
    df_bs.fillna(0, inplace= True)
   

    df_bs.iloc[:, 0:]= df_bs.iloc[:, 0:].div(1000000)
    
    df_bs.insert(0, "Balance Sheet", "")
    df_bs.insert(len(df_bs.columns), " ", " ")


    columns= []
    output= []
    financial_year= latest_year["l_year"]

    i= 0
    while analysis_period> i:
        parameters= {"statement": "cf", "ticker": ticker, "period": "fy", "fyear": financial_year, "api-key": api_key}
        request = requests.get(request_url, parameters)
        all_data= request.json()
        for response_index, data in enumerate(all_data):
            if data['found'] and len(data['data']) > 0:
                if len(columns) == 0:
                    columns = data['columns']
                output += data['data']
        df_cf= pd.DataFrame(output, columns=columns)
    
        i= i+1  
        financial_year= financial_year-1

    df_cf.drop(["Ticker", "Fiscal Year", "Fiscal Period", "Report Date","SimFinId","Publish Date","Restated Date","Net Income", "Source","TTM","Value Check"], axis=1, inplace=True)

    df_cf.dropna(axis= "columns", how="all", inplace= True)
   
    df_cf.fillna(0, inplace= True)
    

    df_cf.iloc[:, 0:]= df_cf.iloc[:, 0:].div(1000000)
  

    df_cf.insert(0, "Cash Flow Statement", "")


    df_pl= pd.DataFrame.transpose(df_pl)
    df_bs= pd.DataFrame.transpose(df_bs)
    df_cf= pd.DataFrame.transpose(df_cf)

    statement= pd.concat([df_pl, df_bs, df_cf], join= "inner", ignore_index= False, copy= True)
    statement.columns= statement.iloc[1]
    statement= statement.drop(index= "Fiscal Year")
    statement= statement.rename_axis("(in million USD)")
    
    return statement

def fy_income(ticker, analysis_period, analysis_end):
    api_key= "(YOUR SIMFIN API KEY)"
    request_url= "https://simfin.com/api/v2/companies/statements"

    latest_year= {"l_year": analysis_end}

    columns= []
    output= []
    financial_year= latest_year["l_year"]

    i= 0
    while analysis_period> i:
        parameters= {"statement": "pl", "ticker": ticker, "period": "fy", "fyear": financial_year, "api-key": api_key}
        request = requests.get(request_url, parameters)
        all_data= request.json()
        for response_index, data in enumerate(all_data):
            if data['found'] and len(data['data']) > 0:
                if len(columns) == 0:
                    columns = data['columns']
                output += data['data']
        df_pl= pd.DataFrame(output, columns=columns)
    
        i= i+1  
        financial_year= financial_year-1

    df_pl.drop(["SimFinId","Ticker", "Fiscal Period", "Report Date", "Publish Date","Restated Date", "Net Income (Common)", "Source","TTM","Value Check"], axis=1, inplace=True)

    df_pl.dropna(axis= "columns", how="all", inplace= True)
  
    df_pl.fillna(0, inplace= True)
 

    df_pl.iloc[:, 1:]= df_pl.iloc[:, 1:].div(1000000)
 

    df_pl.insert(0, "Income Statement (in million USD)", "")
    df_pl= df_pl.T
    df_pl.columns= df_pl.iloc[1]
    df_pl= df_pl.drop(index= "Fiscal Year")
    
    return df_pl



def fy_bs(ticker, analysis_period, analysis_end):
    api_key= "(YOUR SIMFIN API KEY)"
    request_url= "https://simfin.com/api/v2/companies/statements"

    latest_year= {"l_year": analysis_end}

    columns= []
    output= []
    financial_year= latest_year["l_year"]

    i= 0
    while analysis_period> i:
        parameters= {"statement": "bs", "ticker": ticker, "period": "fy", "fyear": financial_year, "api-key": api_key}
        request = requests.get(request_url, parameters)
        all_data= request.json()
        for response_index, data in enumerate(all_data):
            if data['found'] and len(data['data']) > 0:
                if len(columns) == 0:
                    columns = data['columns']
                output += data['data']
        df_bs= pd.DataFrame(output, columns=columns)
    
        i= i+1  
        financial_year= financial_year-1

    df_bs.drop(["SimFinId","Ticker", "Fiscal Period", "Report Date", "Publish Date","Restated Date","Cash, Cash Equivalents & Short Term Investments", "Payables & Accruals", "Source","TTM","Value Check"], axis=1, inplace=True)

    df_bs.dropna(axis= "columns", how="all", inplace= True)
  
    df_bs.fillna(0, inplace= True)
 

    df_bs.iloc[:, 1:]= df_bs.iloc[:, 1:].div(1000000)
 

    df_bs.insert(0, "Balance Sheet (in million USD)", "")
    df_bs= df_bs.T
    df_bs.columns= df_bs.iloc[1]
    df_bs= df_bs.drop(index= "Fiscal Year")
    
    return df_bs



def fy_cf(ticker, analysis_period, analysis_end):
    api_key= "(YOUR SIMFIN API KEY)"
    request_url= "https://simfin.com/api/v2/companies/statements"

    latest_year= {"l_year": analysis_end}

    columns= []
    output= []
    financial_year= latest_year["l_year"]

    i= 0
    while analysis_period> i:
        parameters= {"statement": "cf", "ticker": ticker, "period": "fy", "fyear": financial_year, "api-key": api_key}
        request = requests.get(request_url, parameters)
        all_data= request.json()
        for response_index, data in enumerate(all_data):
            if data['found'] and len(data['data']) > 0:
                if len(columns) == 0:
                    columns = data['columns']
                output += data['data']
        df_cf= pd.DataFrame(output, columns=columns)
    
        i= i+1  
        financial_year= financial_year-1

    df_cf.drop(["SimFinId","Ticker", "Fiscal Period", "Report Date", "Publish Date","Restated Date","Source","TTM","Value Check"], axis=1, inplace=True)

    df_cf.dropna(axis= "columns", how="all", inplace= True)
  
    df_cf.fillna(0, inplace= True)
 

    df_cf.iloc[:, 1:]= df_cf.iloc[:, 1:].div(1000000)
 

    df_cf.insert(0, "Cash Flow Statement (in million USD)", "")
    df_cf= df_cf.T
    df_cf.columns= df_cf.iloc[1]
    df_cf= df_cf.drop(index= "Fiscal Year")
    
    return df_cf


def plot_currentassets(balance_sheet):
      
    currentassets= ['Cash & Cash Equivalents',
 'Short Term Investments',
 'Accounts Receivable, Net',
 'Inventories',
 'Other Short Term Assets',
 'Prepaid Expenses',
 'Deferred Tax Assets (Short Term)']
    
    current_assets= balance_sheet.T.filter(currentassets)
    
    return current_assets.plot()
    
def common_size(income_statement, balance_sheet):
    c_pl= income_statement.loc["Revenue":"Net Income"]/ income_statement.loc["Revenue"]
    
    c_assets= balance_sheet.loc["Cash & Cash Equivalents":"Total Assets"]/ balance_sheet.loc["Total Assets"]
    c_le= balance_sheet.loc["Accounts Payable":"Total Liabilities & Equity"]/ balance_sheet.loc["Total Liabilities & Equity"]    
    c_bs= pd.concat([c_assets, c_le])
    
    combined= pd.concat([c_pl, c_bs])
    average= pd.DataFrame({"Avg": combined.mean(1)})
    commonsize_statements= combined.join(average)
    
    return commonsize_statements

    
def roe(fy_statements):
    hist_se= fy_statements.loc["Total Equity"]
    calc_years= fy_statements.drop(fy_statements.columns[-1], axis=1)
    
    
    data= pd.DataFrame([])
    
    x,y = 0,2
    while len(hist_se) > x+1:
        mean_se= pd.DataFrame(hist_se.iloc[x:y]).mean()
        
        mean_se= pd.DataFrame(mean_se)
        
        data= data.append(mean_se)
        
        x,y= x+1, y+1
    
    else:
        avg_se= data.T
        avg_se.columns= calc_years.columns.values
        
        hist_roe= calc_years.loc["Net Income"]/avg_se
        mean= hist_roe.mean(axis= 1)
        
        avg_roe= {"Avg Shareholders' Equity": mean}
        avg_roe= pd.DataFrame(avg_roe)
        avg_roe= pd.concat([avg_roe, hist_roe], axis=1)
        
    return avg_roe


def rev_growth(fy_statements):
    growth= fy_statements.loc["Revenue"].pct_change(-1).dropna()
    #reverse pct_change direction
    mean= growth.mean()
    growth= pd.DataFrame(growth).T
    
    growth.insert(0, "Avg", mean)
    avg_growth= growth.rename(index={"Revenue": "Revenue Growth Rate"})
    
    return avg_growth


def asset_turnover(fy_statements):
    hist_ta= fy_statements.loc["Total Assets"]
    calc_years= fy_statements.drop(fy_statements.columns[-1], axis=1)
    
    
    data= pd.DataFrame([])
    
    x,y = 0,2
    while len(hist_ta) > x+1:
        mean_ta= pd.DataFrame(hist_ta.iloc[x:y]).mean()
        
        mean_ta= pd.DataFrame(mean_ta)
        
        data= data.append(mean_ta)
        
        x,y= x+1, y+1
    
    else:
        avg_ta= data.T
        avg_ta.columns= calc_years.columns.values
        
        hist_turnover= calc_years.loc["Revenue"]/avg_ta
        mean= hist_turnover.mean(axis= 1)
        
        avg_turnover= {"Avg": mean}
        avg_turnover= pd.DataFrame(avg_turnover)
        avg_turnover= pd.concat([avg_turnover, hist_turnover], axis=1)
        avg_turnover= avg_turnover.rename(index={0: "Asset Turnover Rate"})
        
    return avg_turnover

def shares_outstanding(ticker):
    api_key= "(YOUR SIMFIN API KEY)"
    request_url= "https://simfin.com/api/v2/companies/shares"

    date= datetime.datetime.now()
    year= now.year

    columns= []
    output= []

    parameters= {"type": "common", "ticker": ticker, "period": "fy", "fyear": year, "api-key": api_key}
    request = requests.get(request_url, parameters)
    all_data= request.json()
    for response_index, data in enumerate(all_data):
        if data['found'] and len(data['data']) > 0:
            if len(columns) == 0:
                columns = data['columns']
            output += data['data']
    common_shares_outstanding = pd.DataFrame(output, columns=columns)
    latest_shares_outstanding= pd.DataFrame(common_shares_outstanding.iloc[[-1]])
    
    return latest_shares_outstanding


def interest_expense(ticker, fy_statements):
    request_url = "https://api.unibit.ai/v2/company/coreFinancials/?"
    start_date= str(fy_statements.columns[-1])+"-01-01"
    end_date= str(fy_statements.columns[0])+"-12-31"
    unibit_key= "(YOUR UNIBIT API KEY)"
    parameters= {"tickers": ticker, "interval": "A", "statement": "IS", "startDate": start_date, "endDate": end_date, "selectedFields": "interest_expense,report_date", "dataType": "csv", "accessKey": unibit_key}

    request = requests.get(request_url, parameters)

    data= io.StringIO(request.text)
    csv= pd.read_csv(data, sep=",")

    interest_expense= csv.sort_values(by= "report date", ascending= False)
    interest_expense= interest_expense.T
    interest_expense.iloc[1]= interest_expense.iloc[1].div(1000000)
    interest_expense.columns= interest_expense.iloc[2]
    interest_expense= interest_expense.drop(["ticker", "report date"])
    interest_expense= interest_expense.rename_axis(ticker+"(in million USD)")
    return interest_expense

def gross_ppe(ticker, fy_statements):
    request_url = "https://api.unibit.ai/v2/company/coreFinancials/?"
    start_date= str(fy_statements.columns[-1])+"-01-01"
    end_date= str(fy_statements.columns[0])+"-12-31"
    unibit_key= "(YOUR UNIBIT API KEY)"
    parameters= {"tickers": ticker, "interval": "A", "statement": "BS", "startDate": start_date, "endDate": end_date, "selectedFields": "gross_ppe,report_date", "dataType": "csv", "accessKey": unibit_key}

    request = requests.get(request_url, parameters)

    data= io.StringIO(request.text)
    csv= pd.read_csv(data, sep=",")

    gross_ppe= csv.sort_values(by= "report date", ascending= False)
    gross_ppe= gross_ppe.T
    gross_ppe.iloc[1]= gross_ppe.iloc[1].div(1000000)
    gross_ppe.columns= gross_ppe.iloc[2]
    gross_ppe= gross_ppe.drop(["ticker", "report date"])
    gross_ppe= gross_ppe.rename_axis(ticker+ "(in million USD)")
    return gross_ppe

def accumulated_dep(ticker, fy_statements):
    request_url = "https://api.unibit.ai/v2/company/coreFinancials/?"
    start_date= str(fy_statements.columns[-1])+"-01-01"
    end_date= str(fy_statements.columns[0])+"-12-31"
    unibit_key= "(YOUR UNIBIT API KEY)"
    parameters= {"tickers": ticker, "interval": "A", "statement": "BS", "startDate": start_date, "endDate": end_date, "selectedFields": "gross_ppe,report_date", "dataType": "csv", "accessKey": unibit_key}

    request = requests.get(request_url, parameters)

    data= io.StringIO(request.text)
    csv= pd.read_csv(data, sep=",")

    gross_ppe= csv.sort_values(by= "report date", ascending= False)
    gross_ppe= gross_ppe.T
    gross_ppe.iloc[1]= gross_ppe.iloc[1].div(1000000)
    gross_ppe.columns= gross_ppe.iloc[2]
    gross_ppe= gross_ppe.drop(["ticker", "report date"])
    gross_ppe= gross_ppe.rename_axis(ticker+ "(in million USD)")
    
    net_ppe= pd.DataFrame(INTC.loc["Property, Plant & Equipment, Net"])
    net_ppe= net_ppe.iloc[0:len(gross_ppe.T)].T
    net_ppe= net_ppe.rename(index= {"Property, Plant & Equipment, Net": "Accumulated Depreciation"})
    
    gross_ppe.columns=net_ppe.columns.values
    gross_ppe= gross_ppe.rename(index= {"gross ppe": "Accumulated Depreciation"})
    
    accumulated_dep= gross_ppe-net_ppe
    
    return accumulated_dep


def cs_ad(ticker, fy_statements):
    request_url = "https://api.unibit.ai/v2/company/coreFinancials/?"
    start_date= str(fy_statements.columns[-1])+"-01-01"
    end_date= str(fy_statements.columns[0])+"-12-31"
    unibit_key= "(YOUR UNIBIT API KEY)"
    parameters= {"tickers": ticker, "interval": "A", "statement": "BS", "startDate": start_date, "endDate": end_date, "selectedFields": "gross_ppe,report_date", "dataType": "csv", "accessKey": unibit_key}

    request = requests.get(request_url, parameters)

    data= io.StringIO(request.text)
    csv= pd.read_csv(data, sep=",")

    gross_ppe= csv.sort_values(by= "report date", ascending= False)
    gross_ppe= gross_ppe.T
    gross_ppe.iloc[1]= gross_ppe.iloc[1].div(1000000)
    gross_ppe.columns= gross_ppe.iloc[2]
    gross_ppe= gross_ppe.drop(["ticker", "report date"])
    gross_ppe= gross_ppe.rename_axis(ticker)
    
    net_ppe= pd.DataFrame(INTC.loc["Property, Plant & Equipment, Net"])
    net_ppe= net_ppe.iloc[0:len(gross_ppe.T)].T
    net_ppe= net_ppe.rename(index= {"Property, Plant & Equipment, Net": "Accumulated Depreciation"})
    
    gross_ppe.columns=net_ppe.columns.values
    gross_ppe= gross_ppe.rename(index= {"gross ppe": "Accumulated Depreciation"})
    
    accumulated_dep= gross_ppe-net_ppe
    
    total_assets= fy_statements.loc["Total Assets"]
    total_assets= pd.DataFrame(total_assets)
    total_assets= total_assets.iloc[0:len(accumulated_dep.T)].T
    total_assets= total_assets.rename(index= {"Total Assets": "CS Accumulated Depreciation"})
    
    accumulated_dep= accumulated_dep.rename(index= {"Accumulated Depreciation": "CS Accumulated Depreciation"})
    cs_ad= accumulated_dep/total_assets
    mean= cs_ad.loc["CS Accumulated Depreciation"].mean()
    
    avg_ad= {"Avg": mean}
    avg_ad= pd.DataFrame(avg_ad, index= ["CS Accumulated Depreciation"])
    cs_ad= pd.concat([avg_ad, cs_ad], axis=1)
    
    
    return cs_ad
    

def weighted_avg_dep(ticker, fy_statements, fy_income):
    
    request_url = "https://api.unibit.ai/v2/company/coreFinancials/?"
    start_date= str(fy_statements.columns[-1])+"-01-01"
    end_date= str(fy_statements.columns[0])+"-12-31"
    unibit_key= "(YOUR UNIBIT API KEY)"
    parameters= {"tickers": ticker, "interval": "A", "statement": "BS", "startDate": start_date, "endDate": end_date, "selectedFields": "gross_ppe,report_date", "dataType": "csv", "accessKey": unibit_key}

    request = requests.get(request_url, parameters)

    data= io.StringIO(request.text)
    csv= pd.read_csv(data, sep=",")

    gross_ppe= csv.sort_values(by= "report date", ascending= False)
    gross_ppe= gross_ppe.T
    gross_ppe.iloc[1]= gross_ppe.iloc[1].div(1000000)
    gross_ppe.columns= gross_ppe.iloc[2]
    gross_ppe= gross_ppe.drop(["ticker", "report date"])
    gross_ppe= gross_ppe.rename_axis(ticker+ "(in million USD)")

    gross_ppe= gross_ppe.T
    
    years= len(gross_ppe)
    years_label= pd.DataFrame(fy_statements.columns[0:years-1]).T
    years_label.columns= years_label.iloc[0]
    
    a,b = 0,2
    gppe_data= pd.DataFrame([])
    
    while years > a+1:
        mean_gppe= gross_ppe.iloc[a:b].mean()
        mean_gppe= pd.DataFrame(mean_gppe)
        gppe_data= gppe_data.append(mean_gppe)
    
        a,b= a+1, b+1
    
    
    hist_ia= fy_statements.loc["Intangible Assets"]
    
    ia_data= pd.DataFrame([])
    
    x,y = 0,2
    while years > x+1:
        mean_ia= pd.DataFrame(hist_ia.iloc[x:y]).mean()
        mean_ia= pd.DataFrame(mean_ia)
        ia_data= ia_data.append(mean_ia)
        
        x,y= x+1, y+1
    
    else:
        gppe_data= gppe_data.rename(index={"gross ppe": "GPPE & IA"})
        ia_data= ia_data.rename(index={"Intangible Assets": "GPPE & IA"})
        denominator= gppe_data.add(ia_data, fill_value= 0)
        denominator= denominator.T
        denominator.columns= years_label.columns.values
        denominator= denominator.rename(index= {0: "GPPE & IA"})
        
        fy_income= fy_income.T.iloc[0:years-1]
        d_a= pd.DataFrame(fy_income.T.loc["Depreciation & Amortization"]).T
        hist_dep= abs(d_a/denominator.loc["GPPE & IA"])
        mean= hist_dep.mean(axis= 1)
        
        avg_dep= {"Avg": mean}
        avg_dep= pd.DataFrame(avg_dep)
        avg_dep= pd.concat([avg_dep, hist_dep], axis=1)
        avg_dep= avg_dep.rename(index= {"Depreciation & Amortization": "Weighted Depreciation Rate"})
        
        return avg_dep
    

def weighted_avg_ir(ticker, fy_statements):
    
    request_url = "https://api.unibit.ai/v2/company/coreFinancials/?"
    start_date= str(fy_statements.columns[-1])+"-01-01"
    end_date= str(fy_statements.columns[0])+"-12-31"
    unibit_key= "(YOUR UNIBIT API KEY)"
    parameters= {"tickers": ticker, "interval": "A", "statement": "IS", "startDate": start_date, "endDate": end_date, "selectedFields": "interest_expense,report_date", "dataType": "csv", "accessKey": unibit_key}

    request = requests.get(request_url, parameters)

    data= io.StringIO(request.text)
    csv= pd.read_csv(data, sep=",")

    interest_expense= csv.sort_values(by= "report date", ascending= False)
    interest_expense= interest_expense.T
    interest_expense.iloc[1]= interest_expense.iloc[1].div(1000000)
    interest_expense.columns= interest_expense.iloc[2]
    interest_expense= interest_expense.drop(["ticker", "report date"])
    interest_expense= interest_expense.rename_axis(ticker)

    interest_expense= interest_expense.T
    
    years= len(interest_expense)
    years_label= pd.DataFrame(fy_statements.columns[0:years]).T
    years_label.columns= years_label.iloc[0]
    
    
    hist_ltdebt= fy_statements.loc["Long Term Debt"]
    
    ltdebt_data= pd.DataFrame([])
    
    x,y = 0,2
    while years > x:
        mean_ltdebt= pd.DataFrame(hist_ltdebt.iloc[x:y]).mean()
        mean_ltdebt= pd.DataFrame(mean_ltdebt)
        ltdebt_data= ltdebt_data.append(mean_ltdebt)
        
        x,y= x+1, y+1
    
    else:
        interest_expense= interest_expense.T.rename(index= {"interest expense": "Weighted Avg IR"})
        interest_expense.columns= years_label.columns.values
        
        ltdebt_data= ltdebt_data.T.rename(index= {0: "Weighted Avg IR"})
        ltdebt_data.columns= years_label.columns.values
        
        hist_ir= abs(interest_expense/ltdebt_data)
        mean= hist_ir.mean(axis= 1)
        
        avg_ir= {"Avg": mean}
        avg_ir= pd.DataFrame(avg_ir)
        avg_ir= pd.concat([avg_ir, hist_ir], axis=1)
        
        return avg_ir


def avg_assumptions(ticker, fy_statements, fy_income): 
    
    request_url = "https://api.unibit.ai/v2/company/coreFinancials/?"
    start_date= str(fy_statements.columns[-1])+"-01-01"
    end_date= str(fy_statements.columns[0])+"-12-31"
    unibit_key= "(YOUR UNIBIT API KEY)"
    
    #avg_ir:
    parameters= {"tickers": ticker, "interval": "A", "statement": "IS", "startDate": start_date, "endDate": end_date, "selectedFields": "interest_expense,report_date", "dataType": "csv", "accessKey": unibit_key}

    request = requests.get(request_url, parameters)

    data= io.StringIO(request.text)
    csv= pd.read_csv(data, sep=",")

    interest_expense= csv.sort_values(by= "report date", ascending= False)
    interest_expense= interest_expense.T
    interest_expense.iloc[1]= interest_expense.iloc[1].div(1000000)
    interest_expense.columns= interest_expense.iloc[2]
    interest_expense= interest_expense.drop(["ticker", "report date"])
    interest_expense= interest_expense.rename_axis(ticker)

    interest_expense= interest_expense.T
    
    years= len(interest_expense)
    years_label= pd.DataFrame(fy_statements.columns[0:years]).T
    years_label.columns= years_label.iloc[0]
    
    
    hist_ltdebt= fy_statements.loc["Long Term Debt"]
    
    ltdebt_data= pd.DataFrame([])
    
    x,y = 0,2
    while years > x:
        mean_ltdebt= pd.DataFrame(hist_ltdebt.iloc[x:y]).mean()
        mean_ltdebt= pd.DataFrame(mean_ltdebt)
        ltdebt_data= ltdebt_data.append(mean_ltdebt)
        
        x,y= x+1, y+1
    
    else:
        interest_expense= interest_expense.T.rename(index= {"interest expense": "Weighted Avg IR"})
        interest_expense.columns= years_label.columns.values
        
        ltdebt_data= ltdebt_data.T.rename(index= {0: "Weighted Avg IR"})
        ltdebt_data.columns= years_label.columns.values
        
        hist_ir= abs(interest_expense/ltdebt_data)
        mean= hist_ir.mean(axis= 1)
        
        avg_ir= {"Avg": mean}
        avg_ir= pd.DataFrame(avg_ir)
        avg_ir= pd.concat([avg_ir, hist_ir], axis=1)

    
    parameters= {"tickers": ticker, "interval": "A", "statement": "BS", "startDate": start_date, "endDate": end_date, "selectedFields": "gross_ppe,report_date", "dataType": "csv", "accessKey": unibit_key}

    request = requests.get(request_url, parameters)

    data= io.StringIO(request.text)
    csv= pd.read_csv(data, sep=",")

    gross_ppe= csv.sort_values(by= "report date", ascending= False)
    gross_ppe= gross_ppe.T
    gross_ppe.iloc[1]= gross_ppe.iloc[1].div(1000000)
    gross_ppe.columns= gross_ppe.iloc[2]
    gross_ppe= gross_ppe.drop(["ticker", "report date"])
    gross_ppe= gross_ppe.rename_axis(ticker+ "(in million USD)")

    gross_ppe= gross_ppe.T
    
    years= len(gross_ppe)
    years_label= pd.DataFrame(fy_statements.columns[0:years-1]).T
    years_label.columns= years_label.iloc[0]
    
    a,b = 0,2
    gppe_data= pd.DataFrame([])
    
    while years > a+1:
        mean_gppe= gross_ppe.iloc[a:b].mean()
        mean_gppe= pd.DataFrame(mean_gppe)
        gppe_data= gppe_data.append(mean_gppe)
    
        a,b= a+1, b+1
    
    
    hist_ia= fy_statements.loc["Intangible Assets"]
    
    ia_data= pd.DataFrame([])
    
    x,y = 0,2
    while years > x+1:
        mean_ia= pd.DataFrame(hist_ia.iloc[x:y]).mean()
        mean_ia= pd.DataFrame(mean_ia)
        ia_data= ia_data.append(mean_ia)
        
        x,y= x+1, y+1
    
    else:
        gppe_data= gppe_data.rename(index={"gross ppe": "GPPE & IA"})
        ia_data= ia_data.rename(index={"Intangible Assets": "GPPE & IA"})
        denominator= gppe_data.add(ia_data, fill_value= 0)
        denominator= denominator.T
        denominator.columns= years_label.columns.values
        denominator= denominator.rename(index= {0: "GPPE & IA"})
        
        fy_income= fy_income.T.iloc[0:years-1]
        d_a= pd.DataFrame(fy_income.T.loc["Depreciation & Amortization"]).T
        hist_dep= abs(d_a/denominator.loc["GPPE & IA"])
        mean= hist_dep.mean(axis= 1)
        
        avg_dep= {"Avg": mean}
        avg_dep= pd.DataFrame(avg_dep)
        avg_dep= pd.concat([avg_dep, hist_dep], axis=1)
        avg_dep= avg_dep.rename(index= {"Depreciation & Amortization": "Weighted Depreciation Rate"})
        
    
    hist_ta= fy_statements.loc["Total Assets"]
    calc_years= fy_statements.drop(fy_statements.columns[-1], axis=1)
    
    
    data= pd.DataFrame([])
    
    x,y = 0,2
    while len(hist_ta) > x+1:
        mean_ta= pd.DataFrame(hist_ta.iloc[x:y]).mean()
        
        mean_ta= pd.DataFrame(mean_ta)
        
        data= data.append(mean_ta)
        
        x,y= x+1, y+1
    
    else:
        avg_ta= data.T
        avg_ta.columns= calc_years.columns.values
        
        hist_turnover= calc_years.loc["Revenue"]/avg_ta
        mean= hist_turnover.mean(axis= 1)
        
        avg_turnover= {"Avg": mean}
        avg_turnover= pd.DataFrame(avg_turnover)
        avg_turnover= pd.concat([avg_turnover, hist_turnover], axis=1)
        avg_turnover= avg_turnover.rename(index={0: "Asset Turnover Rate"})
        
   
    growth= fy_statements.loc["Revenue"].pct_change(-1).dropna()
    
    mean= growth.mean()
    growth= pd.DataFrame(growth).T
    
    growth.insert(0, "Avg", mean)
    avg_growth= growth.rename(index={"Revenue": "Revenue Growth Rate"})
    
    
    avg_assumptions= avg_growth["Avg"].append([avg_turnover["Avg"], avg_ir["Avg"], avg_dep["Avg"]])
    avg_assumptions= pd.DataFrame(avg_assumptions)
    
    return avg_assumptions
    

def assumptions(common_size, avg_assumptions):
    common_size= pd.DataFrame(common_size["Avg"]).loc["Cost of Revenue": "Total Liabilities"]
    assumptions= common_size.drop(["Total Assets", "Depreciation & Amortization"])
    assumptions= pd.concat([avg_assumptions, assumptions])
    assumptions= assumptions.rename(columns= {"Avg": "Assumed Values"})
    
    #assumptions.reset_index().rename(columns={"index": "Items"})
    
    return assumptions


#returns empty statements with only pro_forma revenue
def pro_forma(ticker, fy_statements, assumptions):
    latest_year= fy_statements.columns[0]
    column_labels= []
    for i in list(range(1, 11)):
        column= column_labels.append(latest_year+i)

    pro_forma= pd.DataFrame(index= fy_statements.index, columns= column_labels)
    pro_forma= pro_forma.rename_axis(ticker+ " (in million USD)")
    
    
    fy_statements= fy_statements.sort_values(by= "Fiscal Year", axis= 1)
    fy_statements= fy_statements.rename_axis(ticker+ " (in million USD)")
    
    latest_rev= fy_statements.loc["Revenue", fy_statements.columns.values[len(fy_statements.columns)-1]]
    growth_rate= 1+ assumptions.loc["Revenue Growth Rate"].values[0]
    y1_pf_rev= latest_rev*growth_rate
    pro_forma.loc["Revenue", pro_forma.columns.values[0]]= y1_pf_rev
    
    i= 1  
    while i < 10:
        pro_forma.loc["Revenue", pro_forma.columns.values[i]]= pro_forma.loc["Revenue", pro_forma.columns.values[i-1]]*growth_rate
        i= i+1
    
    income_assumptions= assumptions["Cost of Revenue":"Net Income"]
    revenue= pd.DataFrame(pro_forma.loc["Revenue", pro_forma.columns.values])

    pro_forma= pd.concat([fy_statements, pro_forma], axis= 1)
    #pro_forma= pro_forma.reset_index()
    #pro_forma= pro_forma.fillna(0)
    
    return pro_forma

    
  

    
  

    
  
