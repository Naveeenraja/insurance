from flask import Flask,render_template,request,redirect,session
from flask_session import Session
import data.mcqutil as mcq_utils
import json
from datetime import date, timedelta
file ="customers.json"
file1 = "policy.json"

app=Flask(__name__)
app.config["SECRET_KEY"]="somekey"
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)

def check_session():
    if len(session.keys())>0:
        return True
    else:
        return False

@app.route("/logout" , methods=["POST" , "GET"]) 
def logout():
    if check_session():
        session.pop("code_number" , None)
        session.pop("Firstname" , None) 
    return redirect("/")  

@app.route("/", methods=["POST" , "GET"])
def index():
    return render_template("index.html")   

@app.route("/register_page", methods=["POST" , "GET"])
def register_page():
    return render_template("register.html")

@app.route("/login_page", methods=["POST" , "GET"])
def login_page():
    return render_template("login.html")   

@app.route("/service_page", methods=["POST" , "GET"])
def service_page():
    return render_template("services.html") 

@app.route("/contact_page", methods=["POST" , "GET"])
def contact_page():
    return render_template("contact.html") 

@app.route("/about_page", methods=["POST" , "GET"])
def about_page():
    return render_template("about.html") 

@app.route("/register", methods=["POST" , "GET"])
def reg():
    data = mcq_utils.read_json(file)
    if request.method=="POST":
        length=len(data["customers"])
        code=length + 100984 
        Policy_Id1=length + 21231 * 2
        Policy_Id2=length + 11231 * 2
        Policy_Id3=length + 41231 * 2
        fname=request.form["firstName"]
        lname=request.form["lastname"]
        email= request.form["email"]
        phone= request.form["phoneNumber"]
        password= request.form["password"]
        list_of_customers={
            "code_number" : code,
            "Firstname" : fname,
            "Lastname"  : lname,
            "phone" : phone,
            "Email" : email,
            "Password" : password,
            "Health Insurance Policy Id": "", 
            "Vehicle Insurance Policy Id": "",
            "Life Insurance Policy Id":"" ,
            "Middlename" : ""  ,
            "Father / Husbandname" : "",
            "Surname" : "",
            "Full Name" : "",
            "nominee" : "" ,
            "Type of relation" : "" ,
            "Age" : "" ,
            "Date of Birth" : "",
            "Gender" : "",
            "Address1" : "",
            "Address2" : "",
            "District" : "",
            "State" : "",
            "Pincode" : "",
            "phone2" : "",
            "email2" : "",  
            "Policy Type" : "",
            "Id Type" : "",
            "Id Number" : "",
            "Premium" : "",
            "Amount" : "",
            "Next Premium Date" : "",
            "Policy Type2" : "",
            "Id Type2" : "",
            "Id Number2" : "",
            "Premium2" : "",
            "Amount2" : "",
            "Next Premium Date2" : "",
            "Policy Type3" : "",
            "Id Type3" : "",
            "Id Number3" : "",
            "Type of vehicle" : "",
            "Vehicle number" : "",
            "DL / RC Num" : "",
            "Amount3" : "",
            "Next Premium Date3" : ""
        }
        data["customers"].append(list_of_customers)
        mcq_utils.write_json(file,data)
        msg= fname + " Your registration has been completed successfully !! " +"your code number is :" + str(code)
        msg2="your code number is :" + str(code)
        data = mcq_utils.read_json(file)
        return render_template("login.html",data=data["customers"],msg=msg )
    # return render_template("mcq2.html", data=data["student registration"])
    
