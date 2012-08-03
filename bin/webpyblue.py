import web
render = web.template.render('templates/')

urls = (
  '/', 'index'
)   

app = web.application(urls, globals())

class index:
    def GET(self):
        name = 'Ella, Chloe, and Britt!'
        return render.index(name)

if __name__ == '__main__':
    app.run()
