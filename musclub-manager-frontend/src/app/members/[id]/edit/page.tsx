export default async function MemberEdit({
    params
}: {
    params: Promise<{ id: number }>
}) {
    const p = await params;

    return (
        <div>
            Editing member with ID: {p.id}
        </div>
    );
}
