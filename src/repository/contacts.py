from datetime import datetime, date, timedelta
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from src.entity.models import Contact
from src.schemas.contact import ContactSchema


async def get_contacts(limit: int, offset: int, db: AsyncSession):
    stmt = select(Contact).offset(offset).limit(limit)
    contacts = await db.execute(stmt)
    return contacts.scalars().all()


async def get_contact(contact_id: int, db: AsyncSession):
    stmt = select(Contact).filter_by(id=contact_id)
    contact = await db.execute(stmt)
    return contact.scalar_one_or_none()


async def create_contact(body: ContactSchema, db: AsyncSession):
    contact = Contact(**body.model_dump(exclude_unset=True))
    db.add(contact)
    await db.commit()
    await db.refresh(contact)
    return contact


async def update_contact(contact_id: int, body: ContactSchema, db: AsyncSession):
    stmt = select(Contact).filter_by(id=contact_id)
    result = await db.execute(stmt)
    contact = result.scalar_one_or_none()
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone = body.phone
        contact.birthday = body.birthday
        contact.description = body.description
        await db.commit()
        await db.refresh(contact)
    return contact


async def delete_contact(contact_id: int, db: AsyncSession):
    stmt = select(Contact).filter_by(id=contact_id)
    result = await db.execute(stmt)
    contact = result.scalar_one_or_none()
    if contact:
        await db.delete(contact)
        await db.commit()
    return contact


async def get_birthday_users(db: AsyncSession):
    today = date.today()
    next_week = today + timedelta(days=7)
    res = []
    stmt = select(Contact)
    results = await db.execute(stmt)
    contacts = results.scalars().all()
    for contact in contacts:
        current_birthday = datetime(today.year, contact.birthday.month, contact.birthday.day).date()
        if today <= current_birthday < next_week:
            res.append(contact)
    return res


async def find_contacts(search: str, db: AsyncSession):
    stmt = select(Contact).filter(or_(Contact.first_name.ilike(f"%{search}%"), Contact.last_name.ilike(f"%{search}%"),
                                      Contact.email.ilike(f"%{search}%")))
    contacts = await db.execute(stmt)
    return contacts.scalars().all()
