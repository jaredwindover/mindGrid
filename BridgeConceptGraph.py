from IntKey import IntKey

class BridgeConceptGraph:
    
    def __init__(self,baseKey = IntKey()):
        self.baseKey = baseKey
        self.freedKeys = []
        self.lastKey = baseKey.get(0)
        self.bridges = {}
        self.concepts = {}
        self.ForwardEdges = {}
        self.ReverseEdges = {}

    def AddBridge(self,bridge):
        k = self.GetNextKey()
        self.bridges[k] = bridge
        self.ForwardEdges[k] = []
        self.ReverseEdges[k] = []
        return k

    def AddConcept(self,concept):
        k = self.GetNextKey()
        self.concepts[k] = concept
        self.ForwardEdges[k] = []
        self.ReverseEdges[k] = []
        return k
        
    def GetNextKey(self):
        try:
            return self.freedKeys.pop()
        except:
            k = self.lastKey
            self.lastKey = self.baseKey.increment(self.lastKey)
            return k

    def ConnectBridgeToConcept(self, iBridge, iConcept):
        self.ForwardEdges[iBridge].append(iConcept)
        self.ReverseEdges[iConcept].append(iBridge)

    def ConnectConceptToBridge(self,iConcept,iBridge):
        self.ForwardEdges[iConcept].append(iBridge)
        self.ReverseEdges[iBridge].append(iConcept)

    def DisconnectBridgeFromConcept(self,iBridge,iConcept):
        self.ForwardEdges[iBridge].remove(iConcept)
        self.ReverseEdges[iConcept].remove(iBridge)

    def DisconnectConceptFromBridge(self,iConcept,iBridge):
        self.ForwardEdges[iConcept].remove(iBridge)
        self.ReverseEdges[iBridge].remove(iConcept)
        
    def RemoveBridge(self,iBridge):
        del self.bridges[iBridge]
        for i in self.ForwardEdges[iBridge]:
            self.ReverseEdges[i].remove(iBridge)
        for i in self.ReverseEdges[iBridge]:
            self.ForwardEdges[i].remove(iBridge)
        del self.ReverseEdges[iBridge]
        del self.ForwardEdges[iBridge]
        self.freedKeys.append(iBridge)

    def RemoveConcept(self,iConcept):
        del self.concepts[iConcept]
        for i in self.ForwardEdges[iConcept]:
            self.ReverseEdges[i].remove(iConcept)
        for i in self.ReverseEdges[iConcept]:
            self.ForwardEdges[i].remove(iConcept)
        del self.ReverseEdges[iConcept]
        del self.ForwardEdges[iConcept]
        self.freedKeys.append(iConcept)
