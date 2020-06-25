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
        if self.selectmode == "All Available":
            for em in self.listofagents:
                for s in em.roles:
                    if s == roleofissue and em.is_available == "True":
                        list.append(em.name)
                        break
                    
        elif self.selectmode == "Least Busy":
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
                  
              
        elif self.selectmode == "Random":
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
    a = input("Enter the agent is available or not? ")
    b = input("The agent is available since? (Enter the time in hh:mm:ss format): ")
    b.split(":")
    h = b[0]
    m = b[1]
    s = b[2]
    timeinmin = h * 60 + m
    timeinsec = timeinmin * 60 + s 
    c = input("Enter the list of roles that the agent is capable of separated by comma: ").split(",")
    ls.append(agent(name,a,timeinsec,c))

selectmode = input("Enter the selection mode: ")
role = input("Enter role of issue: ")
obj = agentselector(ls,selectmode)
print(obj.agentselector(role))    

