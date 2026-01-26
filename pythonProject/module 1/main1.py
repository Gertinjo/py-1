contact_info = {
    "Gerti" : "04800000",
    "Dren"  : "04880123"
}
print(contact_info)

Gerti_phone = contact_info["Gerti"]
print(Gerti_phone)

contact_info["Gerti"] = "048000000"
print(contact_info)

contact_info["Deon"] = "044123123"
print(contact_info)

del contact_info["Deon"]
print(contact_info)




contact_information = {
    "Gerti":{
        "phone": "54454848",
        "email": "gerti@gmail.com",
        "birthday": "19.19.1999"
    },
    "Dreni":{
        "phone": "1236654",
        "email": "dreni@gmail.com",
        "birthday": "31.12.2025"
    },
    "Deon":{
        "phone": "6576534",
        "email": "deon@gmail.com",
        "birthday": "12/01/1500"
    }
}
print(contact_information)
gerti_infos = contact_information["Gerti"]
print(gerti_infos)

contacts = {
    "Gerti": ("12354343" , "gerti@gmail.com"),
    "Dren": ("453543213" , "dren@gmail.com"),
    "Deon": ("43543123" , "deon@gmail.com")
}

gerti_infos = contacts["Gerti"]
phone_number = gerti_infos[0]
print(phone_number)