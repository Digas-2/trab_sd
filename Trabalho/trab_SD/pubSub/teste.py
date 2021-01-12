class SubscriberData:
  def __init__(self, tag,connection_status):
    #self.sub_id = sub_id
    self.tag = tag
    self.connection_status = connection_status

dict_of_subs = {"":SubscriberData}

dict_of_subs["teste"] = SubscriberData("babvab",True)
dict_of_subs["teste2"] = SubscriberData("gghff",False)
dict_of_subs["teste3"] = SubscriberData("babtr3vab",False)

print(dict_of_subs["teste"].tag)