'use client';

import React from 'react';

import PersonsIcon from '@gravity-ui/icons/svgs/persons.svg';
import CalendarIcon from '@gravity-ui/icons/svgs/calendar.svg';
import NodesLeftIcon from '@gravity-ui/icons/svgs/nodes-left.svg';

import MusclubIcon from '../../assets/logo.svg';

import { AsideHeader, LogoProps, MenuItem, SubheaderMenuItem } from "@gravity-ui/navigation";
import { usePathname } from 'next/navigation';

const asideLogo: LogoProps = {text: "Musclub Manager", icon: MusclubIcon};

const asideSubheaderItems: SubheaderMenuItem[] = [
    {
        item: {
            id: "dashboardButton",
            title: "Dashboard",
            icon: NodesLeftIcon,
        },
    }
]

const asideMenuItems: MenuItem[] = [
    {
        id: "membersButton",
        title: "Members",
        icon: PersonsIcon,
        link: "/members"
    },
    {
        id: "eventsButton",
        title: "Events",
        icon: CalendarIcon,
        link: "/events"
    }
];

function generateAsideMenuItems(pathname: string): MenuItem[] {
    return asideMenuItems.map(item => {
        item.current = pathname === item.link;

        return item;
    });
}

export const Sidebar = ({children}: {children: React.ReactNode}) => {
    const [compact, setCompact] = React.useState<boolean>(false);
    const pathname = usePathname();
    
    return (
        <AsideHeader
            compact={compact}
            headerDecoration={true}

            logo={asideLogo}
            // subheaderItems={asideSubheaderItems} // Causes hydratation error
            menuItems={generateAsideMenuItems(pathname)}

            renderContent={() => {
                return children;
            }}

            onChangeCompact={() => {
                setCompact(!compact)
            }}
        />
    );
}
