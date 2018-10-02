def delegate(request):
    """
    Delegates any HTTP request to the proper action
    """
    mushroom = Mushroom(**request.get_json())
    mapper = MushroomMapper()
    if request["method"] == "POST":
        mapper.put_mushroom(mushroom)
