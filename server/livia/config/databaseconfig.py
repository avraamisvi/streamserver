from livia.model.base import Base

engine = create_engine("mysql://root:123456@localhost/livia")
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
#session = Session()

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()