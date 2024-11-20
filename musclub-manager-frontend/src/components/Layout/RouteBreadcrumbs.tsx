import { Breadcrumbs, BreadcrumbsItem, FirstDisplayedItemsCount, LastDisplayedItemsCount } from "@gravity-ui/uikit";
import { usePathname, useRouter } from "next/navigation";

type BreadcrumbFormatter = (item: string) => string;

const breadcrumbsFormatters: BreadcrumbFormatter[] = [
    (item) => {
        return item.toUpperCase();
    },
];

type PathSegment = {
    text: string,
    route: string,
}

function formatPath(path: string): PathSegment[] {
    let pathSegments = path.split("/");
    pathSegments.shift();

    let formattedPathSegments: PathSegment[] = [];
    let route = "";

    for (let i = 0; i < pathSegments.length; ++i) {
        const formatter = breadcrumbsFormatters[i];
        const segment = pathSegments[i];

        route += "/" + segment;

        const pathSegment = {
            text: (formatter != null && segment != "") ? formatter(segment) : segment,
            route: route,
        };

        formattedPathSegments.push(pathSegment);
    }

    return formattedPathSegments;
}

const ROOT_SEGMENT: PathSegment = {
    text: "Musclub Manager",
    route: "/"
};

export const RouteBreadcrumbs = () => {
    const router = useRouter();
    const path = usePathname();

    const formattedPathSegments = [ROOT_SEGMENT].concat(formatPath(path));

    const breadcrumbsItems = formattedPathSegments.map((segment) => {
        return { text: segment.text, action: () => { router.push(segment.route) } } as BreadcrumbsItem;
    });

    return (
        <Breadcrumbs
            items={breadcrumbsItems}
            lastDisplayedItemsCount={LastDisplayedItemsCount.Two}
            firstDisplayedItemsCount={FirstDisplayedItemsCount.One}
        />
    );
}
