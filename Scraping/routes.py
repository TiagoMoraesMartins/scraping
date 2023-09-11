from Scraping import app
from flask import render_template
from Scraping.forms import ScrapingForm

@app.route('/')
def index():
    form = ScrapingForm()
    if form.validate_on_submit():
        url = form.url.data
        
        #TODO: 
        #Chamar a função de scraping
        #Scraping(url)
        #Tratar o retorno positivo ou negativo
        #return redirect(url_for('pagina_resultado'))
    return render_template('home.html', form=form)