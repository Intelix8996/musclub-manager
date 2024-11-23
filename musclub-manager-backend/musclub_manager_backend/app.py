import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import selectinload
from starlette.status import HTTP_404_NOT_FOUND

from musclub_manager_backend.db_models import Member
from musclub_manager_backend.json_models import MemberBrief, MembersResponse, SpecialisationFull, InstrumentFull, \
    MemberResponse, MemberFull

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

origins = [
    "*",
]

# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = create_async_engine(f"postgresql+asyncpg://{os.environ['DB_URL']}", echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)


@app.get("/members")
async def members() -> MembersResponse:
    async with (async_session() as session):
        result = select(Member).options(selectinload(Member.specialisations), selectinload(Member.instruments))
        result = await session.scalars(result)

        return MembersResponse(
            members={
                i.id: MemberBrief(full_name=i.full_name,
                                  status=i.status,
                                  specialisations={j.id: SpecialisationFull(title=j.title) for j in i.specialisations},
                                  instruments={j.id: InstrumentFull(title=j.title) for j in i.instruments},
                                  )
                for i in result
            }
        )


@app.get("/member/{member_id}")
async def members(member_id: int) -> MemberResponse:
    async with (async_session() as session):
        stmt = select(Member).where(Member.id == member_id).options(selectinload(Member.specialisations),
                                                                    selectinload(Member.instruments))
        result = (await session.scalars(stmt)).one_or_none()

        if not result:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND,
                detail=f'Member with id {member_id} not found',
            )

        return MemberResponse(
            member=MemberFull(
                full_name=result.full_name,
                photo_url=result.photo_url,
                telegram=result.telegram,
                socials=result.socials,
                status=result.status,
                specialisations={j.id: SpecialisationFull(title=j.title) for j in result.specialisations},
                instruments={j.id: InstrumentFull(title=j.title) for j in result.instruments},
                repertoire=result.repertoire,
                band_structure=result.band_structure,
                notes=result.notes,
            )
        )
