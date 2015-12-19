class LogicGate:
    def __init__(self,n)
        self.label = n
        self.output = none
    def getLabel(self):
        return self.label
    def getOutput(self):
        return self.output
    
class BinaryGate:
    def __init__(self,n):
        LogicGate __ init__(self,n,pA,pB)
        self.pinA = pA
        self.pinB = pB
    def getpinA(self):
        if self.pinA == none:
            return input(self.getLabel()+'-->')
        else:
            return self pinB.getFrom().getOutput()
    def getpinB(self):
        if self.pinB == none:
            return input(self.getLabel()+'-->')
        else:
            return self.pinB.getFrom.getOutput()
    def setnextpin(self,source):
        if self.pinA == none:
            self.pinA = source
        else:
            if self.pinB == none:
                self.pinB = source
            else:
                print("no empyt pin")
class AndGate(BinaryGate):
	def __init__(self,n,pA,pB):
		BinaryGate __init__(self,n,pA,pB)
		
	def performGateLogic(self):
		a = self.getpinA()
		b = self.getpinB()
		if a == 1 and b == 1:
			return 1
		else:
			return 0
class OrGate(BinaryGate):	
	def __init__(self,n,pA,pB):
            BinaryGate__init__(self,n,pA,pB)
	def performGateLogic(self):
		a = self.getpinA()
		b = self.getpinb()
		if a == 1 or b == 1:
			return 1
		else:
			return 0
		    

class NANDGate(BinaryGate):
    def __init__(self,n,pA,pB):
        BinaryGate__init__(self,n,pA,pB)
    def performGateLogic(self):
        a = self.gatepinA()
        b = self.gatepinB()
        if a == 0 and b == 0:
            return 0
        else:
            return 1
        
class NORGate(BinaryGate):
    def __init__(self,n,pA,pB):
        BinaryGate__init__(self,n,pA,pB)
    def performGateLogic(self):
        a = self.gatepinA()
        b = self.gatepinB()
        if a == 1 and b == 1:
            return 0
        else:
            return 1
class XORGate(BinaryGate):
    def __init__(self,n.pA,pB):
        BinaryGate__init__(self,n,pA,pB)
    def performGateLogic(self):
        a = self.gatepinA()
        b = self.gatepinB()
        if a == 1 and b == 1 or a == 0 and b == 0:
            return 0
        else:
            return 1
class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate   = tgate
        tgate.setNextPin(fgate.gateOutput)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

        
	
	


	


	
                
    
