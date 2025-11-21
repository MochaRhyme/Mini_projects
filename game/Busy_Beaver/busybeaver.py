class summon_beaver:
    def __init__(self,state:int=0,state_num:int=2,position:int=0,*commands):
        self.state=state
        self.state_num=state_num
        self.position=position
        self.step=0
        self.commands=commands
    def __str__(self):
        return {'state':self.state,'state_num':self.state_num,'position':self.position,'step':self.step},'\nCommands :',self.commands