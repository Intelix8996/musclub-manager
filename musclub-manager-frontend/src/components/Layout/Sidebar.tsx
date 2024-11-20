'use client';

import React from 'react';

import PersonsIcon from '@gravity-ui/icons/svgs/persons.svg';
import CalendarIcon from '@gravity-ui/icons/svgs/calendar.svg';
import NodesLeftIcon from '@gravity-ui/icons/svgs/nodes-left.svg';

import MusclubIcon from '../../assets/logo.svg';

import { AppRouterInstance } from 'next/dist/shared/lib/app-router-context.shared-runtime';
import { usePathname, useRouter } from 'next/navigation';

import { AsideHeader, LogoProps, MenuItem, SubheaderMenuItem } from "@gravity-ui/navigation";

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

type MenuItemWithRoute = MenuItem & {
    route: string,
}

const asideMenuItems: MenuItemWithRoute[] = [
    {
        id: "membersButton",
        title: "Members",
        icon: PersonsIcon,

        route: "/members",
    },
    {
        id: "eventsButton",
        title: "Events",
        icon: CalendarIcon,

        route: "/events",
    }
];

function generateAsideMenuItems(pathname: string, router: AppRouterInstance): MenuItem[] {
    return asideMenuItems.map(item => {
        item.current = pathname === item.route;
        item.onItemClick = () => {
            router.push(item.route);
        }

        return item;
    });
}

export const Sidebar = ({children}: {children: React.ReactNode}) => {
    const [compact, setCompact] = React.useState<boolean>(false);

    const pathname = usePathname();
    const router = useRouter();
    
    return (
        <AsideHeader
            compact={compact}
            headerDecoration={true}

            logo={asideLogo}
            // subheaderItems={asideSubheaderItems} // Causes hydratation error
            menuItems={generateAsideMenuItems(pathname, router)}

            renderContent={() => {
                return children;
            }}

            onChangeCompact={() => {
                setCompact(!compact)
            }}
        />
    );
}
