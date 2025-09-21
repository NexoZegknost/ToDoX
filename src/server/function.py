from server.connect import SUPABASE


def checkState(data):
    if len(data) == 0:
        return False
    else:
        return True


def createTask(title, content):
    response = (
        SUPABASE.table("todoX")
        .insert({"title": title, "content": content, "state": False})
        .execute()
    )
    return response.data[0]["id"]


def loadTask():
    response = SUPABASE.table("todoX").select("*").execute()
    data = []
    for i in response:
        data.append(i)
    (tag, data) = data[0]
    return data


def removeTask(index):
    response = SUPABASE.table("todoX").delete().eq("id", index).execute()
    return response.data
