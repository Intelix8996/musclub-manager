import React from "react";

export default async function Member({
    params
}: {
    params: Promise<{ id: string }>
}) {
    const p = await params;

    return (
        <div>
            Member with ID: {p.id}
        </div>
    );
}
