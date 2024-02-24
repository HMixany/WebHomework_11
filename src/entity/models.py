from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date
from sqlalchemy.orm import DeclarativeBase, column_property
from sqlalchemy.sql.expression import func


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(120), nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    phone: Mapped[str] = mapped_column(String(100), nullable=False)
    birthday: Mapped[str] = mapped_column(Date)
    description: Mapped[str] = mapped_column(String(250), nullable=True)
    birthday_this_year = column_property(func.concat(func.date_part("YYYY", func.current_date()), "-",
                                                     func.date_part("MM", birthday), "-",
                                                     func.date_part("DD", birthday)).cast(Date))
