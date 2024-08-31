start_yyyymm = '201107'
end_yyyymm = '202201'

if start_yyyymm == end_yyyymm:
    Print("difference is 0")
else:
    months = (int(end_yyyymm[:4])-(int(start_yyyymm[:4])+1))*12
    start_year_end_month_diff = 12-int(start_yyyymm[4:])
    end_year_start_month_diff = int(end_yyyymm[4:])

    print(months+start_year_end_month_diff+end_year_start_month_diff)