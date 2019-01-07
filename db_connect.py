from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:1sw-ipetre@localhost:3306/classicmodels')
print(engine.table_names())