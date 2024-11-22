from __future__ import annotations

from sqlalchemy import Integer, Enum, Table, Column, ForeignKey, Sequence, JSON
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship


class Base(AsyncAttrs, DeclarativeBase):
    def __repr__(self):
        package = self.__class__.__module__
        class_ = self.__class__.__name__
        attrs = [(k, getattr(self, k)) for k in self.__mapper__.columns.keys()]
        sattrs = ', '.join(f'{key}={value!r}' for key, value in attrs)
        return f'{package}.{class_}({sattrs})'


member_specialisation_relation = Table(
    "member_specialisation_relation",
    Base.metadata,
    Column("member_id", ForeignKey("members.id"), index=True),
    Column("spec_id", ForeignKey("specialisations.id"), index=True),
)
member_instrument_relation = Table(
    "member_instrument_relation",
    Base.metadata,
    Column("member_id", ForeignKey("members.id"), index=True),
    Column("instruments_id", ForeignKey("instruments.id"), index=True),
)


class Member(Base):
    __tablename__ = 'members'

    id: Mapped[int] = mapped_column(Integer, Sequence('members_seq'), primary_key=True, index=True)
    full_name: Mapped[str]
    photo_url: Mapped[str] = mapped_column(nullable=True)

    telegram: Mapped[str] = mapped_column(nullable=True)
    socials: Mapped[dict[str, str]] = mapped_column(JSON, nullable=False)

    status = mapped_column(Enum("active", "inactive", "retired", name="status_enum", create_type=False), nullable=False)
    specialisations: Mapped[list[Specialisation]] = relationship(secondary=member_specialisation_relation,
                                                                 back_populates='members')
    instruments: Mapped[list[Instrument]] = relationship(secondary=member_instrument_relation, back_populates='members')
    repertoire: Mapped[str] = mapped_column(server_default='')
    band_structure: Mapped[str] = mapped_column(server_default='')
    notes: Mapped[str] = mapped_column(server_default='')


class Specialisation(Base):
    __tablename__ = 'specialisations'

    id: Mapped[int] = mapped_column(Integer, Sequence('specialisations_seq'), primary_key=True, index=True)
    title: Mapped[str]
    members: Mapped[list[Member]] = relationship(secondary=member_specialisation_relation,
                                                 back_populates='specialisations')


class Instrument(Base):
    __tablename__ = 'instruments'

    id: Mapped[int] = mapped_column(Integer, Sequence('instruments_seq'), primary_key=True, index=True)
    title: Mapped[str]
    members: Mapped[list[Member]] = relationship(secondary=member_instrument_relation, back_populates='instruments')
