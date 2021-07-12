from a_basic_ex.cust_db.cust_model import *
from abc import ABC, abstractmethod


class Service(ABC):

    @abstractmethod
    def add_customer(self, cust):
        pass

    @abstractmethod
    def update_customer(self, cust):
        pass

    @abstractmethod
    def delete_customer(self, custId):
        pass

    @abstractmethod
    def get_customer(self, custId):
        pass

    @abstractmethod
    def get_all_customer(self):
        pass


class ServiceImpl(Service):

    def add_customer(self, cust):
        if self.get_customer(cust.customerId):
            return 'Duplicate customer with id {}'.format(cust.customerId)
        else:
            db.session.add(cust)
            db.session.commit()
            return 'Customer id {} added successfully'.format(cust.customerId)

    def update_customer(self, cust):
        db_cust = self.get_customer(cust.customerId)
        if db_cust:
            db_cust.customerName = cust.customerName
            db_cust.customerAge = cust.customerAge
            db_cust.customerBalance = cust.customerBalance
            db_cust.customerAddress = cust.customerAddress
            db.session.commit()
            return 'Customer {} info updated successfully'.format(cust.customerId)
        else:
            return 'customer with {} id not present so can not update'.format(cust.customerId)

    def delete_customer(self, custId):
        db_cust = self.get_customer(custId)
        if db_cust:
            db.session.delete(db_cust)
            db.session.commit()
            return 'customer {} info deleted successfully'.format(custId)
        else:
            return 'customer with {} id not present so can not delete'.format(custId)

    def get_customer(self, custId):
        return Customer.query.filter_by(customerId=custId).first()

    def get_all_customer(self):
        return Customer.query.all()