@app.route("/login", methods=["GET" , "POST"])
def login():
    # if check_session():
        data = mcq_utils.read_json(file)
        message=""
        if request.method=="POST":                                                   
            code=int(request.form["code"])
            password=request.form["password"]
            message="incorrect password / code Number" 
            for i in data["customers"] : 
                session['user']=i['Firstname']
                session["firstname"]=i["Firstname"]
                session["email"]=i["Email"]
                session["lastname"]=i["Lastname"]
                session["phone"]=i["phone"]
                session["code_number"]=i["code_number"]
                session["id_number1"]=i["Life Insurance Policy Id"]
                session["Age"]=i["Age"]
                session['Middlename']=i['Middlename']
                session['Surname']= i['Surname']
                session['Father / husband name']=i['Father / Husbandname']
                session['nominee']=i['nominee']
                session['Type of Relation']=i['Type of relation']
                session['Age']=i['Age']
                session['Date of Birth']=i['Date of Birth']
                session['Gender']=i['Gender']
                session['Address1']=i['Address1']
                session['Address2']=i['Address2']
                session['District']= i['District']
                session['State']=i['State']
                session['Pincode']=i['Pincode']
                session['phone2']=i['phone2']
                session['email2']=i['email2']
                session['Policytype']=i['Policy Type']
                session['IDtype']=i['Id Type']
                session['Id Number']=i['Id Number']
                session['Premium']=i['Premium']
                session['Amount']=i['Amount']
                session['Next Premium Date']=i['Next Premium Date']
                session['Full Name']=i['Full Name']
                session['Life Insurance Policy Id']=i['Life Insurance Policy Id']
                session['Policytype2']=i['Policy Type2']
                session['IDtype2']=i['Id Type2']
                session['Id Number2']=i['Id Number2']
                session['Premium2']=i['Premium2']
                session['Amount2']=i['Amount2']
                session['Next Premium Date2']=i['Next Premium Date2']
                session['Health Insurance Policy Id']=i['Health Insurance Policy Id']
                session['Policytype3']=i['Policy Type3']
                session['IDtype3']=i['Id Type3']
                session['Id Number3']=i['Id Number3']
                session['Type of vehicle']=i['Type of vehicle']
                session['Amount3']=i['Amount3']
                session['Vehicle number']=i['Vehicle number']
                session['DL / RC Num']=i['DL / RC Num']
                session['Next Premium Date3']=i['Next Premium Date3']
                session['Vehicle Insurance Policy Id']=i['Vehicle Insurance Policy Id']
                if i["code_number"]==code :
                    
                    if i["Password"]==password:
                        
                        return render_template("sucess.html")
        return render_template("login.html" ,message=message)

@app.route("/gotodashboard")
def gotodashboard():
    msg="Life"
    if check_session():
        return render_template("dashboard.html", msg=msg, fname=session['firstname'])
    

@app.route("/existing")
def existing():
    if check_session():
        data=mcq_utils.read_json(file)
        for i in data['customers']:
            if i['Firstname'] == session['firstname']:
                session['Policytype']=i['Policy Type']
                session['Life Insurance Policy Id']=i['Life Insurance Policy Id']
                session['Premium']=i['Premium']
                session['Amount']=i['Amount']
                session['Next Premium Date']=i['Next Premium Date']
                session['Full Name']=i['Full Name']
                session['nominee']=i['nominee']
        return render_template("existing.html", data=data["customers"],premiumdate=session['Next Premium Date'] , fname=session['firstname'] ,amount= session['Amount'],premium= session['Premium'], policyholdername= session['Full Name'],  policytype=session['Policytype'] ,policyid=session["Health Insurance Policy Id"] ,nominee=session['nominee'] )
    

@app.route("/gotohealth")
def gotohealth():
    msg2="Health"
    return render_template("dashboardd.html",msg2=msg2, fname=session['firstname'] )

@app.route("/existing2")
def existing2():
    if check_session():
        data=mcq_utils.read_json(file)
        for i in data['customers']:
            if i['Firstname'] == session['firstname']:
                session['Policytype2']=i['Policy Type2']
                session['Health Insurance Policy Id']=i['Health Insurance Policy Id']
                session['Premium2']=i['Premium2']
                session['Amount2']=i['Amount2']
                session['Next Premium Date2']=i['Next Premium Date2']
                session['Full Name']=i['Full Name']
                session['nominee']=i['nominee']
        return render_template("existing2.html",data=data["customers"],premiumdate=session['Next Premium Date2'] , fname=session['firstname'] ,amount= session['Amount2'],premium= session['Premium2'], policyholdername= session['Full Name'],  policytype=session['Policytype2'] ,policyid=session["Health Insurance Policy Id"] ,nominee=session['nominee'])


@app.route("/gotovehicle")
def gotovehicle():
    msg1="Vehicle"
    if check_session():
        return render_template("dashboarddd.html",msg1=msg1,fname=session['firstname'] )

@app.route("/existing3")
def existing3():
    return render_template("existing3.html")


@app.route("/new_policy")
def new_policy():
    if check_session():
        return render_template("reg.html", fname= session["firstname"], code=session["code_number"], email=session["email"], phone=session["phone"])

