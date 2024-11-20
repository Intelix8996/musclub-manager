import React from "react";

export default async function Event({
    params
}: {
    params: Promise<{ id: string }>
}) {
    const p = await params;

    return (
        <div>
            Event with ID: {p.id}
        </div>
    );
}
