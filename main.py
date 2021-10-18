from datetime import datetime, timezone

from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

import models
import schema
from crud import create_short_link_db, get_original_link
from db import SessionLocal, engine
from service import create_short_link

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/api/shorten')
async def get_short_link(created_url: schema.ShortenUrl, db: Session = Depends(get_db)):
    timestamp = datetime.now().replace(tzinfo=timezone.utc).timestamp()
    short_link = create_short_link(created_url.url, timestamp)
    try:
        create_short_link_db(db, original=created_url.url, short_link=short_link)
        return {"short_link": short_link}
    except Exception as e:
        return {
            "error": str(e)
        }


@app.get("/{short_url}")
async def redirect_to(short_url: str, db: Session = Depends(get_db)):
    obj = get_original_link(db, short_link=short_url)
    if obj is None:
        raise HTTPException(status_code=404, detail="The link does not exist, could not redirect")
    return RedirectResponse(url=obj.original_url)
