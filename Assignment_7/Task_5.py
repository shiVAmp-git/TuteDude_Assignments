from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def process_payment(self,amount):
        self.amount=amount
        print(f"INR {self.amount} got processed")
class CreditCardPayment(Payment):
    def process_payment(self,amount):
        self.amount=amount
        print(f"INR {self.amount} id done via Credit Card")
class UPIPayment(Payment):
    def process_payment(self,amount):
        self.amount=amount
        print(f"INR {self.amount} got processed via UPI")    
cc1 = CreditCardPayment()
cc1.process_payment(5000)
upi1 = UPIPayment()
upi1.process_payment(6000)