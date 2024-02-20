from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.entity.models import Contact
from src.schemas.contact import ContactSchema


async def get_contacts(limit: int, offset: int, db: AsyncSession):
    stmt = select(Contact).offset(offset).limit(limit)
    todos = await db.execute(stmt)
    return todos.scalars().all()


async def get_contact(contact_id: int, db: AsyncSession):
    stmt = select(Contact).filter_by(id=contact_id)
    todo = await db.execute(stmt)
    return todo.scalar_one_or_none()


async def create_contact(body: ContactSchema, db: AsyncSession):
    contact = Contact(**body.model_dump(exclude_unset=True))
    db.add(contact)
    await db.commit()
    await db.refresh(contact)
    return contact


async def update_contact(contact_id: int, db: AsyncSession):
    pass


async def delete_contact(contact_id: int, db: AsyncSession):
    pass
