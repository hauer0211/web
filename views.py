from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/singinpage.html")
def home():
    return render_template('singinpage.html')
@views.route("/")
def site():
    return render_template("/singinpage.html")

@views.route("/homepage.html")
def homepage():
    books = [
        
        {'singer': 'ZARA',
         'song': 'カーゴパンズ',
         'releas_days': '2020年7月16日',
         'link': 'https://www.youtube.com/watch?v=Fp8msa5uYsc',
         'picture': '/image/ka-go1.jpg'},
        {'singer': 'ZARA',
         'song': 'ジャケット',
         'releas_days': '2023年7月16日',
         'link': 'https://www.youtube.com/watch?v=Mc-wFcieEmU',
         'picture': 'image/jaket1jpg.jpg'
         },
        {'singer': 'DABABY',
         'song': 'ROCKSTAR',
         'releas_days': '2020年7月16日',
         'link': 'https://www.youtube.com/watch?v=83xBPCw5hh4',
         'picture': 'image/jacketstadium1.jpg'},
        {'singer': "Why don't we",
         'song': 'What am i',
         'releas_days': '2020年7月16日',
         'link': 'https://www.youtube.com/watch?v=ZxgbQz4n8-s',
         'picture': 'image/artworks-zF4PkzpZja0GWQrV-WysZqA-t500x500.jpg'},
        {'singer': 'Post Malon',
         'song': 'Goodbyes',
         'releas_days': '2020年7月16日',
         'link': 'https://www.youtube.com/watch?v=ba7mB8oueCY',
         'picture': 'image/artworks-zF4PkzpZja0GWQrV-WysZqA-t500x500.jpg'},
        {'singer': '24kGlodn',
         'song': 'Mood',
         'releas_days': '2020年7月16日',
         'link': 'https://www.youtube.com/watch?v=GrAchTdepsU',
         'picture': 'image/artworks-zF4PkzpZja0GWQrV-WysZqA-t500x500.jpg'},
        {'singer': 'Maroon 5',
         'song': 'Payphone',
         'releas_days': '2012年7月16日',
         'link': 'https://www.youtube.com/watch?v=KRaWnd3LJfs',
         'picture': 'image/artworks-zF4PkzpZja0GWQrV-WysZqA-t500x500.jpg'},
        {'singer': 'Charlie Puth',
         'song': 'Dangerously',
         'releas_days': '2015年7月16日',
         'link': 'https://www.youtube.com/watch?v=TBXQu8ORnBQ',
         'picture': 'artworks-zF4PkzpZja0GWQrV-WysZqA-t500x500.jpg'},
        {'singer': 'Olivia Rodrigo',
         'song': 'Vampire',
         'releas_days': '2023年7月16日',
         'link': 'https://www.youtube.com/watch?v=RlPNh_PBZb4',
         'picture': 'artworks-zF4PkzpZja0GWQrV-WysZqA-t500x500.jpg'},
        {'singer': '50 Cent',
         'song': 'In Da Club',
         'releas_days': '2009年7月16日',
         'link': 'https://www.youtube.com/watch?v=5qm8PH4xAss',
         'picture': 'artworks-zF4PkzpZja0GWQrV-WysZqA-t500x500.jpg'},
        {'singer': 'Dr.Dre ft.Snoop Dogg',
         'song': 'Still D.R.E',
         'releas_days': '2010年7月16日',
         'link': 'https://www.youtube.com/watch?v=_CL6n0FJZpk',
         'picture': 'artworks-zF4PkzpZja0GWQrV-WysZqA-t500x500.jpg'},
    ] 

        
    
    return render_template('homepage.html', books = books)

    
@views.route("/test")
    

@views.route("/singup.html")
def singup():
    return render_template("singup.html") 

@views.route("/hiphop.html")
def hiphop():
    songs = [
        {'singer': 'Dr.Dre',
         'song': 'still D.R.E',
         'releas_days': '2012年2月11日',
         'link': 'https://www.youtube.com/watch?v=_CL6n0FJZpk'},
        {'singer': 'Hanumankind.Kalmi',
         'song': 'Big Dawgs',
         'releas_days': '2024年2月11日',
         'link': 'https://www.youtube.com/watch?v=hOHKltAiKXQ'},
        {'singer': 'you',
         'song': 'yoo',
         'releas_days': '2020年2月11日',
         'link': ''},
        {'singer': 'you',
         'song': 'yoo',
         'releas_days': '2020年2月11日',
         'link': ''},
        
    ]
    
    return render_template('hiphop.html', songs=songs)



