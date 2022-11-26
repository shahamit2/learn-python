class Authors(dict):
    def __getattr__(self,val):
        return self[val]

a = Authors()
a['Indian'] = ["Nisarg Dutta", "Sadhguru"]
a['German'] = ["Eckhart"]
a.Indian