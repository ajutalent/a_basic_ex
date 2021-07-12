from a_basic_ex.cust_db.cust_model import Customer, app
from a_basic_ex.cust_db.cust_service import ServiceImpl
from flask import request, render_template

service = ServiceImpl()


def dummy_cust():
    return Customer(customerId=0, customerName='', customerAge=0, customerBalance=0.0, customerAddress='')


@app.route('/cust/welcome/', methods=['GET'])
def welcome_customer():
    return render_template('cust.html',cust=dummy_cust(), customers=service.get_all_customer())


@app.route('/cust/save/', methods=['GET', 'POST'])
def save_cust_info():
    msg = ''
    if request.method == 'GET':
        pass
    else:
        ctid = int(request.form['cid'])
        ctnm = (request.form['cnm'])
        ctage = int(request.form['cage'])
        ctbalance = float(request.form['cbal'])
        ctaddress = (request.form['cadr'])
        customer = Customer(customerId = ctid, customerName = ctnm, customerAge= ctage, customerBalance = ctbalance, customerAddress = ctaddress)
        msg = service.add_customer(customer)
    return render_template('cust.html', cust=dummy_cust(), action=msg, customers=service.get_all_customer())


if __name__ == '__main__':
    app.run(debug=True)
