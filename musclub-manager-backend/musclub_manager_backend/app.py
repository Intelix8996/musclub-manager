import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import selectinload
from starlette.status import HTTP_404_NOT_FOUND

from musclub_manager_backend.db_models import Member
from musclub_manager_backend.json_models import MemberBrief, MembersResponse, SpecialisationFull, InstrumentFull, \
    MemberResponse, MemberFull, Social

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
async def list_members_brief() -> MembersResponse:
    async with (async_session() as session):
        result = select(Member).options(selectinload(Member.specialisations), selectinload(Member.instruments))
        result = await session.scalars(result)

        return MembersResponse(
            members=[
                MemberBrief(
                    id=i.id,
                    full_name=i.full_name,
                    status=i.status,
                    specialisations=[SpecialisationFull(id=j.id, title=j.title) for j in i.specialisations],
                    instruments=[InstrumentFull(id=j.id, title=j.title) for j in i.instruments],
                )
                for i in result
            ]
        )


@app.get("/member/{member_id}")
async def get_member(member_id: int) -> MemberResponse:
    async with (async_session() as session):
        stmt = select(Member).where(Member.id == member_id).options(selectinload(Member.specialisations),
                                                                    selectinload(Member.instruments))
        result = (await session.scalars(stmt)).one_or_none()

        if not result:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND,
                detail=f'Member with id {member_id} not found',
            )

        socials: dict[str, str] = result.socials

        return MemberResponse(
            member=MemberFull(
                id=member_id,
                full_name=result.full_name,
                photo_url=result.photo_url,
                telegram=result.telegram,
                socials=[Social(service=i, username=j) for i, j in socials.items()],
                status=result.status,
                specialisations=[SpecialisationFull(id=j.id, title=j.title) for j in result.specialisations],
                instruments=[InstrumentFull(id=j.id, title=j.title) for j in result.instruments],
                repertoire=result.repertoire,
                band_structure=result.band_structure,
                notes=result.notes,
            )
        )


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name


use_route_names_as_operation_ids(app)