from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from app.repositories.model import Base # Added import

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

# Import all model modules here so Base.metadata is populated
import app.repositories.rakuten_bank.model
import app.repositories.sbi_shinsei_bank.model
import app.repositories.sumishin_sbi_bank.model
import app.repositories.sbi_benefit_system.model
import app.repositories.mitsuisumitomo_bank.model
import app.repositories.mitsuisumitomo_card.model # New model

target_metadata = Base.metadata # Changed to use Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    # For autogenerate in "offline" mode (no DB connection),
    # we don't need a URL if we're just comparing metadata.
    # However, context.configure might still expect it.
    # Let's provide a dummy URL if the real one is commented out in alembic.ini
    # or handle it by passing url=None if that's supported for pure metadata diff.
    # For now, to avoid KeyError and assuming autogen might not need a real URL.
    
    # If we are truly offline for autogen, url can be None.
    # The main thing is that target_metadata is set.
    # If 'sqlalchemy.url' is commented out, get_main_option will return None if no default is set.
    # Forcing url=None for pure metadata comparison in offline mode for autogenerate
    context.configure(
        url=None, 
        target_metadata=target_metadata,
        # literal_binds=True, # Removed as it's not compatible with offline autogen diff
        # dialect_opts={"paramstyle": "named"}, # Removed for simplicity
        dialect_name="postgresql"
    )

    # Removed with context.begin_transaction(): for offline autogenerate
    # Also removing context.run_migrations() as it's not needed for autogen setup
    # The autogenerate process itself will use the configured context.


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


# Determine if running in offline or online mode based on sqlalchemy.url presence
db_url_for_mode_check = config.get_main_option("sqlalchemy.url", None)

if not db_url_for_mode_check:
    # If sqlalchemy.url is not set (commented out), run in offline mode.
    # This is to ensure autogenerate can run without a live DB.
    import logging # Make sure logging is imported if not already
    logger = logging.getLogger("alembic.env")
    logger.info("sqlalchemy.url is not configured in alembic.ini, running in offline mode.")
    run_migrations_offline()
else:
    # If sqlalchemy.url is set, proceed with online mode.
    run_migrations_online()
