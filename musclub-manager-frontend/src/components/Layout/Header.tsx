'use client';

import { Breadcrumbs, FirstDisplayedItemsCount, LastDisplayedItemsCount } from "@gravity-ui/uikit";
import { ThemeButton } from "../theme/ThemeButton/ThemeButton";
import React from "react";
import { usePathname } from "next/navigation";

export const Header = () => {
    const category = usePathname();
    
    return (
        <div className="flex">
            <div className="flex-grow flex items-center gap-5 m-5">
                <Breadcrumbs
                    items={[
                        { text: "Home", title: "HomeTitle", action: () => { console.log("Home") } },
                        { text: category, action: () => { console.log("Home") } },
                    ]}
                    lastDisplayedItemsCount={LastDisplayedItemsCount.Two}
                    firstDisplayedItemsCount={FirstDisplayedItemsCount.One}
                />
            </div>
            <div className="flex-none m-5 flex items-center">
                <ThemeButton />
            </div>
        </div>
    );
};
