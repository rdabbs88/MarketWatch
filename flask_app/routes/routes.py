from flask import Blueprint, render_template, current_app
from flask_app.forms import TickerForm
from flask_app.stock import get_stock_data, generate_plot

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET', 'POST'])
def index():
    form = TickerForm()
    plot_url = None
    if form.validate_on_submit():
        ticker = form.ticker.data.upper()
        api_key = current_app.config['ALPHA_VANTAGE_API_KEY']
        data = get_stock_data(ticker, api_key)
        plot_url = generate_plot(data, ticker)
        return render_template('result.html', form=form, plot_url=plot_url, ticker=ticker)
    return render_template('index.html', form=form)
