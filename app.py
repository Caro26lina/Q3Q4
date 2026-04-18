from flask import Flask,request,render_template_string
app=Flask(__name__)
tasks=[]
@app.route('/')
def home():
    html="""
    <h2>TO-DO List</h2>
    <form method='post' action='/add'>
        <input type="text" name="task" placeholder="Enter a task">
        <button type=submit>ADD</button>
    </form>
    <ul>
        {%for t in tasks %}
            <li>{{t}}</li>
        {%endfor%}
    </ul>
    """
    return render_template_string(html,tasks=tasks)
@app.route('/add', methods=['post'])
def add_task():
    task=request.form['task']
    tasks.append(task)
    return "Task Added" \
    "<a href='/'> Go Bach</a>"
if __name__=='__main__':
    app.run(debug=True)