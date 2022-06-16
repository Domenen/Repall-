


# --------------------------------------------------------------------------------
#           Попытка 1
# --------------------------------------------------------------------------------

# d = { "dialect" :"", "driver":"", "username":"", "password":"", "host":"", "port":"", "database":""}

# def parse_connection_string(x):


    # if ":///" in x:
    #     d["dialect"] = "sqlite3"
    #     d["database"] = x.lstrip("sqlite3:///")
    #     print(d)
    # elif "+" in x and "://" in x:
    #     m_driver = x.split("://")
    #     drivers = m_driver[0].split("+")
    #     d["dialect"] = drivers[0]
    #     d["driver"] = drivers[1]
    #     user_name_pass = m_driver[1].split(":")
    #     d["username"] = user_name_pass[0]
    #     d["password"] = user_name_pass[1].split("/")[0].split("@")[0]
    #     d["host"] = user_name_pass[1].split("/")[0].split("@")[1]
    #     # d["port"] = user_name_pass[1].split("/")[0].split("@")[1].split(":")[1]
    #     d["database"] = user_name_pass[1].split("/")[1]
    #     print(d)
    # elif "://" in x:
    #     m_driver = x.split("://")
    #     user_name_pass = m_driver[1].split(":")
    #     d["dialect"] = m_driver[0]
    #     d["username"] = user_name_pass[0]
    #     d["password"] = user_name_pass[1].split("/")[0]
    #     d["database"] = user_name_pass[1].split("/")[1]
    #     print(d)


# -------------------------------------------------------------------------------
#             Попытка 2
# -------------------------------------------------------------------------------

# d = { "dialect" :"", "driver":"", "username":"", "password":"", "host":"", "port":"", "database":""}
connection_string = "postgresql+psycopg2://admin:1234@localhost:fsadghws/b4_7"

def parse_connection_string(x):

    d = { "dialect" :"", "driver":"", "username":"", "password":"", "host":"", "port":"", "database":""}

    if ":///" in x:
        d["dialect"] = x.split(":///")[0]
        d["database"] = x.split(":///")[1]
        print(d)
    else:
        base = x.split("://")
        if "+" in base[0]:
            d["dialect"] = base[0].split("+")[0]
            d["driver"] = base[0].split("+")[1]
        else:
            d["dialect"] = base[0]
        if "@" in base[1]:
            d["username"] = base[1].split("@")[0].split(":")[0]
            d["password"] = base[1].split("@")[0].split(":")[1]
            d["database"] = base[1].split("/")[1]
            if ":" in base[1].split("@")[1]:
                d["host"] = base[1].split("@")[1].split(":")[0]
                d["port"] = base[1].split("@")[1].split(":")[1].split("/")[0]
            else:
                d["host"] = base[1].split("@")[1].split("/")[0]
        else:
            d["username"] = base[1].split(":")[0]
            d["password"] = base[1].split(":")[1].split("/")[0]
            d["database"] = base[1].split(":")[1].split("/")[1]

    return(d)


parse_connection_string(connection_string)

# ------------------------------------------------------------------------------------------------
#                 Попытка 3
# ------------------------------------------------------------------------------------------------

