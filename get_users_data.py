import get_data

def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    z=[]
    x=data['results']
    a=[]
    for i in range(len(x)):
        z.append(x[i]["name"]["first"])
        z.append(x[i]["name"]["last"])
        z.append(x[i]["phone"])
        res={"first_name":z[0],"last_name":z[1],"phone_number":z[2]}
        a.append(res)
    return a
print(get_users_data(get_data.data))
