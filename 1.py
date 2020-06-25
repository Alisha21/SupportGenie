class agent():
    def __init__(self,name,is_available,available_since,roles):
        self.name = name
        self.is_available = is_available
        self.available_since = available_since
        self.roles = roles

class agentselector():
    def __init__(self,listofagents,selectmode):
        self.listofagents = listofagents
        self.selectmode = selectmode
        
        
    def agentselector(self,roleofissue):
        list = []
        if self.selectmode.lower() == "all available":
            for em in self.listofagents:
                for s in em.roles:
                    if s == roleofissue and em.is_available == "True":
                        list.append(em.name)
                        break
                    
        elif self.selectmode.lower() == "least busy":
            n = []
            for em in self.listofagents:
                  n.append(em.available_since)
            
            maxi = max(n)
            for em in self.listofagents:
                if em.available_since == maxi:
                    for s in em.roles:
                        if s == roleofissue:
                            list.append(em.name) 
                            break
                  
              
        elif self.selectmode.lower() == "random":
            for em in self.listofagents:
                for s in em.roles:
                    if s == roleofissue:
                        list.append(em.name)
                        break
            
        return list

ls = []
noofagents = int(input("Please enter the no. of agents: "))
for i in range(noofagents):
    name = input("Enter the name of the agent: ")
    a = input("Enter the agent is available or not? (True or False) ")
    if  a.capitalize() == "True":
        b = input("The agent is available since? (Enter the time in hh:mm:ss format): ").split(":")
        h = int(b[0])
        m = int(b[1])
        s = int(b[2])
        timeinmin = h * 60 + m
        timeinsec = timeinmin * 60 + s
    else:
        timeinsec = 0 
    c = input("Enter the list of roles that the agent is capable of separated by comma: ").split(",")
    ls.append(agent(name,a.capitalize(),timeinsec,c))

selectmode = input("Enter the selection mode: ")
role = input("Enter role of issue that you want to present to any agent: ")
obj = agentselector(ls,selectmode)
print(obj.agentselector(role))    

