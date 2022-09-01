class Car:

    def __init__(self,name="BMW",model="x33"):
        self.name=name
        self.model=model

    
    def __str__(self):

        return(f"{self.name},model is:,{self.model}")









def main():
    car1=Car("BENZ","C200")
    print(car1)














if __name__=="__main__":
    main()