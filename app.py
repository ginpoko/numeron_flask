from flask import Flask,render_template, request, redirect, url_for

app = Flask(__name__)

class Numbers:
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third

@app.route('/start', methods=['GET','POST'])
def wait():
    if request.method == 'GET':
        return render_template('wait.html')
    else:
        my_numbers = Numbers(
            request.form.get('my_first'),
            request.form.get('my_second'),
            request.form.get('my_third'),
        )
        # この部分をNOじゃなくてwait上に同じ値が含まれていると言う警告を出す
        if my_numbers.first == my_numbers.second:
            return render_template('wait.html',change=1)
        elif my_numbers.second == my_numbers.third:
            return render_template('wait.html',change=1)
        elif my_numbers.first == my_numbers.third:
            return render_template('wait.html',change=1)
        else:
            return render_template('wait.html',change=2, numbers=my_numbers)


@app.route('/play', methods=['GET'])
def play():
    if request.method == 'GET':
        return render_template('play.html')
    else:
        pass


# @app.route('/judge')
# def judge():
#     pass


@app.errorhandler(404)
def page_not_found(error):
    return render_template('title.html'), 404

if __name__ == '__main__':
    app.run()
