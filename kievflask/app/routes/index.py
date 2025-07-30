from app import app
from app.services import chartsKiev, memeService
from flasgger import Swagger, swag_from

swagger = Swagger(app)
@app.route('/whats-the-dog-doing')
@swag_from('../apischema/chart-schema.yml')
def apidoc():
    meme = memeService.get_random_meme()
    return meme, 200

@app.route('/v1/chart/death/<type>/<days>/<sum_type>')
@swag_from('../apischema/total-death.yml')
def totalDeath(type, days, sum_type):
    chart = chartsKiev.get_total_deaths(type, int(days), sum_type)
    return chart, 200

@app.route('/v1/chart/equipment/<days>/<sum_type>')
#@swag_from('../apischema/total-equipment.yml')
def totalEquipment(days, sum_type):
    chart = chartsKiev.get_total_equipment(int(days), sum_type)
    return chart, 200

@app.route('/v1/chart/death-equipment/<days>')
@swag_from('../apischema/death-equipment.yml')
def totalDeathEquipment(days):
    chart = chartsKiev.get_death_and_equipment(int(days))
    return chart, 200

@app.route('/v1/chart/death-enjuried/<type>/<days>')
@swag_from('../apischema/death-enjuried.yml')
def totalDeathSplitted(type,days):
    chart = chartsKiev.get_total_deaths_splitted(type,int(days))
    return chart, 200

@app.route('/v1/chart/tree-tag/<days>')
@swag_from('../apischema/tree-tag.yml')
def treeTagSplitted(days):
    chart = chartsKiev.get_tree_tag_total(int(days))
    return chart, 200

@app.route('/v1/chart/death-article/<days>')
@swag_from('../apischema/death-article.yml')
def barDeathArticle(days):
    chart = chartsKiev.get_death_article(int(days))
    return chart, 200

@app.route('/v1/chart/death-and-article/<days>')
@swag_from('../apischema/death-and-article.yml')
def barArticlesAndTotalsDeath(days):
    chart = chartsKiev.get_articles_and_totals_death(int(days))
    return chart, 200

@app.route('/v1/chart/fire-power/')
@swag_from('../apischema/fire-power.yml')
def barFirePower():
    chart = chartsKiev.get_fire_power()
    return chart, 200

@app.route('/v1/chart/refugees-daily/<days>')
@swag_from('../apischema/refugees-daily.yml')
def get_refugees_daily(days):
    chart = chartsKiev.get_refugees_daily(int(days))
    return chart, 200

@app.route('/v1/chart/refugees-aggregated/')
@swag_from('../apischema/refugees-aggregated.yml')
def get_refugees_aggregated():
    chart = chartsKiev.get_refugees_aggregated()
    return chart, 200

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    header['Access-Control-Allow-Methods'] = 'OPTIONS, HEAD, GET, POST, DELETE, PUT'
    return response
