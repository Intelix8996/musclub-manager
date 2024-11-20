import React from "react";

export default async function EventEdit({
    params
}: {
    params: Promise<{ id: string }>
}) {
    const p = await params;

    return (
        <div>
            Editing event with ID: {p.id}
        </div>
    );
}
