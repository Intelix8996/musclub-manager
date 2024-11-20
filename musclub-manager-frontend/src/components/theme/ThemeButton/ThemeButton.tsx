'use client';

import React from "react";

import { Button, Icon } from "@gravity-ui/uikit";
import { Moon, Sun } from '@gravity-ui/icons';

import { DARK_THEME, LIGHT_THEME, ThemeContext } from "../ThemeContext/ThemeContext";

export const ThemeButton = () => {
    const { theme, setTheme } = React.useContext(ThemeContext);

    const isDark = theme === DARK_THEME;

    return (
        <Button
            size="l"
            view="outlined"
            onClick={() => {
                setTheme(isDark ? LIGHT_THEME : DARK_THEME);
            }}
        >
            <Icon data={isDark ? Sun : Moon} />
        </Button>
    );
};