@app.route("/next_page" , methods=["GET" , "POST"]) 
def next_page():
    if 'user' in session:
        if request.method == 'POST':
            with open('customers.json') as json_file:
                data = json.load(json_file)
            for i in data['customers']:
                if i['Firstname'] == session['firstname']:
                    i['Middlename']=request.form["middle"]
                    i['Surname']=request.form["surname"]
                    i['Father / Husbandname']=request.form["fhname"]
                    i['nominee']=request.form["nominee"]
                    i['Type of relation']=request.form["relation"]
                    i['Age']=request.form['age']
                    i['Date of Birth']=request.form["dob"]
                    i['Gender'] = request.form['gender']
                    i['Address1']=request.form["address1"]
                    i['Address2']=request.form["address2"]
                    i['District']=request.form["dis"]
                    i['State']=request.form["state"]
                    i['Pincode']=request.form["pin"]
                    i['phone2']=request.form['phone']
                    i['email2']=request.form['email']
                    session['Middlename']=i['Middlename']
                    session['Surname']= i['Surname']
                    session['Father / husband name']=i['Father / Husbandname']
                    session['nominee']=i['nominee']
                    session['Type of Relation']=i['Type of relation']
                    session['Age']=i['Age']
                    session['Date of Birth']=i['Date of Birth']
                    session['Gender']=i['Gender']
                    session['Address1']=i['Address1']
                    session['Address2']=i['Address2']
                    session['District']= i['District']
                    session['State']=i['State']
                    session['Pincode']=i['Pincode']
                    session['phone2']=i['phone2']
                    session['email2']=i['email2']
            with open('customers.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
            return render_template("next.html", fname=session['firstname'], lname=session['lastname'], nominee=session['nominee'],mname= session['Middlename'],sname=session['Surname'],fhname=session['Father / husband name'],relation=session['Type of Relation'], age=session['Age'],dob=session['Date of Birth'],gender=session['Gender'],add1=session['Address1'],add2=session['Address2'],dis=session['District'],state=session['State'],pin=session['Pincode'],phone=session['phone'] and session['phone2'],email=session['email'] and session['email2'])   
@app.route("/edit" , methods=["GET" , "POST"]) 
def edit():
    return render_template("reg.html" , fname= session["firstname"], code=session["code_number"], email=session["email"], phone=session["phone"])   

@app.route("/exit" , methods=["GET" , "POST"])   
def exit():
     return render_template("dashboard.html" ,premiumdate=session['Next Premium Date'] , fname=session['firstname'] ,amount= session['Amount'],premium= session['Premium'], policyholdername= session['Full Name'],  policytype=session['Policytype'] ,policyid=session["id_number1"] ,nominee=session['nominee'])

@app.route("/save" , methods=["GET" , "POST"])   
def save():
    current_date=date.today()
    threemonth= current_date + timedelta(days=90)
    onemonth= current_date + timedelta(days=30)
    twomonth = current_date + timedelta(days=60)
    sixmonth = current_date + timedelta(days=180)
    msg="Platinum Premuim - 2256/- per 3 month "
    msg1="Gold Premium - Rs.1856/- per 3 months"
    msg2="Silver Premium - Rs.1056/- per 3 months"
    msg3="Bronze Premium - Rs.956/- per 3 months"
    msg4="Platinum Premium - Rs.1056/- per month"
    msg5="Gold Premium - Rs.896/- per  month"
    msg6="Silver Premium - Rs.446/- per month"
    msg7="Bronze Premium - Rs.276/- per month"
    return render_template("policy.html", current_date=current_date, threemonth=threemonth ,onemonth=onemonth, fname=session['firstname'], nominee=session['nominee'] , fhname=session['Father / husband name'], msg=msg, msg1=msg1, msg2=msg2, msg3=msg3, msg4=msg4, msg5=msg5, msg6=msg6, msg7=msg7) 

@app.route("/life" , methods=["GET" , "POST"])  
def life_insurance():
    if check_session():
        data=mcq_utils.read_json(file)
        length=len(data["customers"])
        if 'user' in session:
            if request.method == 'POST':
                with open('customers.json') as json_file:
                    data = json.load(json_file)
                for i in data['customers']:
                    if i['Firstname'] == session['firstname']:
                        i['Policy Type']=request.form["policytype"]
                        i['Id Type']=request.form["idtype"]
                        i['Id Number']=request.form["idnumber"]
                        i['Premium']=request.form["policy"]
                        i['Amount']=request.form["type"]
                        i['Full Name']=request.form["name"]
                        i['Health Insurance Policy Id']=length * 2131125 * 2
                        i['Life Insurance Policy Id']= length * 324567 * 3
                        i['Vehicle Insurance Policy Id']=length * 456346 * 4
                        i['Next Premium Date']=request.form["type2"]
                        session['Policytype']=i['Policy Type']
                        session['IDtype']=i['Id Type']
                        session['Id Number']=i['Id Number']
                        session['Premium']=i['Premium']
                        session['Amount']=i['Amount']
                        session['Next Premium Date']=i['Next Premium Date']
                        session['Full Name']=i['Full Name']
                with open('customers.json', 'w') as json_file:
                    json.dump(data, json_file, indent=4)
                return render_template("dashboard.html", premiumdate=session['Next Premium Date'] , fname=session['firstname'] ,amount= session['Amount'],premium= session['Premium'], policyholdername= session['Full Name'],  policytype=session['Policytype'] ,policyid=session["id_number1"] ,nominee=session['nominee'])
        

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)  