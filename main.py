from flask import Flask

def index():    
    return '''
    <!DOCTYPE html>
<html>
<head>
<title>Компания "Импульс"</title>
</head>
<body>

<h1>
Список сотрудников компании "Импульс"
</h1>

<h2>
Отдел разработки:
</h2>
<p>
<ul>
<li>Главный разработчик - Иванов Иван</li>
<li>Младший разработчик - Степанов Степан</li>
<li>Тестировщик - Данилов Данил</li>
</ul>
</p>
<h2>
Бухгалтерия:
</h2>
<p>
<ul>
<li>Старший бухгалтер - Александров Александр</li>
<li>Бухгалтер - Тимофеев Тимофей</li>
</ul>
</p>
    </body>
</html>
'''



app = Flask(__name__)   

app.add_url_rule('/', 'index', index)   


if __name__ == "__main__":
   
    app.run() 
