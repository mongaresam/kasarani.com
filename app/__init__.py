# app/__init__.py
# ─────────────────────────────────────────────────────────────────
# FIX 1: Removed duplicate create_app() definition.
# FIX 2: Added missing import of `config` dict (was only importing Config class).
# FIX 3: Blueprint registrations are complete and correct.
# ─────────────────────────────────────────────────────────────────
from flask import Flask
from app.extensions import db, migrate, login_manager
from app.config import Config, config          # ← fix: import `config` dict too


def create_app(config_name: str = "development") -> Flask:
    """Application factory — call with a config key string."""
    app = Flask(__name__, instance_relative_config=True)

    # Load config object from the dict keyed by config_name
    app.config.from_object(config[config_name])

    # Load optional instance/config.py overrides (silent if absent)
    app.config.from_pyfile("config.py", silent=True)

    # ── Extensions ──────────────────────────────────────────────
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # ── Blueprints ──────────────────────────────────────────────
    from .blueprints.auth          import auth_bp
    from .blueprints.dashboard     import dashboard_bp
    from .blueprints.academic      import academic_bp
    from .blueprints.results       import results_bp
    from .blueprints.library       import library_bp
    from .blueprints.store         import store_bp
    from .blueprints.students      import students_bp
    from .blueprints.communication import communication_bp
    from .blueprints.timetable     import timetable_bp
    from .blueprints.reports       import reports_bp
    from .blueprints.announcements import announcements_bp
    from .blueprints.settings      import settings_bp

    for bp in (
        auth_bp, dashboard_bp, academic_bp, results_bp,
        library_bp, store_bp, students_bp, communication_bp,
        timetable_bp, reports_bp, announcements_bp, settings_bp,
    ):
        app.register_blueprint(bp)

    return app
