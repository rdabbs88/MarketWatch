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
        stock_data = get_stock_data(ticker, api_key)

        if not stock_data:
            return render_template(
                'result.html', 
                error="Alpha Vantage request failed (possibly rate-limited or invalid ticker). Try again shortly.", 
                form=form, 
                ticker="Unknown")

        df = stock_data["df"]
        plot_url = generate_plot(stock_data, ticker)
        return render_template(
            'result.html', 
            form=form, 
            plot_url=plot_url, 
            ticker=ticker, 
            latest_price=round(stock_data["latest_price"], 2), 
            ma_50=round(stock_data['ma_50'], 2),
            ma_200=round(stock_data["ma_200"], 2),
            pe_ratio=stock_data["pe_ratio"]
        )
    return render_template('index.html', form=form)
