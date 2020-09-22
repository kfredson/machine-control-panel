from flask import Flask, request
app = Flask(__name__)
OUTPUT_LOCATION='C:\\Users\\Administrator\\'

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/submit_write_file')
def write_out_file():
    f = open('C:\\Users\\Administrator\\machine_control_panel\\template.txt')
    template = f.read()
    f.close()
    power = request.args.get('power')
    mode = request.args.get('mode')
    t = request.args.get('thickness')
    power_val = None
    if power=='on':
        power_val = '1'
    elif power=='off':
        power_val = '0'
    grind_val = None
    polish_val = None
    if mode=='grind':
        grind_val = '1'
        polish_val = '0'
    elif mode=='polish':
        grind_val = '0'
        polish_val = '1'
    t_val = None
    if int(t) >= 1 and int(t) <= 999:
        t_val = t.strip()+'.0'
    if power_val!=None and grind_val!=None and polish_val!=None and t_val!=None:
        template = template.replace('$0',power_val)
        template = template.replace('$1',polish_val)
        template = template.replace('$2',grind_val)
        template = template.replace('$3',t_val)
        g = open(OUTPUT_LOCATION+'01000','w')
        g.write(template)
        g.close()
    else:
        raise Exception('Did not get all required values')
    return 'SUCCESS'