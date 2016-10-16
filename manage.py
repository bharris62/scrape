import click
from flask import current_app

from supps import create_app
from supps.extensions import db

HERE = ''

app = create_app()


@app.cli.command()
def list_routes():
    """ List available routes in the application."""
    output = []
    for rule in current_app.url_map.iter_rules():

        methods = ','.join(rule.methods)
        url = str(rule)
        if '_debug_toolbar' in url:
            continue
        line = "{:50s} {:30s} {}".format(rule.endpoint, methods, url)
        output.append(line)

    click.echo('\n'.join(sorted(output)))

    return


@app.cli.command()
def create_db():
    db.create_all()
    db.session.commit()
    click.echo('Database has been created')

    return


@app.cli.command()
def run_scrapers():
    # from supps.tasks.bb_casein import scrape_bodybuilding_casein
    from supps.tasks.bb_whey import scrape_bodybuilding_whey
    # from supps.tasks.vs_whey import scrape_vitamin_shoppe_whey
    click.echo('Running Scrapers!')
    # scrape_bodybuilding_casein()
    scrape_bodybuilding_whey()
    # scrape_vitamin_shoppe_whey()
    click.echo('Scrapers Finished!')

    return


if __name__ == '__main__':
    app.cli()
