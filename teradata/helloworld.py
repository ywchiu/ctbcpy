import teradata

udaExec = teradata.UdaExec(appName= "HelloWorld", version=1);

with udaExec.connect(dsn = "testdsn", method = "odbc" ) as session:
 for row in session.execute("SELECT GetQueryBand()"):
  print(row);
 for row in session.execute("SELECT * FROM dbcinfo"):
  print(row);

