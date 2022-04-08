import pyodbc 

server = '10.0.0.4\TEST44\SQLEXPRESS, 1433' 
database = 'master' 
username = 'sa' 
password = '2Tfu*(eZj0$tNbO' 

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
