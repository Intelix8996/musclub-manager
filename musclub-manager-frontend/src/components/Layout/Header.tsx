import { ThemeButton } from "../theme/ThemeButton/ThemeButton";
import { RouteBreadcrumbs } from "./RouteBreadcrumbs";

export const Header = () => {
    return (
        <div className="flex">
            <div className="flex-grow flex items-center gap-5 m-5">
                <RouteBreadcrumbs />
            </div>
            <div className="flex-none m-5 flex items-center">
                <ThemeButton />
            </div>
        </div>
    );
};