@views.route("/test.html")
def search():
    books=[
        {'singer': 'justin biber',
         'song': 'GHOST',
         'releas_days': '2020年7月16日',
         'link': 'https://www.youtube.com/watch?v=Fp8msa5uYsc'},
        {'singer': 'THE KID laroi',
         'song': 'LOVE AGAIN',
         'releas_days': '2020年7月16日',
         'link': 'https://www.youtube.com/watch?v=Mc-wFcieEmU'},
        {'singer': 'DABABY',
         'song': 'ROCKSTAR',
         'releas_days': '2020年7月16日',
         'link': 'https://www.youtube.com/watch?v=83xBPCw5hh4'},
        {'singer': "Why don't we",
         'song': 'What am i',
         'releas_days': '2020年7月16日',
         'link': 'https://www.youtube.com/watch?v=ZxgbQz4n8-s'},
        {'singer': 'Post Malon',
         'song': 'Goodbyes',
         'releas_days': '2020年7月16日',
         'link': 'https://www.youtube.com/watch?v=ba7mB8oueCY'},
        {'singer': '24kGlodn',
         'song': 'Mood',
         'releas_days': '2020年7月16日',
         'link': 'https://www.youtube.com/watch?v=GrAchTdepsU'},
        {'singer': 'Maroon 5',
         'song': 'Payphone',
         'releas_days': '2012年7月16日',
         'link': 'https://www.youtube.com/watch?v=KRaWnd3LJfs'},
        {'singer': 'Charlie Puth',
         'song': 'Dangerously',
         'releas_days': '2015年7月16日',
         'link': 'https://www.youtube.com/watch?v=TBXQu8ORnBQ'},
        {'singer': 'Olivia Rodrigo',
         'song': 'Vampire',
         'releas_days': '2023年7月16日',
         'link': 'https://www.youtube.com/watch?v=RlPNh_PBZb4'},
        {'singer': '50 Cent',
         'song': 'In Da Club',
         'releas_days': '2009年7月16日',
         'link': 'https://www.youtube.com/watch?v=5qm8PH4xAss'},
        {'singer': 'Dr.Dre ft.Snoop Dogg',
         'song': 'Still D.R.E',
         'releas_days': '2010年7月16日',
         'link': 'https://www.youtube.com/watch?v=_CL6n0FJZpk'},
    ] 
        
    
    return render_template('test.html', books = books)

@views.route("/hop.html")
def hop():
    hops=[
        {'singer': 'tt',
         'song': 'tt',
         'releas_days': 'tt',
         'link': 'https://www.youtube.com/watch?v=_CL6n0FJZpk'},
        {'singer': 'tt',
         'song': 'tt',
         'releas_days': 'tt',
         'link': 'https://www.youtube.com/watch?v=_CL6n0FJZpk'}
    ]
    return render_template('hop.html', hops = hops)

@views.route("/jazz.html")
def jazz():
    jazzs = [
        {'singer': 'William John Evans',
         'song': 'Waltz for Debby',
         'releas_days': '2011',
         'link': 'https://www.youtube.com/watch?v=W3wq7ejawIA'},
        {'singer': '',
         'song': '',
         'releas_days': '',
         'link': ''},
        {'singer': '',
         'song': '',
         'releas_days': '',
         'link': ''},
        {'singer': '',
         'song': '',
         'releas_days': '',
         'link': ''}
        
    ]
        
    
    return render_template("jazz.html", jazzs = jazzs )

@views.route("/Setuppage.html")
def setup():
    choices = [
         {'cloth': 'image/whiteshirt.jpg',
          'pattern': 'image/whiteshirtpattern.jpg'}
    ]
    return render_template("Setuppage.html", choices = choices)

@views.route("/MAN.html")
def mans():
    return render_template("MAN.html")

@views.route("/WOMANS.html")
def womens():
    return render_template("WOMANS.html")

@views.route("/SHOES.html")
def shoes():
    return render_template("SHOES.html")

@views.route("/ACCESSORY.html")
def accessory():
    return render_template("ACCESSORY.html")