import pandas as pd
import datetime
import os

today = datetime.datetime.today()


if str(os.path.isfile('/home/Sonu/Documents/Sonu Project/insta.xlsx'))== 'True':
    print ('created')
else:

    today = datetime.datetime.today()
    writer = pd.ExcelWriter('insta.xlsx', engine='xlsxwriter')
    writer.save()



    #dataframe Name and Age columns
    df = pd.DataFrame({today: [(xp)]})

    #Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('insta.xlsx', engine='xlsxwriter')

    #Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    #Close the Pandas Excel writer and output the Excel file.
    writer.save()
