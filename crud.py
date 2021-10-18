from sqlalchemy.orm import Session

import models
import schema


def get_original_link(db: Session, short_link: str):
    """
        Функция получения полного урла по короткому урлу
    :param db: Сессия с бд
    :param short_link: короткий урл
    :return:
    """
    return db.query(models.ShortendUrl).filter(models.ShortendUrl.short_link == short_link).first()


def create_short_link_db(db: Session, original: str, short_link: str):
    """
        Функция сохранения короткой ссылки в базу данных
    :param db: сессия с бд
    :param original: Оригинальный урл
    :param short_link: Сжатый урл
    :return:
    """
    db_url = models.ShortendUrl(original_url=original, short_link=short_link)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schema.CreateUser):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
