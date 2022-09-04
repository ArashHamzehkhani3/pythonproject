class Car:

    def __init__(self,name="BMW",model="x33", driver="user"):
        self.name=name
        self.model=model
        self.driver=driver

    
    def __str__(self):

        return(f"{self.name},model is:,{self.model}")





    def start(self,fuel):
        self.fuel=fuel

        print(f"Engine have started with{self.fuel}")






    
    def get_name(self,drive):
       self.drive=drive
       drivername={}
       drivername["name"]=self.drive
       print("This car is driven by ",drivername["name"])











def main():
    uname=input("Enter name of  the car:")
    model=input("Enter the model:")
    driver=input("what is your name")
    car1=Car(uname,model,driver)
    car1.get_name(driver)
    car1.start(40) 









if __name__=="__main__":
    main()