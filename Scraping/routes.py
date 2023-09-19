from Scraping import app
from flask import render_template
from Scraping.forms import ScrapingForm
from controllers.PesquisaController import PesquisaController

@app.route('/')
def index():
    
    form = ScrapingForm()
    if form.validate_on_submit():
        url = form.url.data
        try:
            df = PesquisaController.GetPesquisa(url)
            print(df)
            #return redirect(url_for('pagina_resultado'))
        except e as error:
            print(error)    
        
    return render_template('home.html', form=form)