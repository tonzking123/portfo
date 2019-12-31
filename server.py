import csv
from flask import Flask , render_template,url_for, request,redirect
app = Flask(__name__)

@app.route('/') #root directory = home page of the web
def hello_world():
    #print(url_for('static', filename='cloud storage.ico'))
    return render_template('index.html') #normally render_template is calling template from folder named templates so you need to create that folder and put your template in

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode = 'a') as database:
        email = data['email']
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',mode='a',newline='') as database2:
        email = data['email']
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
        

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #print(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "something is wrong with database"
    else:
        return 'something went wrong'
