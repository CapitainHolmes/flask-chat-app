{"filter":false,"title":"run.py","tooltip":"/run.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":23,"column":20},"end":{"row":23,"column":21},"action":"insert","lines":[" "],"id":596},{"start":{"row":23,"column":21},"end":{"row":23,"column":22},"action":"insert","lines":["s"]},{"start":{"row":23,"column":22},"end":{"row":23,"column":23},"action":"insert","lines":["e"]},{"start":{"row":23,"column":23},"end":{"row":23,"column":24},"action":"insert","lines":["s"]},{"start":{"row":23,"column":24},"end":{"row":23,"column":25},"action":"insert","lines":["s"]},{"start":{"row":23,"column":25},"end":{"row":23,"column":26},"action":"insert","lines":["i"]},{"start":{"row":23,"column":26},"end":{"row":23,"column":27},"action":"insert","lines":["o"]},{"start":{"row":23,"column":27},"end":{"row":23,"column":28},"action":"insert","lines":["n"]}],[{"start":{"row":23,"column":28},"end":{"row":23,"column":29},"action":"insert","lines":[":"],"id":597}],[{"start":{"row":23,"column":29},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":598},{"start":{"row":24,"column":0},"end":{"row":24,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":24,"column":8},"end":{"row":24,"column":9},"action":"insert","lines":["r"],"id":599},{"start":{"row":24,"column":9},"end":{"row":24,"column":10},"action":"insert","lines":["e"]},{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"insert","lines":["t"]},{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"insert","lines":["u"]},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["r"]},{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"insert","lines":["n"]}],[{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"insert","lines":[" "],"id":600},{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"insert","lines":["r"]},{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"insert","lines":["e"]},{"start":{"row":24,"column":17},"end":{"row":24,"column":18},"action":"insert","lines":["d"]},{"start":{"row":24,"column":18},"end":{"row":24,"column":19},"action":"insert","lines":["i"]},{"start":{"row":24,"column":19},"end":{"row":24,"column":20},"action":"insert","lines":["r"]},{"start":{"row":24,"column":20},"end":{"row":24,"column":21},"action":"insert","lines":["e"]},{"start":{"row":24,"column":21},"end":{"row":24,"column":22},"action":"insert","lines":["c"]},{"start":{"row":24,"column":22},"end":{"row":24,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":24,"column":23},"end":{"row":24,"column":24},"action":"insert","lines":["."],"id":601}],[{"start":{"row":24,"column":24},"end":{"row":24,"column":26},"action":"insert","lines":["()"],"id":602}],[{"start":{"row":24,"column":25},"end":{"row":24,"column":26},"action":"insert","lines":["s"],"id":603},{"start":{"row":24,"column":26},"end":{"row":24,"column":27},"action":"insert","lines":["e"]},{"start":{"row":24,"column":27},"end":{"row":24,"column":28},"action":"insert","lines":["e"]},{"start":{"row":24,"column":28},"end":{"row":24,"column":29},"action":"insert","lines":["s"]},{"start":{"row":24,"column":29},"end":{"row":24,"column":30},"action":"insert","lines":["i"]},{"start":{"row":24,"column":30},"end":{"row":24,"column":31},"action":"insert","lines":["o"]},{"start":{"row":24,"column":31},"end":{"row":24,"column":32},"action":"insert","lines":["n"]}],[{"start":{"row":24,"column":32},"end":{"row":24,"column":34},"action":"insert","lines":["[]"],"id":604}],[{"start":{"row":24,"column":33},"end":{"row":24,"column":35},"action":"insert","lines":["\"\""],"id":605}],[{"start":{"row":24,"column":34},"end":{"row":24,"column":35},"action":"insert","lines":["u"],"id":606},{"start":{"row":24,"column":35},"end":{"row":24,"column":36},"action":"insert","lines":["s"]},{"start":{"row":24,"column":36},"end":{"row":24,"column":37},"action":"insert","lines":["e"]},{"start":{"row":24,"column":37},"end":{"row":24,"column":38},"action":"insert","lines":["r"]},{"start":{"row":24,"column":38},"end":{"row":24,"column":39},"action":"insert","lines":["n"]},{"start":{"row":24,"column":39},"end":{"row":24,"column":40},"action":"insert","lines":["a"]},{"start":{"row":24,"column":40},"end":{"row":24,"column":41},"action":"insert","lines":["m"]},{"start":{"row":24,"column":41},"end":{"row":24,"column":42},"action":"insert","lines":["e"]}],[{"start":{"row":26,"column":4},"end":{"row":26,"column":8},"action":"remove","lines":["    "],"id":607}],[{"start":{"row":24,"column":23},"end":{"row":24,"column":24},"action":"remove","lines":["."],"id":608}],[{"start":{"row":24,"column":26},"end":{"row":24,"column":27},"action":"remove","lines":["e"],"id":609}],[{"start":{"row":24,"column":26},"end":{"row":24,"column":27},"action":"insert","lines":["s"],"id":610}],[{"start":{"row":24,"column":24},"end":{"row":24,"column":31},"action":"remove","lines":["session"],"id":611},{"start":{"row":24,"column":24},"end":{"row":24,"column":31},"action":"insert","lines":["session"]}],[{"start":{"row":0,"column":0},"end":{"row":39,"column":70},"action":"remove","lines":["import os","from datetime import datetime","from flask import Flask, redirect, render_template, request, session","","app = Flask(__name__)","app.secret_key = \"randomstring123\"","messages = []","","def add_messages(username, message):","    \"\"\"Add messages to the 'messages' list\"\"\"","    now = datetime.now().strftime(\"%H:%M:%S\")","    messages.append(\"({}) {}: {}\".format(now, username, message))","","def get_all_messages():","    \"\"\"Get all messages and separate them with a 'br'\"\"\"","    return \"<br>\".join(messages)","","@app.route('/', methods = [\"GET\", \"POST\"])","def index():","    \"\"\"Main page with instructions\"\"\"","    if request.method == \"POST\":","        session[\"username\"] = request.form[\"username\"]","        ","    if \"username\" in session:","        return redirect(session[\"username\"])","        ","    return render_template(\"index.html\")","    ","@app.route('/<username>')","def user(username):","    \"\"\"Display chat messages\"\"\"","    return \"<h1>Welcome, {0}</h1>{1}\".format(username, get_all_messages())","    ","@app.route('/<username>/<message>')","def send_message(username, message):","    \"\"\"Create a new message and redirect to the chat page\"\"\"","    add_messages(username, message)","    return redirect(\"/\" + username)","    ","app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)"],"id":612},{"start":{"row":0,"column":0},"end":{"row":46,"column":70},"action":"insert","lines":["import os","from datetime import datetime","from flask import Flask, redirect, render_template, request, session","","","app = Flask(__name__)","app.secret_key = \"randomstring123\"","messages = []","","","def add_messages(username, message):","    \"\"\"Add messages to the `messages` list\"\"\"","    now = datetime.now().strftime(\"%H:%M:%S\")","    messages.append(\"({}) {}: {}\".format(now, username, message))","","","def get_all_messages():","    \"\"\"Get all of the messages and separate them with a `br`\"\"\"","    return \"<br>\".join(messages)","","","@app.route(\"/\", methods=[\"GET\", \"POST\"])","def index():","    \"\"\"Main page with instructions\"\"\"","    if request.method == \"POST\":","        session[\"username\"] = request.form[\"username\"]","","    if \"username\" in session:","        return redirect(session[\"username\"])","","    return render_template(\"index.html\")","","","@app.route(\"/<username>\")","def user(username):","    \"\"\"Display chat messages\"\"\"","    return \"<h1>Welcome, {0}</h1>{1}\".format(username, get_all_messages())","","","@app.route(\"/<username>/<message>\")","def send_message(username, message):","    \"\"\"Create a new message and redirect back to the chat page\"\"\"","    add_messages(username, message)","    return redirect(\"/\" + username)","","","app.run(host=os.getenv(\"IP\"), port=int(os.getenv(\"PORT\")), debug=True)"]}],[{"start":{"row":12,"column":45},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":613},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":4},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":614},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["m"],"id":615},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["e"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["s"]},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["s"]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["G"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["E"]},{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"insert","lines":["="]}],[{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"remove","lines":["="],"id":616},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"remove","lines":["E"]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"remove","lines":["G"]}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["a"],"id":617},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["g"]},{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"insert","lines":["e"]},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"insert","lines":["."]},{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["d"]}],[{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["i"],"id":618},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":["c"]},{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":16},"end":{"row":13,"column":18},"action":"insert","lines":["()"],"id":619}],[{"start":{"row":13,"column":16},"end":{"row":13,"column":18},"action":"remove","lines":["()"],"id":620}],[{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"insert","lines":[" "],"id":621},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["="]}],[{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":[" "],"id":622}],[{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["{"],"id":623}],[{"start":{"row":13,"column":20},"end":{"row":13,"column":22},"action":"insert","lines":["\"\""],"id":624}],[{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":["t"],"id":625},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["i"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["m"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["e"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"insert","lines":["s"]}],[{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["t"],"id":626},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"insert","lines":["a"]},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"insert","lines":["m"]},{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"insert","lines":["p"]}],[{"start":{"row":13,"column":31},"end":{"row":13,"column":32},"action":"insert","lines":[":"],"id":627}],[{"start":{"row":13,"column":32},"end":{"row":13,"column":33},"action":"insert","lines":[" "],"id":628}],[{"start":{"row":13,"column":33},"end":{"row":13,"column":34},"action":"insert","lines":["n"],"id":629},{"start":{"row":13,"column":34},"end":{"row":13,"column":35},"action":"insert","lines":["o"]},{"start":{"row":13,"column":35},"end":{"row":13,"column":36},"action":"insert","lines":["w"]}],[{"start":{"row":13,"column":36},"end":{"row":13,"column":37},"action":"insert","lines":["."],"id":630}],[{"start":{"row":13,"column":36},"end":{"row":13,"column":37},"action":"remove","lines":["."],"id":631}],[{"start":{"row":13,"column":36},"end":{"row":13,"column":37},"action":"insert","lines":[","],"id":632}],[{"start":{"row":13,"column":37},"end":{"row":13,"column":38},"action":"insert","lines":[" "],"id":633}],[{"start":{"row":13,"column":38},"end":{"row":13,"column":40},"action":"insert","lines":["\"\""],"id":634}],[{"start":{"row":13,"column":39},"end":{"row":13,"column":40},"action":"insert","lines":["f"],"id":635},{"start":{"row":13,"column":40},"end":{"row":13,"column":41},"action":"insert","lines":["r"]},{"start":{"row":13,"column":41},"end":{"row":13,"column":42},"action":"insert","lines":["o"]},{"start":{"row":13,"column":42},"end":{"row":13,"column":43},"action":"insert","lines":["m"]}],[{"start":{"row":13,"column":44},"end":{"row":13,"column":45},"action":"insert","lines":[":"],"id":636}],[{"start":{"row":13,"column":45},"end":{"row":13,"column":46},"action":"insert","lines":[" "],"id":637}],[{"start":{"row":13,"column":46},"end":{"row":13,"column":47},"action":"insert","lines":["u"],"id":638},{"start":{"row":13,"column":47},"end":{"row":13,"column":48},"action":"insert","lines":["s"]},{"start":{"row":13,"column":48},"end":{"row":13,"column":49},"action":"insert","lines":["e"]},{"start":{"row":13,"column":49},"end":{"row":13,"column":50},"action":"insert","lines":["r"]},{"start":{"row":13,"column":50},"end":{"row":13,"column":51},"action":"insert","lines":["n"]},{"start":{"row":13,"column":51},"end":{"row":13,"column":52},"action":"insert","lines":["a"]},{"start":{"row":13,"column":52},"end":{"row":13,"column":53},"action":"insert","lines":["m"]},{"start":{"row":13,"column":53},"end":{"row":13,"column":54},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":54},"end":{"row":13,"column":55},"action":"insert","lines":[","],"id":639}],[{"start":{"row":13,"column":55},"end":{"row":13,"column":56},"action":"insert","lines":[" "],"id":640}],[{"start":{"row":13,"column":56},"end":{"row":13,"column":58},"action":"insert","lines":["\"\""],"id":641}],[{"start":{"row":13,"column":57},"end":{"row":13,"column":58},"action":"insert","lines":["m"],"id":642},{"start":{"row":13,"column":58},"end":{"row":13,"column":59},"action":"insert","lines":["e"]},{"start":{"row":13,"column":59},"end":{"row":13,"column":60},"action":"insert","lines":["s"]},{"start":{"row":13,"column":60},"end":{"row":13,"column":61},"action":"insert","lines":["s"]},{"start":{"row":13,"column":61},"end":{"row":13,"column":62},"action":"insert","lines":["a"]},{"start":{"row":13,"column":62},"end":{"row":13,"column":63},"action":"insert","lines":["g"]},{"start":{"row":13,"column":63},"end":{"row":13,"column":64},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":64},"end":{"row":13,"column":65},"action":"insert","lines":["0"],"id":643}],[{"start":{"row":13,"column":64},"end":{"row":13,"column":65},"action":"remove","lines":["0"],"id":644}],[{"start":{"row":13,"column":65},"end":{"row":13,"column":66},"action":"insert","lines":[":"],"id":645}],[{"start":{"row":13,"column":66},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":646},{"start":{"row":14,"column":0},"end":{"row":14,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":8},"action":"remove","lines":["    "],"id":647},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]},{"start":{"row":13,"column":66},"end":{"row":14,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":13,"column":66},"end":{"row":13,"column":67},"action":"insert","lines":[" "],"id":648},{"start":{"row":13,"column":67},"end":{"row":13,"column":68},"action":"insert","lines":["m"]},{"start":{"row":13,"column":68},"end":{"row":13,"column":69},"action":"insert","lines":["e"]},{"start":{"row":13,"column":69},"end":{"row":13,"column":70},"action":"insert","lines":["s"]},{"start":{"row":13,"column":70},"end":{"row":13,"column":71},"action":"insert","lines":["s"]}],[{"start":{"row":13,"column":71},"end":{"row":13,"column":72},"action":"insert","lines":["a"],"id":649},{"start":{"row":13,"column":72},"end":{"row":13,"column":73},"action":"insert","lines":["g"]},{"start":{"row":13,"column":73},"end":{"row":13,"column":74},"action":"insert","lines":["e"]},{"start":{"row":13,"column":74},"end":{"row":13,"column":75},"action":"insert","lines":["}"]}],[{"start":{"row":15,"column":19},"end":{"row":15,"column":65},"action":"remove","lines":["(\"({}) {}: {}\".format(now, username, message))"],"id":650}],[{"start":{"row":15,"column":19},"end":{"row":15,"column":21},"action":"insert","lines":["()"],"id":651}],[{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"insert","lines":["m"],"id":652},{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["e"]},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["s"]},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":["s"]},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"insert","lines":["a"]},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":["g"]},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"insert","lines":["e"]},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["_"],"id":653},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["d"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["i"]},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"insert","lines":["c"]},{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"insert","lines":["r"]}],[{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"remove","lines":["r"],"id":654}],[{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"insert","lines":["t"],"id":655}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "],"id":656},{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":18,"column":12},"end":{"row":20,"column":0},"action":"remove","lines":["ll of the messages and separate them with a `br`\"\"\"","    return \"<br>\".join(messages)",""],"id":657},{"start":{"row":17,"column":6},"end":{"row":19,"column":0},"action":"insert","lines":["ll of the messages and separate them with a `br`\"\"\"","    return \"<br>\".join(messages)",""]}],[{"start":{"row":16,"column":0},"end":{"row":20,"column":12},"action":"remove","lines":["","def gell of the messages and separate them with a `br`\"\"\"","    return \"<br>\".join(messages)","t_all_messages():","    \"\"\"Get a"],"id":658},{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"remove","lines":["",""]},{"start":{"row":14,"column":34},"end":{"row":15,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":31,"column":55},"end":{"row":31,"column":63},"action":"remove","lines":["get_all_"],"id":659}],[{"start":{"row":31,"column":64},"end":{"row":31,"column":65},"action":"insert","lines":["0"],"id":660}],[{"start":{"row":31,"column":64},"end":{"row":31,"column":65},"action":"remove","lines":["0"],"id":661}],[{"start":{"row":31,"column":64},"end":{"row":31,"column":65},"action":"remove","lines":[")"],"id":662},{"start":{"row":31,"column":63},"end":{"row":31,"column":65},"action":"remove","lines":["()"]}],[{"start":{"row":31,"column":63},"end":{"row":31,"column":64},"action":"insert","lines":[")"],"id":663}],[{"start":{"row":31,"column":11},"end":{"row":31,"column":64},"action":"remove","lines":["\"<h1>Welcome, {0}</h1>{1}\".format(username, messages)"],"id":664}],[{"start":{"row":31,"column":11},"end":{"row":31,"column":12},"action":"insert","lines":["r"],"id":665},{"start":{"row":31,"column":12},"end":{"row":31,"column":13},"action":"insert","lines":["e"]},{"start":{"row":31,"column":13},"end":{"row":31,"column":14},"action":"insert","lines":["d"]},{"start":{"row":31,"column":14},"end":{"row":31,"column":15},"action":"insert","lines":["n"]},{"start":{"row":31,"column":15},"end":{"row":31,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":31,"column":15},"end":{"row":31,"column":16},"action":"remove","lines":["e"],"id":666},{"start":{"row":31,"column":14},"end":{"row":31,"column":15},"action":"remove","lines":["n"]},{"start":{"row":31,"column":13},"end":{"row":31,"column":14},"action":"remove","lines":["d"]}],[{"start":{"row":31,"column":13},"end":{"row":31,"column":14},"action":"insert","lines":["n"],"id":667},{"start":{"row":31,"column":14},"end":{"row":31,"column":15},"action":"insert","lines":["d"]},{"start":{"row":31,"column":15},"end":{"row":31,"column":16},"action":"insert","lines":["e"]},{"start":{"row":31,"column":16},"end":{"row":31,"column":17},"action":"insert","lines":["r"]}],[{"start":{"row":31,"column":11},"end":{"row":31,"column":17},"action":"remove","lines":["render"],"id":668},{"start":{"row":31,"column":11},"end":{"row":31,"column":26},"action":"insert","lines":["render_template"]}],[{"start":{"row":31,"column":26},"end":{"row":31,"column":28},"action":"insert","lines":["()"],"id":669}],[{"start":{"row":31,"column":27},"end":{"row":31,"column":29},"action":"insert","lines":["\"\""],"id":670}],[{"start":{"row":31,"column":28},"end":{"row":31,"column":29},"action":"insert","lines":["c"],"id":671},{"start":{"row":31,"column":29},"end":{"row":31,"column":30},"action":"insert","lines":["h"]},{"start":{"row":31,"column":30},"end":{"row":31,"column":31},"action":"insert","lines":["a"]},{"start":{"row":31,"column":31},"end":{"row":31,"column":32},"action":"insert","lines":["t"]},{"start":{"row":31,"column":32},"end":{"row":31,"column":33},"action":"insert","lines":["."]},{"start":{"row":31,"column":33},"end":{"row":31,"column":34},"action":"insert","lines":["h"]},{"start":{"row":31,"column":34},"end":{"row":31,"column":35},"action":"insert","lines":["t"]},{"start":{"row":31,"column":35},"end":{"row":31,"column":36},"action":"insert","lines":["m"]},{"start":{"row":31,"column":36},"end":{"row":31,"column":37},"action":"insert","lines":["l"]}],[{"start":{"row":31,"column":38},"end":{"row":31,"column":39},"action":"insert","lines":[" "],"id":672}],[{"start":{"row":31,"column":38},"end":{"row":31,"column":39},"action":"remove","lines":[" "],"id":673}],[{"start":{"row":31,"column":38},"end":{"row":31,"column":39},"action":"insert","lines":[","],"id":674}],[{"start":{"row":31,"column":39},"end":{"row":31,"column":40},"action":"insert","lines":[" "],"id":675},{"start":{"row":31,"column":40},"end":{"row":31,"column":41},"action":"insert","lines":["u"]},{"start":{"row":31,"column":41},"end":{"row":31,"column":42},"action":"insert","lines":["s"]},{"start":{"row":31,"column":42},"end":{"row":31,"column":43},"action":"insert","lines":["e"]},{"start":{"row":31,"column":43},"end":{"row":31,"column":44},"action":"insert","lines":["r"]},{"start":{"row":31,"column":44},"end":{"row":31,"column":45},"action":"insert","lines":["n"]}],[{"start":{"row":31,"column":45},"end":{"row":31,"column":46},"action":"insert","lines":["]"],"id":676}],[{"start":{"row":31,"column":45},"end":{"row":31,"column":46},"action":"remove","lines":["]"],"id":677}],[{"start":{"row":31,"column":45},"end":{"row":31,"column":46},"action":"insert","lines":["a"],"id":678}],[{"start":{"row":31,"column":40},"end":{"row":31,"column":46},"action":"remove","lines":["userna"],"id":679},{"start":{"row":31,"column":40},"end":{"row":31,"column":48},"action":"insert","lines":["username"]}],[{"start":{"row":31,"column":48},"end":{"row":31,"column":49},"action":"insert","lines":[" "],"id":680},{"start":{"row":31,"column":49},"end":{"row":31,"column":50},"action":"insert","lines":["="]}],[{"start":{"row":31,"column":50},"end":{"row":31,"column":51},"action":"insert","lines":[" "],"id":681}],[{"start":{"row":31,"column":51},"end":{"row":31,"column":52},"action":"insert","lines":["u"],"id":682},{"start":{"row":31,"column":52},"end":{"row":31,"column":53},"action":"insert","lines":["s"]},{"start":{"row":31,"column":53},"end":{"row":31,"column":54},"action":"insert","lines":["e"]},{"start":{"row":31,"column":54},"end":{"row":31,"column":55},"action":"insert","lines":["r"]}],[{"start":{"row":31,"column":55},"end":{"row":31,"column":56},"action":"insert","lines":["n"],"id":683},{"start":{"row":31,"column":56},"end":{"row":31,"column":57},"action":"insert","lines":["a"]},{"start":{"row":31,"column":57},"end":{"row":31,"column":58},"action":"insert","lines":[","]}],[{"start":{"row":31,"column":57},"end":{"row":31,"column":58},"action":"remove","lines":[","],"id":684}],[{"start":{"row":31,"column":57},"end":{"row":31,"column":58},"action":"insert","lines":["m"],"id":685},{"start":{"row":31,"column":58},"end":{"row":31,"column":59},"action":"insert","lines":["e"]},{"start":{"row":31,"column":59},"end":{"row":31,"column":60},"action":"insert","lines":[","]}],[{"start":{"row":31,"column":60},"end":{"row":31,"column":61},"action":"insert","lines":[" "],"id":686},{"start":{"row":31,"column":61},"end":{"row":31,"column":62},"action":"insert","lines":["c"]},{"start":{"row":31,"column":62},"end":{"row":31,"column":63},"action":"insert","lines":["h"]},{"start":{"row":31,"column":63},"end":{"row":31,"column":64},"action":"insert","lines":["a"]}],[{"start":{"row":31,"column":64},"end":{"row":31,"column":65},"action":"insert","lines":["t"],"id":687}],[{"start":{"row":31,"column":61},"end":{"row":31,"column":65},"action":"remove","lines":["chat"],"id":688},{"start":{"row":31,"column":61},"end":{"row":31,"column":74},"action":"insert","lines":["chat_messages"]}],[{"start":{"row":31,"column":74},"end":{"row":31,"column":75},"action":"insert","lines":[" "],"id":689},{"start":{"row":31,"column":75},"end":{"row":31,"column":76},"action":"insert","lines":["="]}],[{"start":{"row":31,"column":76},"end":{"row":31,"column":77},"action":"insert","lines":[" "],"id":690},{"start":{"row":31,"column":77},"end":{"row":31,"column":78},"action":"insert","lines":["m"]},{"start":{"row":31,"column":78},"end":{"row":31,"column":79},"action":"insert","lines":["e"]},{"start":{"row":31,"column":79},"end":{"row":31,"column":80},"action":"insert","lines":["s"]},{"start":{"row":31,"column":80},"end":{"row":31,"column":81},"action":"insert","lines":["s"]},{"start":{"row":31,"column":81},"end":{"row":31,"column":82},"action":"insert","lines":["a"]},{"start":{"row":31,"column":82},"end":{"row":31,"column":83},"action":"insert","lines":["g"]},{"start":{"row":31,"column":83},"end":{"row":31,"column":84},"action":"insert","lines":["e"]}],[{"start":{"row":31,"column":84},"end":{"row":31,"column":85},"action":"insert","lines":["7"],"id":691},{"start":{"row":31,"column":85},"end":{"row":31,"column":86},"action":"insert","lines":["-"]}],[{"start":{"row":31,"column":85},"end":{"row":31,"column":86},"action":"remove","lines":["-"],"id":692},{"start":{"row":31,"column":84},"end":{"row":31,"column":85},"action":"remove","lines":["7"]}],[{"start":{"row":31,"column":84},"end":{"row":31,"column":85},"action":"insert","lines":["s"],"id":693}],[{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"insert","lines":["s"],"id":694}],[{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"remove","lines":["."],"id":695}],[{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["_"],"id":696}]]},"ace":{"folds":[],"scrolltop":180.6171875,"scrollleft":0,"selection":{"start":{"row":14,"column":34},"end":{"row":14,"column":34},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":2,"state":"start","mode":"ace/mode/python"}},"timestamp":1564145632745,"hash":"784397f2db29e1ad106685ede2834aef2ba1978f"}