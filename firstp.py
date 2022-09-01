class Car:

    def __init__(self,name="BMW",model="x33"):
        self.name=name
        self.model=model

    
    def __str__(self):

        return(f"{self.name},model is:,{self.model}")









def main():
    uname=input("Enter name of  the car:")
    model=input("Enter the model:")
    car1=Car(uname,model)
    print(car1)














if __name__=="__main__":
    main()