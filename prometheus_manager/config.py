from flask import current_app


def construct_db_url(config, account):
    return f"mysql+pymysql://{config[account]['USERNAME']}:{config[account]['PASSWORD']}@{config['HOST']}/{config['DATABASE']}"


def construct_config(db_account):
    db_config = current_app.config['DATABASE']
    current_app.config['SQLALCHEMY_DATABASE_URI'] = construct_db_url(db_config, db_account)
    current_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
