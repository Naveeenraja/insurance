from flask import Flask,render_template,request,redirect,session
from flask_session import Session
import data.mcqutil as mcq_utils
import json
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
            "Gender" : session,
            "Middlename" : "",
            "surname" : "",
            "father / husband name" : "",
            "type of relation" : "",
            "nominee_name" : "",
            "age" : "",
            "Dob" : "",
            "gender" : "",
            "address" : "",
            "district" : "",
            "state" : "",
            "pincode" : "",
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
                # session["gender"]=i["Gender"]
                if i["code_number"]==code :
                    print(i["code_number"])
                    if i["Password"]==password:
                        print(i["Password"])
                        return render_template("dashboard.html", data=data["customers"], code=code,fname=session["firstname"])
        return render_template("login.html" ,message=message)
    
@app.route("/new_policy")
def new_policy():
    if check_session():
        return render_template("reg.html", fname= session["firstname"], code=session["code_number"], email=session["email"], phone=session["phone"])

@app.route("/next_page" , methods=["GET" , "POST"]) 
def next_page():
    if 'user'in session:
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
    
        
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)  