'use client';

import { Header } from "./Header";
import { Sidebar } from "./Sidebar";

export const Layout = ({children}: {children: React.ReactNode}) => {
    return (
        <Sidebar>
            <Header />
            {children}
        </Sidebar>
    );
}
