# SPDX-FileCopyrightText: 2021-2024 Taavi Väänänen <hi@taavi.wtf>
# SPDX-License-Identifier: AGPL-3.0-only

from flask_alembic import Alembic
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()
alembic = Alembic()
