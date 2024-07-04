import math
class Person():
    def __init__(self,s_name,kg_weight,m_height):
        self.name=s_name
        self.weight=kg_weight
        self.height=m_height
    
    def getBMI(self):   #weight/(height**2)
        bmi=self.weight/(self.height**2)
        return bmi
    
    def isHealthy(self): # Healthy BMI range: 18.5 kg/m2 - 25 kg/m2
        bmi=self.getBMI()
        if bmi>18.5 and bmi<25:
            return True
        return False
    
    def getHealthyWeights(self): # Healthy weight for the height: 59.9 kgs - 81.0 kgs
        max_health_weight= (self.height**2)*25
        min_health_weight= (self.height**2)*18.5
        return min_health_weight,max_health_weight
    
    def whatToDO(self): # Lose 9.0 kgs to reach a BMI of 25 kg/m2.
        bmi=self.getBMI()
        if bmi<18.5:
            return "gain", self.getHealthyWeights()[0]-self.weight 
        elif bmi>25:
            return "lose", self.weight-self.getHealthyWeights()[1]
        return "None. You are in shape."
    
    def __str__(self):
        return "{0} ({1}kg,{2}m)".format(self.name,self.weight,self.height)

if __name__ == "__main__":
        
    p=Person('Amin',90,1.80)
    b=p.getBMI()
    print(b,p.isHealthy(),p.getHealthyWeights(),p.whatToDO())
    print(p)
