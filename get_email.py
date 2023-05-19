import get_data

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    z=[]
    x=data['results']
    for i in x:
        z.append(i['email'])
    return z
print(get_email(get_data.data))