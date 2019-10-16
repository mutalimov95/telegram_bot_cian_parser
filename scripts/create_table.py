from models import ChatLink
from settings import db


if __name__ == '__main__':
    db.create_tables([ChatLink])

